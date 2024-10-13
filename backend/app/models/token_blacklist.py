from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class TokenBlacklist(Base):
    __tablename__ = 'token_blacklist'

    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String, nullable=False, unique=True)
    blacklisted_on = Column(DateTime, default=datetime.utcnow)

    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.utcnow()

    def __repr__(self):
        return f"<TokenBlacklist(token={self.token})>"