import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


# --------------------------------------------------
# MySQLゲートウェイ層
# --------------------------------------------------
class MySQLGateway:
    """
    MySQLゲートウェイ層

    Methods
    -------
    get_session
        MySQLセッションを返す
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

        self.engine = create_engine(
            f"mysql+mysqlconnector://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}",
            echo=False,
        )

        self.SessionLocal = sessionmaker(bind=self.engine)

    def get_session(self) -> Session:
        """
        MySQLセッションを返す

        Parameters
        -------
        none
            なし

        Returns
        -------
        Session
            MySQLセッション
        """

        return self.SessionLocal()
