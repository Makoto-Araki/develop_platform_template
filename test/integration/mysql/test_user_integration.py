import pandas as pd
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.mysql.models import Base, Department, User
from src.mysql.service import DepartmentService, UserService


@pytest.fixture
def gateway():
    """
    ゲートウェイ準備
    """

    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(bind=engine)

    class TestGateway:
        def get_session(self):
            return SessionLocal()

    return TestGateway(), SessionLocal


@pytest.fixture
def seeded_gateway(gateway):
    """
    ゲートウェイからデータ登録
    """

    gateway_obj, SessionLocal = gateway
    session = SessionLocal()

    session.add_all(
        [
            Department(id=1, name="経営"),
            Department(id=2, name="総務"),
            User(id=1, name="Alice", email="alice@test.com", department_id=1),
            User(id=2, name="Bob", email="bob@test.com", department_id=2),
        ]
    )

    session.commit()
    session.close()

    return gateway_obj


def test_get_all_users_integration(seeded_gateway):
    """
    全ユーザー情報取得のテスト
    """

    service = UserService(seeded_gateway)
    df = service.get_all_users()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert set(df["email"]) == {
        "alice@test.com",
        "bob@test.com",
    }


def test_get_all_users_with_department_integration(seeded_gateway):
    """
    全ユーザー情報を部門情報を付与して取得のテスト
    """

    service = UserService(seeded_gateway)
    df = service.get_all_users_with_department()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert "department_name" in df.columns
    assert df.iloc[0]["department_name"] == "経営"
    assert df.iloc[1]["department_name"] == "総務"


def test_get_all_users_with_department_like_sql_integration(seeded_gateway):
    """
    全ユーザー情報を部門情報を付与してSQLフラットな結果を返すテスト
    """

    service = UserService(seeded_gateway)
    df = service.get_all_users_with_department_like_sql()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert "department_name" in df.columns
    assert df.iloc[0]["department_name"] == "経営"
    assert df.iloc[1]["department_name"] == "総務"


def test_get_one_user_by_id_integration(seeded_gateway):
    """
    指定IDのユーザー情報取得のテスト
    """

    service = UserService(seeded_gateway)
    df = service.get_one_user_by_id(1)

    assert len(df) == 1
    assert df.iloc[0]["name"] == "Alice"


def test_get_one_user_with_department_by_id_integration(seeded_gateway):
    """
    指定IDのユーザー情報を部門情報を付与して取得のテスト
    """

    service = UserService(seeded_gateway)
    df = service.get_one_user_with_department_by_id(1)

    assert len(df) == 1
    assert df.iloc[0]["name"] == "Alice"
    assert df.iloc[0]["email"] == "alice@test.com"
    assert df.iloc[0]["department_name"] == "経営"


def test_get_one_user_with_department_like_sql_by_id_integration(seeded_gateway):
    """
    指定IDのユーザー情報を部門情報を付与してSQLフラットな結果を返すテスト
    """

    service = UserService(seeded_gateway)
    df = service.get_one_user_with_department_like_sql_by_id(1)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert "department_name" in df.columns
    assert df.iloc[0]["department_name"] == "経営"


def test_get_all_departments_integration(seeded_gateway):
    """
    全部門情報取得のテスト
    """

    service = DepartmentService(seeded_gateway)
    df = service.get_all_departments()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert set(df["name"]) == {
        "経営",
        "総務",
    }


def test_get_one_department_by_id_integration(seeded_gateway):
    """
    指定IDの部門情報取得のテスト
    """

    service = DepartmentService(seeded_gateway)
    df = service.get_one_department_by_id(1)

    assert len(df) == 1
    assert df.iloc[0]["id"] == 1
    assert df.iloc[0]["name"] == "経営"
