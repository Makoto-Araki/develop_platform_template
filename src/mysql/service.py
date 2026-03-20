import pandas as pd


# --------------------------------------------------
# MySQLサービス層
# --------------------------------------------------
class UserService:
    """
    MySQLサービス層

    Methods
    -------
    get_users
        MySQL取得データをデータフレームで返す
    """

    def __init__(self, gateway) -> None:
        """
        コンストラクタ

        Parameters
        -------
        gateway
            MySQLゲートウェイ層のインスタンス

        Returns
        -------
        None
            なし
        """

        self.gateway = gateway

    def get_users(self) -> pd.DataFrame:
        """
        MySQL取得データをデータフレームで返す

        Parameters
        -------
        None
            なし

        Returns
        -------
        pd.DataFrame
            MySQL取得データのデータフレーム
        """

        sql = """
        SELECT
            id,
            name,
            age
        FROM
            users
        """

        df = self.gateway.execute_query(sql)

        return df
