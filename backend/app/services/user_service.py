from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate


users = []


def create_user(db: Session, user: UserCreate):
    new_user = User(
        name=user.name,
        mobile=user.mobile,
        shop_name=user.shop_name,
        language=user.language
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_users(db: Session):
    return db.query(User).all()