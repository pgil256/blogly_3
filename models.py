"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    __table__ = 'users'

    id == db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable = False)
    last_name = db.Column(db.Text, nullable = False)
    image_url = db.Column(db.Text, nullable=False)

    user_posts = db.relatiobship("Post", backref = 'user', cascade = 'all')

    @property 
    def full_name(self):

        return f'{self.first_name} {self.last_name}'

class Post(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_keys = True)
    title = db.Column(db.Text, nullable = False)
    content = db.Column(db.Text, nullable = False)

class PostTag(db.Model):

    __tablename__ = "posts_tags"

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)


class Tag(db.Model):

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False, unique=True)

    posts = db.relationship(
        'Post',
        secondary="posts_tags",
        backref="tags",
    )


def connect_db(app):
    db.app = app
    db.init_app(app)