from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_uploads import UploadSet, configure_uploads, IMAGES
import os
from flask_images import Images
from flask_discussion import Discussion
from datetime import timedelta

 
app = Flask(__name__)

Env = 'prod'

photos = UploadSet('photos', IMAGES)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'static/images')

# flask uploads
app.config['UPLOADED_PHOTOS_DEST'] = STATIC_ROOT


if Env == 'dev':
    app.config.from_pyfile('config.cfg')
else:
    app.config.from_pyfile('prodconfig.cfg')
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

configure_uploads(app, photos)

db = SQLAlchemy(app)
Migrate(app, db)
images = Images(app)

app.config['DISCUSSION_DISQUS_SHORTNAME'] = 'maxmuhanda'
discussion = Discussion(app)


# db error
@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


# blueprint views
from Portfolio.main.routes import main
from Portfolio.admin.routes import  author

app.register_blueprint(main)
app.register_blueprint(author)
