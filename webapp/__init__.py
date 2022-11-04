from crypt import methods
from flask import Flask, render_template, request, redirect, url_for, jsonify, json
from flask_sqlalchemy import SQLAlchemy  
from webapp.main import plot
from webapp.model import db, Mark, CarModel
from webapp.forms import FindForm

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route("/", methods=['POST','GET'])
    def index():
        form = FindForm()
        form.mark.choices = [(mark.id, mark.name) for mark in Mark.query.all()]
        if request.method == 'POST':
            mark = Mark.query.filter_by(id=form.mark.data).first()
            model = CarModel.query.filter_by(id=form.model.data).first()
            year_from = request.form['year_from']
            year_to = request.form['year_to']
            fuel = request.form['fuel']
            gear_type = request.form['gear_type']
            owners_count_group = request.form['owners_count_group']
            return redirect(url_for('plot_page', mark = mark, model = model, year_from=year_from, year_to = year_to, 
                                    fuel=fuel,gear_type=gear_type, owners_count_group=owners_count_group))
        else:
            return render_template('index.html', form=form)

    @app.route('/model/<get_model>')
    def modelbymark(get_model):
        model = CarModel.query.filter_by(mark_id=get_model).all()
        modelArray = []
        for car in model:
            modelObj = {}
            modelObj['id'] = car.id
            modelObj['name'] = car.name
            modelArray.append(modelObj)
        return jsonify({'modelmark' : modelArray})

    @app.route("/plot_page", methods=['POST','GET'])
    def plot_page():    
        url_plot=plot(mark = request.args.get('mark'), model = request.args.get('model'),
                    year_from=request.args.get('year_from'), year_to = request.args.get('year_to'), 
                    fuel = request.args.get('fuel'), gear_type = request.args.get('gear_type'),
                    owners_count_group = request.args.get('owners_count_group'))
        print(type(url_plot))        
        return render_template('plot_page.html', 
                    mark = request.args.get('mark'), model = request.args.get('model'),
                    year_from=request.args.get('year_from'), year_to = request.args.get('year_to'), 
                    fuel = request.args.get('fuel'), gear_type = request.args.get('gear_type'),
                    wners_count_group = request.args.get('owners_count_group'), url_plot=url_plot)
    
    return app

if __name__ == "__main__":
    app.run(debug=True)