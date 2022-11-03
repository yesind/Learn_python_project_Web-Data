from webapp import create_app
from fill_db import get_model

app = create_app()
with app.app_context():
    get_model()