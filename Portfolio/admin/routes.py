from flask import render_template, send_file, Blueprint, redirect, url_for, flash, request, send_from_directory, abort, current_app, session
from Portfolio import db, photos, app, mail
from Portfolio.models import User, Blog, Category, Contact, Portfolio
from flask_security import login_required, logout_user, current_user
from Portfolio.admin.forms import ArticleForm, CategoryForm, UpdateForm, Reply, PortfolioForm
from Portfolio.picture_handler import add_profile_pic, add_port_pic
from flask_mail import Message
import os
import uuid

save = 1

author = Blueprint('author', __name__)


@author.route('/admin/', methods=['POST', 'GET'])
@login_required
def admin():
    blogs = Blog.query.all()
    messages = Contact.query.all()
    categories = Category.query.all()
    users = User.query.all()

    form = PortfolioForm()

    if form.validate_on_submit():
        first_name = str(uuid.uuid4())
        pic = add_port_pic(form.pic.data, first_name)

        new_port = Portfolio(title=form.title.data, small=form.small.data,
                             pic=pic, description=form.description.data, link=form.link.data)
        print(form.title.data)
        db.session.add(new_port)
        db.session.commit()
        flash("Portfolio Added", 'success')
        return redirect(url_for('author.admin'))

    return render_template('admin/index.html', admin=True, form=form, users=users, categories=categories, blogs=blogs, messages=messages)


@author.route('/admin/add', methods=['GET', 'POST'])
@login_required
def add_post():
    categories = Category.query.all()

    if request.method == 'POST' and 'thefile' in request.files:
        global save
        save = photos.url(photos.save(request.files['thefile']))
        # return '<h1>'+photos.path(image_filename)+'</h1>'

    # form
    form = ArticleForm()
    if form.validate_on_submit():
        image_url = photos.url(photos.save(form.picture.data))

        new_blog = Blog(title=form.title.data,
                        description=form.description.data,
                        keywords=form.keywords.data,
                        img_alt=form.img_alt.data,
                        category_id=int(request.form['category_id']),
                        picture=image_url,
                        user_id=current_user.id,
                        text=form.text.data)
        db.session.add(new_blog)
        db.session.commit()
        flash("Blog Posted", 'success')
        return redirect(url_for('author.posts'))

    return render_template('admin/add_post.html', form=form, categories=categories, save=save)

# UPDATE BLOG


@author.route('/admin/<int:blog_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(blog_id):
    categories = Category.query.all()

    blog = Blog.query.get_or_404(blog_id)
    if blog.user != current_user:
        abort(403)

    form = ArticleForm()

    if form.validate_on_submit():
        blog.title = form.title.data
        blog.text = form.text.data
        blog.user_id = current_user.id
        blog.description = form.description.data
        blog.keywords = form.keywords.data
        blog.img_alt = form.img_alt
        db.session.commit()
        flash("Post has been updated", 'success')
        return redirect(url_for('author.posts', blog_id=blog.id))

    elif request.method == 'GET':
        form.title.data = blog.title
        form.description.data = blog.description
        form.keywords.data = blog.keywords
        form.text.data = blog.text
        current_user.id = blog.user_id

    return render_template('admin/add_post.html', form=form, categories=categories, blog=blog, save=save)

# DELETE BLOG


@author.route('/admin/<int:blog_id>/delete', methods=['POST'])
@login_required
def delete_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    db.session.delete(blog)
    db.session.commit()
    flash('Deleted Successfully', 'success')
    return redirect(url_for('author.admin'))


# DELETE USER
@author.route('/admin/<int:user_id>/delete_user', methods=['POST'])
@login_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('Deleted Successfully', 'success')
    return redirect(url_for('author.admin'))


#  CATEGORIES
@author.route('/admin/categories', methods=['GET', 'POST'])
@login_required
def categories():
    categories = Category.query.all()
    form = CategoryForm()

    if form.validate_on_submit():
        new_cat = Category(name=form.name.data)
        db.session.add(new_cat)
        db.session.commit()
        return redirect(url_for('author.categories'))

    return render_template('admin/categories.html', admin=True, form=form, categories=categories)

# SETTINGS


@author.route('/admin/settings')
@login_required
def settings():
    return render_template('admin/settings.html', admin=True)


#
@author.route('/admin/users')
@login_required
def users():
    page = request.args.get('page', type=int)
    users = User.query.order_by(
        User.confirmed_at.desc()).paginate(page=page, per_page=5)

    return render_template('admin/users.html', admin=True, users=users)


@author.route('/admin/posts')
@login_required
def posts():
    page = request.args.get('page', type=int)
    blogs = Blog.query.order_by(
        Blog.date.desc()).paginate(page=page, per_page=10)

    return render_template('admin/posts.html', admin=True, blogs=blogs)

# update profile


@author.route('/admin/<int:current_user_id>/profile', methods=['GET', 'POST'])
@login_required
def profile(current_user_id):
    user = User.query.get_or_404(current_user_id)
    form = UpdateForm()

    if form.validate_on_submit():
        if form.picture.data:
            first_name = current_user.first_name
            pic = add_profile_pic(form.picture.data, first_name)
            current_user.profile_pic = pic

        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.bio = form.bio.data
        db.session.commit()
        flash('user updated', 'success')
        return redirect(url_for('author.profile', current_user_id=current_user.id))

    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.bio.data = current_user.bio

    return render_template('admin/profile.html', admin=True, form=form)


@author.route('/admin/details')
@login_required
def details():
    return render_template('admin/details.html', admin=True)

# message


@author.route('/admin/<int:message_id>/massage', methods=['POST', 'GET'])
@login_required
def message(message_id):
    message = Contact.query.filter_by(id=message_id).first()
    form = Reply()
    if request.method == 'POST':
        msg = Message(form.head.data, recipients=[form.email.data])
        msg.body = form.body.data
        mail.send(msg)
        flash('You have Replied', 'success')
        return redirect(url_for('author.admin'))

    return render_template('admin/message.html', admin=True, message=message, form=form)


# Delete Message
@author.route('/admin/<int:message_id>/delete_msg', methods=['POST'])
@login_required
def delete_msg(message_id):
    message = Contact.query.filter_by(id=message_id).first()
    db.session.delete(message)
    db.session.commit()
    flash('Message Deleted !', 'success')
    return redirect(url_for('author.admin'))
