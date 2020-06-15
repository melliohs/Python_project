import datetime
import sqlalchemy
from . import db_session
from .db_session import SqlAlchemyBase
from flask_login import UserMixin



class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    username = sqlalchemy.Column(sqlalchemy.String,  unique=True, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    image_file = sqlalchemy.Column(sqlalchemy.String, nullable=False, default='default.jpg')
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)


class Сharacter(SqlAlchemyBase):
    __tablename__ = 'character'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    role = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    biography = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    image = sqlalchemy.Column(sqlalchemy.String, nullable=False, default='default.jpg')
    abilities_1 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    abilities_2 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    abilities_3 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    abilities_4 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    abilities_description_1 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    abilities_description_2 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    abilities_description_3 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    abilities_description_4 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    abilities_image_1 = sqlalchemy.Column(sqlalchemy.String, nullable=False, default='default.jpg')
    abilities_image_2 = sqlalchemy.Column(sqlalchemy.String, nullable=False, default='default.jpg')
    abilities_image_3 = sqlalchemy.Column(sqlalchemy.String, nullable=False, default='default.jpg')
    abilities_image_4 = sqlalchemy.Column(sqlalchemy.String, nullable=False, default='default.jpg')
    abilities_video_1 = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    abilities_video_2 = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    abilities_video_3 = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    abilities_video_4 = sqlalchemy.Column(sqlalchemy.String, nullable=False)


class News(SqlAlchemyBase):
    __tablename__ = 'news'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    author = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    date = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    category = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    image = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    small_description = sqlalchemy.Column(sqlalchemy.String, nullable=True)

class Guides(SqlAlchemyBase):
    __tablename__ = 'guides'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    author = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    date = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    image = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    small_description = sqlalchemy.Column(sqlalchemy.String, nullable=True)




