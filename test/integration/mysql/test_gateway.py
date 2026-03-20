"""
gateway モジュールの結合テスト

execute_query
1. 正常系テスト
    データフレームが返されることを確認
"""

import pytest

from src.mysql.gateway import MySQLGateway


class TestUserIntegration:
    """
    MySQL疎通確認を行う結合テストクラス

    Methods
    -------
    setup
        MySQL接続情報を引数にセットしてインスタンス準備
    test_execute_query
        MySQL疎通確認
    """

    @pytest.fixture(autouse=True)
    def setup(self) -> None:
        """
        SQL実行を行いデータフレームを返す

        Parameters
        -------
        None
            なし

        Returns
        -------
        None
            なし
        """

        self.db_config = {
            "host": "host.docker.internal",
            "user": "test_user",
            "password": "test_password",
            "database": "test_db",
        }

        self.gateway = MySQLGateway(self.db_config)

    def test_execute_query(self) -> None:
        """
        SQL実行を行いデータフレームを返す

        Parameters
        -------
        None
            なし

        Returns
        -------
        None
            なし
        """

        sql = "SELECT * FROM users ;"
        df = self.gateway.execute_query(sql)

        assert len(df.columns) == 4
        assert len(df) == 3
