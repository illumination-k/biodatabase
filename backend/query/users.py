from sqlalchemy.orm import Session
import models
import bcrypt
from typing import Optional, Literal


ENCODE = "utf-8"


def get_user_by_username(db: Session, username: str) -> Optional[models.User]:
    try:
        user = db.query(models.User).filter(models.User.username == username).first()
    except:
        db.rollback()
        return None
    return user


KEY_LITERAL = Literal["username", "email"]


def get_user(db: Session, key: KEY_LITERAL, query: str) -> Optional[models.User]:
    try:
        if key == "username":
            user = db.query(models.User).filter(models.User.username == query).first()
        elif key == "email":
            user = db.query(models.User).filter(models.User.email == query).first()
        else:
            raise ValueError("get invalid key")
    except:
        db.rollback()
        return None
    return user


def create_user(db: Session, user: models.User) -> Optional[models.User]:
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except:
        db.rollback()
        return None


def check_password(db: Session, username: str, password: str) -> bool:
    db_user = get_user_by_username(db, username)
    return bcrypt.checkpw(password.encode(ENCODE), db_user.password.encode(ENCODE))
