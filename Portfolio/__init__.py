from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_uploads import UploadSet, configure_uploads, IMAGES
import os
from flask_mail import Mail
from flask_images import Images
from flask_discussion import Discussion
from Portfolio.config import Config, ConfigRemote


app = Flask(__name__)

Env = 'dev'

photos = UploadSet('photos', IMAGES)


if Env == 'dev':
    app.config.from_object(Config)
else:
    app.config.from_object(ConfigRemote)


configure_uploads(app, photos)


db = SQLAlchemy(app)
Migrate(app, db)
images = Images(app)
discussion = Discussion(app)
mail = Mail(app)

# db error


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


# blueprint views
from Portfolio.main.routes import main
from Portfolio.admin.routes import author
from Portfolio.errors.handlers import errors

app.register_blueprint(main)
app.register_blueprint(author)
app.register_blueprint(errors)
