
from flask_security.forms import RegisterForm
from wtforms import StringField, TextAreaField, SubmitField
from flask_uploads import IMAGES
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, Email
from flask_wtf.file import FileField, FileAllowed
from flask_ckeditor import CKEditorField, CKEditor
from Portfolio import app

ckeditor = CKEditor(app)



class ExtendedRegisterForm(RegisterForm):
    first_name = StringField(validators=[InputRequired(
        'This is required'), Length(max=30, message="Name is Too long")])
    last_name = StringField(validators=[InputRequired(
        'This is required'), Length(max=30, message="Name is Too long")])


class ArticleForm(FlaskForm):
    title = StringField(validators=[Length(min=1, max=200)])
    description = TextAreaField(validators=[Length(min=10)])
    keywords = StringField(validators=[Length(max=100)])
    picture = FileField(validators=[FileAllowed(IMAGES, message='Images only')])
    img_alt = StringField()
    text = CKEditorField(validators=[Length(min=30)])
    submit = SubmitField('Post Blog')


class UpdateForm(FlaskForm):
    first_name = StringField(validators=[Length(min=2, max=20)])
    last_name = StringField(validators=[Length(min=2, max=20)])
    picture = FileField(validators=[FileAllowed(IMAGES, 'Images only')])
    bio = TextAreaField(validators=[Length(min=5)])
    url_to = StringField()
    
class PortfolioForm(FlaskForm):
    title = StringField()
    small = StringField()
    pic =  FileField(validators=[FileAllowed(IMAGES, 'Images only')])
    description = TextAreaField()
   
    link = StringField()
  
class CategoryForm(FlaskForm):
    name = StringField(validators=[Length(max=100)])
    submit = SubmitField('Save Changes')


class Reply(FlaskForm):
    email = StringField(validators=[Email()])
    head = StringField()
    body = TextAreaField()

