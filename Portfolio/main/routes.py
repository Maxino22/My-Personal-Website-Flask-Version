from flask import render_template, send_file, Blueprint, redirect, url_for, flash, request, send_from_directory, abort, current_app
from Portfolio import db
from Portfolio.models import User, Blog, Category, Contact, Portfolio
from Portfolio.main.forms import ContactForm
import os


main = Blueprint('main', __name__)



@main.route('/', methods=['GET', 'POST'])
def index():
    user = User.query.filter_by(first_name='Maxwell').first()

    page = request.args.get('page', type=int)
    blogs = Blog.query.order_by(
        Blog.date.desc()).paginate(page=page, per_page=6)
    cats = Category.query.all()

    portfolio = Portfolio.query.all()

    form = ContactForm()

    if form.validate_on_submit():
        new_message = Contact(name=form.name.data,
                               email=form.email.data, message=form.message.data)
        db.session.add(new_message)
        db.session.commit()
        flash('Message Has been recieved I will get Back to you', "success")
        return redirect(url_for('main.index'))

    return render_template('index.html', user=user , blogs=blogs, cats=cats, portfolio=portfolio, form=form)


@main.route('/blog/<string:slug>')
def post(slug):
    blogs = Blog.query.order_by(Blog.date.desc()).limit(5).all()
    post = Blog.query.filter_by(slug=slug).first()
    cats = Category.query.all()
    return render_template('post.html', cats=cats,post=post, blogs=blogs)




# Category route
@main.route('/category/<string:slug>')
def category(slug):
    page = request.args.get('page', type=int)
    blogs = Blog.query.order_by(Blog.date.desc()).paginate(page=page, per_page=8)
    category = Category.query.filter_by(slug=slug).first()
    posts = Blog.query.all()
    cats = Category.query.all()
    return render_template('category.html', category=category, cats=cats, blogs=blogs, posts=posts)

@main.route('/download')
def download():
    path = os.path.join(current_app.root_path, "static/document/mypdf.pdf")
    return send_file(path, as_attachment=True)

# HTML SITEMAP
@main.route('/sitemap')
def sitemap():
    posts = Blog.query.all()
    cats = Category.query.all()
    return render_template('sitemap.html', posts=posts, cats=cats)

