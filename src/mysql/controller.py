import pandas as pd

# --------------------------------------------------
# MySQLコントローラ層
# --------------------------------------------------
class UserController:
    """
    MySQLコントローラ層

    Methods
    -------
    get_users
        MySQL取得データをデータフレームで返す
    """

    def __init__(self, service) -> None:
        """
        コンストラクタ

        Parameters
        -------
        service
            MySQLサービス層のインスタンス

        Returns
        -------
        None
            なし
        """

        self.service = service

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

        df = self.service.get_users()

        return df