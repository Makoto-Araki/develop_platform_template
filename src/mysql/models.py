from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, declarative_base, mapped_column

Base = declarative_base()


# --------------------------------------------------
# Userモデル
# --------------------------------------------------
class User(Base):
    """
    Userモデル

    Columns
    -------
    id
        ID(主キー)
    name
        名前
    email
        メールアドレス
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255))
    department_id: Mapped[int] = mapped_column(Integer)


# --------------------------------------------------
# Departmentモデル
# --------------------------------------------------
class Department(Base):
    """
    Departmentモデル

    Columns
    -------
    id
        ID(主キー)
    name
        部門名
    """

    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
