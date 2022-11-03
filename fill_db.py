from webapp.model import db, Model

def get_model():
    models = ['DEFENDER', 'DISCOVERY', 'DISCOVERY_SPORT', 'EVOQUE', 'FREELANDER', 'RANGE_ROVER', 
            'RANGE_ROVER_SPORT', 'RANGE_ROVER_VELAR']
    for model_car in models:
       save_models(model_car, 4)
       print(model_car)

def save_models(name, mark_id):
    new_model = Model(name=name, mark_id=mark_id)
    db.session.add(new_model)
    db.session.commit()
    db.session.close()

