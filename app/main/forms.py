from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import Item


class ItemForm(FlaskForm):
    name = TextAreaField(
        "Name of the item", validators=[DataRequired(), Length(min=1, max=140)]
    )
    description = TextAreaField(
        "Description of the item", validators=[DataRequired(), Length(min=1, max=140)]
    )
    submit = SubmitField("Submit")

