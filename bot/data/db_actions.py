from sqlalchemy import (
    insert,
    update,
    delete
)
from sqlalchemy.orm import Session

from bot.data.models import Role, User, Category, Image
from bot.data.db_init import engine


def add_user(tg_id: int):
    with Session(engine) as session:
        role = (
            session
                .query(Role)
                .where(Role.name == 'user')
                .one_or_none()
        )
        session.add(insert(User).values(tg_id=tg_id, role_id=role.role_id))
        session.commit()


def change_user_role(tg_id: int, role_name: str):
    with Session(engine) as session:
        role = (
            session
                .query(Role)
                .where(Role.name == role_name)
                .one_or_none()
        )
        session.add(update(User).where(User.tg_id == tg_id).values(role_id=role.role_id))


def delete_user(tg_id: int):
    with Session(engine) as session:
        session.add(delete(User).where(User.tg_id == tg_id))
        session.commit()


def get_categories() -> list[Category]:
    with Session(engine) as session:
        categories = (
            session
                .query(Category)
                .all()
        )
    return categories


def get_categories_names() -> list[str]:
    return [cat.name for cat in get_categories()]



def add_category(name: str):
    with Session(engine) as session:
        session.add(insert(Category).values(name=name))
        session.commit()


def delete_category(category_id: int):
    with Session(engine) as session:
        session.add(delete(Category).where(Category.category_id == category_id))
        session.commit()


def add_image(image: bytes, category_id: int):
    with Session(engine) as session:
        session.add(insert(Image).values(image=image, category_id=category_id))
        session.commit()
