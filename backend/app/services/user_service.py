from app.models.user import User
from app.schemas.user import UserCreate


users = []


def create_user(user: UserCreate):
    new_user = {
        "name": user.name,
        "mobile": user.mobile,
        "shop_name": user.shop_name,
        "language": user.language
    }

    users.append(new_user)
    return new_user


def get_users():
    return users