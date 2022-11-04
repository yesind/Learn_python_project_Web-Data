import webapp.config
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class FindForm(FlaskForm):
    mark = SelectField('Марка', validators=[DataRequired()], choices=[], render_kw={"class": "form-control"})
    model = SelectField('Модель', validators=[DataRequired()],choices=[], render_kw={"class": "form-control"})
    year_from = StringField('Год с', validators=[DataRequired()],render_kw={"class": "form-control"})
    year_to = StringField('Год до', validators=[DataRequired()], render_kw={"class": "form-control"})
    fuel = SelectField('Вид топлива', validators=[DataRequired()], choices=['GASOLINE', 'DIESEL', 'ELECTRO'], render_kw={"class": "form-control"})
    gear_type = SelectField('Привод', validators=[DataRequired()], choices=['ALL_WHEEL_DRIVE','FORWARD_CONTROL', 'REAR_DRIVE'], render_kw={"class": "form-control"})
    owners_count_group = SelectField('Количество владельцев', validators=[DataRequired()], choices=['ONE', 'LESS_THAN_TWO'], render_kw={"class": "form-control"}) 
    submit = SubmitField('Поиск', render_kw={"class":"btn btn-primary"})