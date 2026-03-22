from unittest.mock import MagicMock

import pandas as pd

from src.mysql.service import DepartmentService, UserService


class DummyUser:
    """
    ダミー情報のクラス定義
    """

    def __init__(self, id, name, email, department_id):
        self.id = id
        self.name = name
        self.email = email
        self.department_id = department_id


class DummyDepartment:
    """
    ダミー情報のクラス定義
    """

    def __init__(self, id, name):
        self.id = id
        self.name = name


def create_mock_user_gateway(users):
    """
    モック作成
    """

    session = MagicMock()
    result = MagicMock()
    result.scalars.return_value.all.return_value = users
    session.execute.return_value = result
    gateway = MagicMock()
    gateway.get_session.return_value = session

    return gateway, session


def test_get_all_users():
    """
    全ユーザー情報取得のテスト
    """

    users = [
        DummyUser(1, "Alice", "alice@test.com", 1),
        DummyUser(2, "Bob", "bob@test.com", 2),
    ]

    gateway, session = create_mock_user_gateway(users)
    service = UserService(gateway)
    df = service.get_all_users()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert list(df.columns) == ["id", "name", "email", "department_id"]
    assert df.iloc[0]["email"] == "alice@test.com"

    session.close.assert_called_once()


def test_get_one_user_by_id():
    """
    指定IDのユーザー情報取得のテスト
    """

    users = [
        DummyUser(1, "Alice", "alice@test.com", 1),
    ]

    gateway, session = create_mock_user_gateway(users)
    service = UserService(gateway)
    df = service.get_one_user_by_id(1)

    assert len(df) == 1
    assert df.iloc[0]["id"] == 1
    assert df.iloc[0]["name"] == "Alice"

    session.close.assert_called_once()


def create_mock_department_gateway(departments):
    """
    モック作成
    """

    session = MagicMock()
    result = MagicMock()
    result.scalars.return_value.all.return_value = departments
    session.execute.return_value = result
    gateway = MagicMock()
    gateway.get_session.return_value = session

    return gateway, session


def test_get_all_departments():
    """
    全部門情報取得のテスト
    """

    departments = [
        DummyDepartment(1, "経営"),
        DummyDepartment(2, "総務"),
    ]

    gateway, session = create_mock_department_gateway(departments)
    service = DepartmentService(gateway)
    df = service.get_all_departments()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert list(df.columns) == ["id", "name"]
    assert df.iloc[0]["name"] == "経営"

    session.close.assert_called_once()


def test_get_one_department_by_id():
    """
    指定IDの部門情報取得のテスト
    """

    departments = [
        DummyDepartment(1, "経営"),
    ]

    gateway, session = create_mock_department_gateway(departments)
    service = DepartmentService(gateway)
    df = service.get_one_department_by_id(1)

    assert len(df) == 1
    assert df.iloc[0]["id"] == 1
    assert df.iloc[0]["name"] == "経営"

    session.close.assert_called_once()


def create_mock_user_with_department_gateway(rows):
    """
    モック作成
    """

    session = MagicMock()
    result = MagicMock()
    result.all.return_value = rows
    session.execute.return_value = result
    gateway = MagicMock()
    gateway.get_session.return_value = session

    return gateway, session


def test_get_all_users_with_department():
    """
    全ユーザー情報を部門情報を付与して取得のテスト
    """

    users_with_department = [
        (
            DummyUser(1, "Alice", "alice@test.com", 1),
            DummyDepartment(1, "経営"),
        ),
        (
            DummyUser(2, "Bob", "bob@test.com", 1),
            DummyDepartment(2, "総務"),
        ),
    ]

    gateway, session = create_mock_user_with_department_gateway(users_with_department)
    service = UserService(gateway)
    df = service.get_all_users_with_department()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert list(df.columns) == ["id", "name", "email", "department_name"]
    assert df.iloc[0]["email"] == "alice@test.com"

    session.close.assert_called_once()


def test_get_all_users_with_department_like_sql():
    """
    全ユーザー情報を部門情報を付与してSQLフラットな結果を返すテスト
    """

    users_with_department = [
        (1, "Alice", "alice@test.com", "経営"),
        (2, "Bob", "bob@test.com", "総務"),
    ]

    gateway, session = create_mock_user_with_department_gateway(users_with_department)
    service = UserService(gateway)
    df = service.get_all_users_with_department_like_sql()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert list(df.columns) == ["id", "name", "email", "department_name"]
    assert df.iloc[0]["email"] == "alice@test.com"

    session.close.assert_called_once()


def test_get_one_user_with_department_by_id():
    """
    指定IDのユーザー情報を部門情報を付与して取得のテスト
    """

    users_with_department = [
        (
            DummyUser(1, "Alice", "alice@test.com", 1),
            DummyDepartment(1, "経営"),
        ),
    ]

    gateway, session = create_mock_user_with_department_gateway(users_with_department)
    service = UserService(gateway)
    df = service.get_one_user_with_department_by_id(1)

    assert len(df) == 1
    assert df.iloc[0]["id"] == 1
    assert df.iloc[0]["name"] == "Alice"

    session.close.assert_called_once()


def test_get_one_user_with_department_by_id_like_sql():
    """
    指定IDのユーザー情報を部門情報を付与してSQLフラットな結果を返すテスト
    """

    users_with_department = [
        (1, "Alice", "alice@test.com", "経営"),
    ]

    gateway, session = create_mock_user_with_department_gateway(users_with_department)
    service = UserService(gateway)
    df = service.get_one_user_with_department_like_sql_by_id(1)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert list(df.columns) == ["id", "name", "email", "department_name"]
    assert df.iloc[0]["id"] == 1
    assert df.iloc[0]["department_name"] == "経営"

    session.close.assert_called_once()
