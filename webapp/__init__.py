from crypt import methods
from flask import Flask, render_template, request, redirect, url_for, jsonify, json
from flask_sqlalchemy import SQLAlchemy  
from webapp.main import plot
from webapp.model import db, Mark, Model
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
            model = Model.query.filter_by(id=form.model.data).first()
            year_from = request.form['year_from']
            year_to = request.form['year_to']
            print(mark.name, model.name)
            #return f'<h1>Mark: {mark.name}, Car_Model: {model.name} </h1>'
            return redirect(url_for('plot_page', mark = mark, model = model, year_from=year_from, year_to = year_to))
        else:
            #marks = ['AUDI', "BMW", "MERCEDES", "LAND_ROVER"]
        # models = ['A1', 'A2', 'A3', 'A4', 'A4_ALLROAD', 'A5', 'A6', 'A7', 'A8', 'ALLROAD', 
            #    'E_TRON', 'Q2', 'Q3', 'Q3_SPORTBACK', 'Q4', 'Q4_SPORTBACK', 'Q5', 
            #    'Q5_E_TRON', 'Q5_SPORTBACK', 'Q7', 'Q8', 'R8', 'RS3', 'RS4', 'RS5', 'RS6', 
        #     'RS7', 'RSQ3', 'RS_E_TRON_GT', 'RS_Q3_SPORTBACK', 'RS_Q8', 'S1', 'S2', 'S3', 
            #    'S4', 'S5', 'S6', 'S7', 'S8', 'SQ2', 'SQ5', 'SQ5_SPORTBACK', 'SQ7', 'SQ8', 'TT', 'TTS', 'TT_RS']
            return render_template('index.html', form=form)

    @app.route('/model/<get_model>')
    def modelbymark(get_model):
        model = Model.query.filter_by(mark_id=get_model).all()
        modelArray = []
        for car in model:
            modelObj = {}
            modelObj['id'] = car.id
            modelObj['name'] = car.name
            modelArray.append(modelObj)
        return jsonify({'modelmark' : modelArray})


    @app.route("/plot_page", methods=['POST','GET'])
    def plot_page():
    
        from webapp.main import plot
    
        url_plot=plot(mark = request.args.get('mark')[1:-1], model = request.args.get('model')[1:-1],
                    year_from=request.args.get('year_from'), year_to = request.args.get('year_to'))
                
        return render_template('plot_page.html', 
                    mark = request.args.get('mark')[1:-1], model = request.args.get('model')[1:-1],
                    year_from=request.args.get('year_from'), year_to = request.args.get('year_to'), url_plot=url_plot,)
    
    return app

if __name__ == "__main__":
    app.run(debug=True)