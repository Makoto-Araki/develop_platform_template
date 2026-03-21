from unittest.mock import MagicMock

import pandas as pd

from src.mysql.controller import DepartmentController, UserController


def test_get_all_users():
    """
    全ユーザー情報取得のテスト
    """

    mock_service = MagicMock()

    expected = pd.DataFrame(
        [{"id": 1, "name": "Alice", "email": "alice@test.com", "department_id": 1}]
    )

    mock_service.get_all_users.return_value = expected

    controller = UserController(mock_service)

    df = controller.get_all_users()

    assert df.equals(expected)


def test_get_one_user_by_id():
    """
    指定IDのユーザー情報取得のテスト
    """

    mock_service = MagicMock()

    expected = pd.DataFrame(
        [{"id": 1, "name": "Alice", "email": "alice@test.com", "department_id": 1}]
    )

    mock_service.get_one_user_by_id.return_value = expected

    controller = UserController(mock_service)

    df = controller.get_one_user_by_id(1)

    assert df.equals(expected)


def test_get_all_departments():
    """
    全部門情報取得のテスト
    """

    mock_service = MagicMock()

    expected = pd.DataFrame(
        [
            {"id": 1, "name": "経営"},
            {"id": 2, "name": "総務"},
            {"id": 3, "name": "経理"},
            {"id": 4, "name": "営業"},
        ]
    )

    mock_service.get_all_departments.return_value = expected

    controller = DepartmentController(mock_service)

    df = controller.get_all_departments()

    assert df.equals(expected)


def test_get_one_department_by_id():
    """
    指定IDの部門情報取得のテスト
    """

    mock_service = MagicMock()

    expected = pd.DataFrame([{"id": 1, "name": "経営"}])

    mock_service.get_one_department_by_id.return_value = expected

    controller = DepartmentController(mock_service)

    df = controller.get_one_department_by_id(1)

    assert df.equals(expected)
