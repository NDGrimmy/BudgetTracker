from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
from utils.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(String, unique=True, index=True, nullable=False)
    date = Column(Date, nullable=False)
    name = Column(String, nullable=False)
    amount = Column(Numeric, nullable=False)
    category = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
