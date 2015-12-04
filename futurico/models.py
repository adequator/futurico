from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Text)


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    text = Column(Text)
    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship('User', backref="posts")
    counter = relationship('Counter', uselist=False, backref="post")


class Counter(Base):
    __tablename__ = 'counters'
    post_id = Column(Integer, ForeignKey('posts.id'), primary_key=True)
    views = Column(Integer)

