import webapp.config
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class FindForm(FlaskForm):
    mark = SelectField('Марка', validators=[DataRequired()], choices=[], render_kw={"class": "form-control"})
    model = SelectField('Модель', validators=[DataRequired()],choices=[], render_kw={"class": "form-control"})
    year_from = StringField('Год с', validators=[DataRequired()],render_kw={"class": "form-control"})
    year_to = StringField('Год до', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Поиск', render_kw={"class":"btn btn-primary"})