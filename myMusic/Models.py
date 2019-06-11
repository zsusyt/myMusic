from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, SmallInteger, String, Date, DateTime, Float, Boolean, Text, LargeBinary)
from sqlalchemy.orm import relationship
from scrapy.utils.project import get_project_settings

DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class Album(DeclarativeBase):
    __tablename__ = "album"

    id = Column(Integer, primary_key=True)
    imgSrc = Column('imgSrc', Text())
    titleCn = Column('titleCn', Text())
    titleEn = Column('titleEn', Text())
    songs = relationship('Song', backref='album')


class Song(DeclarativeBase):
    __tablename__ = "song"

    id = Column(Integer, primary_key=True)
    highUrl = Column('highUrl', Text())
    lowUrl = Column('lowUrl', Text())
    subTitle = Column('subTitle', Text())
    serial = Column('serial', Integer)
    album_id = Column(Integer, ForeignKey('album.id'))
    # album = relationship('Album')

