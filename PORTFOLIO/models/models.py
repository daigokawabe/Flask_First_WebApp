from PORTFOLIO.database import db
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Login(db.Model):
    __tablename__ = 'login'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    users = db.relationship("User", uselist=False, backref="login")

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    login_id = db.Column(db.Integer, db.ForeignKey('login.id'), nullable=False)

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    photopost = db.Column(db.String(200), nullable=False)
    tagpost = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=func.now(), onupdate=func.now())
    login_id = db.Column(db.Integer, db.ForeignKey('login.id'), nullable=False)
    # parent = relationship("Parent", back_populates="children")


# class Parent(Base):
#     __tablename__ = 'parent'
#     id = Column(Integer, primary_key=True)
#     children = relationship("Child", back_populates="parent")

# class Child(Base):
#     __tablename__ = 'child'
#     id = Column(Integer, primary_key=True)
#     parent_id = Column(Integer, ForeignKey('parent.id'))
#     parent = relationship("Parent", back_populates="children")


