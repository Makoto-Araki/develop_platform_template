import pandas as pd


class UserController:
    """
    MySQLコントローラ層

    Methods
    -------
    get_all_users
        全ユーザー情報をデータフレームで返す
    get_one_user_by_id
        指定IDのユーザー情報を取得する
    get_all_users_with_department
        全ユーザー情報を部門情報を付与してデータフレームで返す
    get_all_users_with_department_like_sql
        全ユーザー情報を部門情報を付与してSQLフラットな結果を返す
    get_one_user_with_department_by_id
        指定IDのユーザー情報を部門情報を付与してデータフレームで返す
    get_one_user_with_department_like_sql_by_id
        指定IDのユーザー情報を部門情報を付与してSQLフラットな結果を返す
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

    def get_all_users(self) -> pd.DataFrame:
        """
        全ユーザー情報をデータフレームで返す

        Parameters
        -------
        None
            なし

        Returns
        -------
        pd.DataFrame
            MySQL取得データのデータフレーム
        """

        df = self.service.get_all_users()

        return df

    def get_one_user_by_id(self, id: int) -> pd.DataFrame:
        """
        指定IDのユーザー情報を取得する

        Parameters
        -------
        id
            検索対象ユーザーのID

        Returns
        -------
        pd.DataFrame
            MySQL取得データのデータフレーム
        """

        df = self.service.get_one_user_by_id(id)

        return df

    def get_all_users_with_department(self) -> pd.DataFrame:
        """
        全ユーザー情報を部門情報を付与してデータフレームで返す

        Parameters
        -------
        None
            なし

        Returns
        -------
        pd.DataFrame
            MySQL取得データのデータフレーム
        """

        df = self.service.get_all_users_with_department()

        return df

    def get_all_users_with_department_like_sql(self) -> pd.DataFrame:
        """
        全ユーザー情報を部門情報を付与してSQLフラットな結果を返す

        Parameters
        -------
        None
            なし

        Returns
        -------
        pd.DataFrame
            MySQL取得データのデータフレーム
        """

        df = self.service.get_all_users_with_department_like_sql()

        return df

    def get_one_user_with_department_by_id(self, id: int) -> pd.DataFrame:
        """
        指定IDのユーザー情報を部門情報を付与して取得する

        Parameters
        -------
        id
            検索対象ユーザーのID

        Returns
        -------
        pd.DataFrame
            MySQL取得データのデータフレーム
        """

        df = self.service.get_one_user_with_department_by_id(id)

        return df

    def get_one_user_with_department_like_sql_by_id(self, id: int) -> pd.DataFrame:
        """
        指定IDのユーザー情報を部門情報を付与してSQLフラットな結果を返す

        Parameters
        -------
        id
            検索対象ユーザーのID

        Returns
        -------
        pd.DataFrame
            MySQL取得データのデータフレーム
        """

        df = self.service.get_one_user_with_department_like_sql_by_id(id)

        return df


class DepartmentController:
    """
    MySQLコントローラ層

    Methods
    -------
    get_all_departments
        全部門情報をデータフレームで返す
    get_one_department_by_id
        指定IDの部門情報を取得する
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

    def get_all_departments(self) -> pd.DataFrame:
        """
        全部門情報をデータフレームで返す

        Parameters
        -------
        None
            なし

        Returns
        -------
        pd.DataFrame
            MySQL取得データのデータフレーム
        """

        df = self.service.get_all_departments()

        return df

    def get_one_department_by_id(self, id: int) -> pd.DataFrame:
        """
        指定IDの部門情報を取得する

        Parameters
        -------
        id
            検索対象部門のID

        Returns
        -------
        pd.DataFrame
            MySQL取得データのデータフレーム
        """

        df = self.service.get_one_department_by_id(id)

        return df
