from flask import Flask,send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_uploads import UploadSet, configure_uploads, IMAGES
import os
from flask_sitemap import Sitemap
from flask_mail import Mail
from flask_images import Images
from flask_discussion import  Discussion
from Portfolio.config import Config, ConfigRemote


app = Flask(__name__, static_folder='static')

Env = 'prod'
photos = UploadSet('photos', IMAGES)


if Env == 'dev':
    app.config.from_object(Config)
else:
    app.config.from_object(ConfigRemote)


configure_uploads(app, photos)

db = SQLAlchemy(app)
Migrate(app, db)
images = Images(app)
mail = Mail(app)
ext = Sitemap(app)
discussion = Discussion(app)

# db error


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()

# robot
@app.route('/robots.txt')
def static_root():
    return send_from_directory('static', 'robots.txt')

# blueprint views
from Portfolio.main.routes import main
from Portfolio.admin.routes import author
from Portfolio.errors.handlers import errors

app.register_blueprint(main)
app.register_blueprint(author)
app.register_blueprint(errors)
