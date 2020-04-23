from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms.uset_form import UserForm
from forms.group_form import GroupForm
from forms.user_group_form import UserGroupForm
import plotly
import json
from flask_sqlalchemy import SQLAlchemy
import plotly.graph_objs as go
from sqlalchemy.sql import func


app = Flask(__name__)
app.secret_key = 'key'

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1998@localhost/postgres'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://lajdaazigpumhb:2c22c122aace9c7e284a54a8b9c5fce77d7b3e25e63b7f6be7d0f2ef93ce1fb0@ec2-174-129-253-27.compute-1.amazonaws.com:5432/df88p4jfspv874'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), nullable=False)

    User_User_Group = db.relationship("Group", secondary='user_group')


class Group(db.Model):
    __tablename__ = 'group'

    group_id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(20), nullable=False)
    group_topic = db.Column(db.String(20), nullable=False)

    Group_User_Group = db.relationship("User", secondary='user_group')
    Group_Group_Post = db.relationship("Post", secondary='group_post')



class User_Group(db.Model):
    __tablename__ = 'user_group'

    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.group_id'), primary_key=True)


class Post(db.Model):
    __tablename__ = 'post'

    post_id = db.Column(db.Integer, primary_key=True)
    post_content = db.Column(db.String(1000), nullable=False)
    post_hashtag = db.Column(db.String(20), nullable=False)

    Post_Group_Post = db.relationship("Group", secondary='group_post')
    notification = db.relationship("Notification")




class Group_Post(db.Model):
    __tablename__ = 'group_post'

    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'), primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.group_id'), primary_key=True)


class Notification(db.Model):
    __tablename__ = 'notification'

    notification_id = db.Column(db.Integer, primary_key=True)
    notification_time = db.Column(db.String(5), primary_key=True)
    notification_text = db.Column(db.String(100), primary_key=True)

    post_id = db.Column(db.Integer, db.ForeignKey("post.post_id"))