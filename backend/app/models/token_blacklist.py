from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from extensions import db

class TokenBlacklist(db.Model):
    __tablename__ = 'token_blacklist'

    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String(532), nullable=False, unique=True)
    blacklisted_on = Column(DateTime, default=datetime.utcnow)

    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.utcnow()

    def __repr__(self):
        return f"<TokenBlacklist(token={self.token})>"
    
  