from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from api.models import db

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "password": self.password
            # do not serialize the password, its a security breach
        }