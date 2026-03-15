import pandas as pd
import mysql.connector
import os

# --------------------------------------------------
# MySQLゲートウェイ層
# --------------------------------------------------
class MySQLGateway:
    """
    MySQLゲートウェイ層

    Methods
    -------
    execute_query
        SQL実行を行いデータフレームを返す
    """

    def __init__(self, config: dict) -> None:
        """
        コンストラクタ

        Parameters
        -------
        config
            MySQL接続情報の辞書オブジェクト

        Returns
        -------
        None
            なし
        """

        env_host = os.getenv("DB_HOST")

        if env_host:
            config["host"] = env_host

        self.config = config

    def execute_query(self, sql: str) -> pd.DataFrame:
        """
        SQL実行を行いデータフレームを返す

        Parameters
        -------
        sql
            実行するSQL文

        Returns
        -------
        pd.DataFrame
            MySQL取得データのデータフレーム
        """

        conn = mysql.connector.connect(**self.config)

        try:
            cursor = conn.cursor()
            cursor.execute(sql)

            rows = cursor.fetchall()
            columns = cursor.column_names

            df = pd.DataFrame(rows, columns=columns)
            return df

        finally:
            cursor.close()
            conn.close()