import pandas as pd
from sqlalchemy import select

from mysql.models import Department, User


class UserService:
    """
    MySQLサービス層

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
        指定IDのユーザー情報を部門情報を付与して取得する
    get_one_user_with_department_like_sql_by_id
        指定IDのユーザー情報を部門情報を付与してSQLフラットな結果を返す
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

        session = self.gateway.get_session()

        try:
            stmt = select(User)
            result = session.execute(stmt)
            users = result.scalars().all()

            # DataFrame変換
            data = [
                {
                    "id": u.id,
                    "name": u.name,
                    "email": u.email,
                    "department_id": u.department_id,
                }
                for u in users
            ]

            df = pd.DataFrame(data)
            return df

        finally:
            session.close()

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

        session = self.gateway.get_session()

        try:
            stmt = select(User).where(User.id == id)
            result = session.execute(stmt)
            users = result.scalars().all()

            # DataFrame変換
            data = [
                {
                    "id": u.id,
                    "name": u.name,
                    "email": u.email,
                    "department_id": u.department_id,
                }
                for u in users
            ]

            df = pd.DataFrame(data)
            return df

        finally:
            session.close()

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

        session = self.gateway.get_session()

        try:
            # INNER JOIN
            stmt = select(User, Department).join(
                Department, User.department_id == Department.id
            )

            # LEFT JOIN
            # stmt = select(User, Department).outerjoin(
            #    Department, User.department_id == Department.id
            # )

            result = session.execute(stmt).all()

            # DataFrame変換
            data = [
                {
                    "id": u.id,
                    "name": u.name,
                    "email": u.email,
                    "department_name": d.name,
                }
                for u, d in result
            ]

            df = pd.DataFrame(data)
            return df

        finally:
            session.close()

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

        session = self.gateway.get_session()

        try:
            # INNER JOIN
            stmt = select(
                User.id, User.name, User.email, Department.name.label("department_name")
            ).join(Department, User.department_id == Department.id)

            # LEFT JOIN
            # stmt = select(
            #    User.id, User.name, User.email, Department.name.label("deartment_name")
            # ).outerjoin(Department, User.department_id == Department.id)

            result = session.execute(stmt).all()

            df = pd.DataFrame(
                result, columns=["id", "name", "email", "department_name"]
            )
            return df

        finally:
            session.close()

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

        session = self.gateway.get_session()

        try:
            # INNER JOIN
            stmt = (
                select(User, Department)
                .join(Department, User.department_id == Department.id)
                .where(User.id == id)
            )

            # LEFT JOIN
            # stmt = select(User, Department).outerjoin(
            #    Department, User.department_id == Department.id
            # ).where(User.id == id)

            result = session.execute(stmt).all()

            # DataFrame変換
            data = [
                {
                    "id": u.id,
                    "name": u.name,
                    "email": u.email,
                    "department_name": d.name,
                }
                for u, d in result
            ]

            df = pd.DataFrame(data)
            return df

        finally:
            session.close()

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

        session = self.gateway.get_session()

        try:
            # INNER JOIN
            stmt = (
                select(
                    User.id,
                    User.name,
                    User.email,
                    Department.name.label("department_name"),
                )
                .join(Department, User.department_id == Department.id)
                .where(User.id == id)
            )

            # LEFT JOIN
            # stmt = select(
            #    User.id, User.name, User.email, Department.name.label("deartment_name")
            # )
            # .outerjoin(Department, User.department_id == Department.id)
            # .where(User.id == id)

            result = session.execute(stmt).all()

            df = pd.DataFrame(
                result, columns=["id", "name", "email", "department_name"]
            )
            return df

        finally:
            session.close()


class DepartmentService:
    """
    MySQLサービス層

    Methods
    -------
    get_all_departments
        全部門情報をデータフレームで返す
    get_one_department_by_id
        指定IDの部門情報を取得する
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

        session = self.gateway.get_session()

        try:
            stmt = select(Department)
            result = session.execute(stmt)
            departments = result.scalars().all()

            # DataFrame変換
            data = [
                {
                    "id": u.id,
                    "name": u.name,
                }
                for u in departments
            ]

            df = pd.DataFrame(data)
            return df

        finally:
            session.close()

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

        session = self.gateway.get_session()

        try:
            stmt = select(Department).where(Department.id == id)
            result = session.execute(stmt)
            departments = result.scalars().all()

            # DataFrame変換
            data = [
                {
                    "id": u.id,
                    "name": u.name,
                }
                for u in departments
            ]

            df = pd.DataFrame(data)
            return df

        finally:
            session.close()
