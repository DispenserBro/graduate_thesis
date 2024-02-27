from sqlalchemy.orm import relationship, DeclarativeBase
from sqlalchemy import (
    Column,
    Integer,
    String,
    LargeBinary,
    ForeignKey
)


class Base(DeclarativeBase):
    pass


class Role(Base):
    __tablename__ = 'roles'
    
    role_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    users = relationship("User", backref="role", cascade="all, delete")


class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True)
    tg_id = Column(Integer, unique=True, nullable=False)
    role_id = Column(Integer, ForeignKey("roles.role_id"))


class Category(Base):
    __tablename__ = 'categories'
    
    category_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    images = relationship("Image", backref="category", cascade="all, delete")


class Image(Base):
    __tablename__ = 'images'
    
    image_id = Column(Integer, primary_key=True)
    image = Column(LargeBinary, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.category_id"))
