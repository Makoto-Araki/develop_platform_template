"""
service モジュールの単体テスト

get_users
1. 正常系テスト
    データフレームが返されることを確認
"""

import pandas as pd
from src.mysql.service import UserService

class MockGateway:
    """
    MySQLゲートウェイ層のモック

    Methods
    -------
    execute_query
        ゲートウェイ層の実行結果をモック
    """

    def execute_query(self, sql) -> pd.DataFrame:
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
            {"id": 1, "name": "Alice", "age": 30},
            {"id": 2, "name": "Bob", "age": 25}
        ])

# --------------------------------------------------
# MySQLサービス層テスト
# --------------------------------------------------

def test_get_users():
    gateway = MockGateway()
    service = UserService(gateway)
    df = service.get_users()

    assert len(df) == 2
    assert df.iloc[0]["name"] == "Alice"
    assert df.iloc[0]["age"] == 30