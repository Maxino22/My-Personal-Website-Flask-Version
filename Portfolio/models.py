from Portfolio import db, app
from datetime import datetime
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin
from datetime import datetime
from Portfolio.admin.forms import ExtendedRegisterForm
from sqlalchemy import event
from slugify import slugify


# Flask-Security Define models
roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(),
                                 db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(64), unique=True)
    profile_pic = db.Column(db.String(100), default='avatar.png')
    password = db.Column(db.String(255))
    bio = db.Column(db.Text)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime)

    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    blogs = db.relationship('Blog', backref='user', lazy=True)


class Blog(db.Model):
    __tablename__ = 'blog'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    title = db.Column(db.Text(), nullable=False)
    slug = db.Column(db.String(180), nullable=False)
    picture = db.Column(db.String(100))
    description = db.Column(db.String(200))
    keywords = db.Column(db.String(100))
    img_alt = db.Column(db.String(100))

    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    text = db.Column(db.Text, nullable=False)

    @staticmethod
    def generate_slug(target, value, oldvalue, initiator):
        if value and (not target.slug or value != oldvalue):
            target.slug = slugify(value)


db.event.listen(Blog.title, 'set', Blog.generate_slug, retval=False)


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)

    blogs = db.relationship('Blog', backref='category', lazy='dynamic')

    @staticmethod
    def generate_slug(target, value, oldvalue, initiator):
        if value and (not target.slug or value != oldvalue):
            target.slug = slugify(value)


db.event.listen(Category.name, 'set', Category.generate_slug, retval=False)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    small = db.Column(db.String(50))
    pic = db.Column(db.String(50))
    description = db.Column(db.Text())
    url_to = db.Column(db.String(100))
    link = db.Column(db.String(150))


# flask security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore,
                    confirm_register_form=ExtendedRegisterForm)
