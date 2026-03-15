import pytest
import os
from src.mysql.gateway import MySQLGateway 

class TestUserIntegration:
    """MySQLとの疎通を含む結合テスト"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """テスト前後の準備"""
        self.db_config = {
            "host": "host.docker.internal",
            "user": "test_user",
            "password": "test_password",
            "database": "test_db"
        }
        self.gateway = MySQLGateway(self.db_config)

    def test_get_user_by_id(self):
        sql = "SELECT * FROM users ;"
        df = self.gateway.execute_query(sql)
        assert len(df.columns) == 4
