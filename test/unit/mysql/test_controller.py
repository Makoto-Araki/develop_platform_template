"""
controller モジュールの単体テスト

get_users
1. 正常系テスト
    データフレームが返されることを確認
"""

import pandas as pd
from src.mysql.controller import UserController

class MockService:
    """
    MySQLサービス層のモック

    Methods
    -------
    get_users
        サービス層の実行結果をモック
    """

    def get_users(self):
        """
        SQL実行を行いデータフレームを返す

        Parameters
        -------
        sql
            実行するSQL文

        Returns
        -------
        pd.DataFrame
            モックされたデータフレーム
        """

        return pd.DataFrame([
            {"id": 1, "name": "Alice", "age": 30}
        ])

# --------------------------------------------------
# MySQLコントローラ層テスト
# --------------------------------------------------

def test_controller_get_users():
    service = MockService()
    controller = UserController(service)
    df = controller.get_users()

    assert len(df) == 1
    assert df.iloc[0]["name"] == "Alice"
    assert df.iloc[0]["age"] == 30