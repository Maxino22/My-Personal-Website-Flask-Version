from flask import render_template, send_file, Blueprint, redirect, url_for, flash, request, send_from_directory, abort, current_app
from Portfolio import db, ext
from Portfolio.models import User, Blog, Category, Contact, Portfolio
from Portfolio.main.forms import ContactForm
import os


main = Blueprint('main', __name__)



@main.route('/', methods=['GET', 'POST'])
def index():
    user = User.query.filter_by(first_name='Maxwell').first()
    return render_template('index.html', user=user)

@ext.register_generator
def index():
    yield 'main.index', {},"2021-08-19T11:13:12+00:00", 'always', 0.7

@main.route('/blog')
def blog():
    page = request.args.get('page', type=int)
    blogs = Blog.query.order_by(
        Blog.date.desc()).paginate(page=page, per_page=6)
    cats = Category.query.all()
    return render_template('blog.html', blogs=blogs, cats=cats)

@ext.register_generator
def blog():
    yield 'main.blog', {}, "2021-08-19T11:13:12+00:00", 'always', 0.8

@main.route('/blog/<string:slug>')
def post(slug):
    blogs = Blog.query.order_by(Blog.date.desc()).limit(5).all()
    post = Blog.query.filter_by(slug=slug).first()
    cats = Category.query.all()
    return render_template('post.html', cats=cats,post=post, blogs=blogs)

@ext.register_generator
def post():
    yield 'main.post' ,{'slug':'post.slug'}, "2021-08-19T11:13:12+00:00", 'always', 0.7


# Category route
@main.route('/category/<string:slug>')
def category(slug):
    page = request.args.get('page', type=int)
    blogs = Blog.query.order_by(Blog.date.desc()).paginate(page=page, per_page=8)
    category = Category.query.filter_by(slug=slug).first()
    posts = Blog.query.all()
    cats = Category.query.all()
    return render_template('category.html', category=category, cats=cats, blogs=blogs, posts=posts)

@ext.register_generator
def category():
    yield 'main.category' ,{'slug':'cat.slug'}, "2021-08-19T11:13:12+00:00", 'always', 0.7
    

@main.route('/work')
def work():
    portfolio = Portfolio.query.all()
    return render_template('work.html', portfolio=portfolio)

@ext.register_generator
def work():
    yield 'main.work', {}, "2021-08-19T11:13:12+00:00", 'always', 0.5

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        new_message = Contact(name=form.name.data,
                               email=form.email.data, message=form.message.data)
        db.session.add(new_message)
        db.session.commit()
        flash('Message Has been recieved I will get Back to you', "success")
        return redirect(url_for('main.contact'))
    

    return render_template('contact.html', form=form)

@ext.register_generator
def contact():
    yield 'main.contact', {}, "2021-08-19T11:13:12+00:00", 'always', 0.5

@main.route('/download')
def download():
    path = os.path.join(current_app.root_path, "static/document/mypdf.pdf")
    return send_file(path, as_attachment=True)


@ext.register_generator
def download():
    yield 'main.download', {}, "2021-08-19T11:13:12+00:00", 'always', 0.5
