import logging

from flask import Flask

# create logger for app
logger = logging.getLogger('app')
logger.setLevel(logging.INFO)

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT)

app = Flask(__name__)
app.config.from_object("app.config")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///predictions.sqlite3'  # step 2
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# unpickle my models


from .views import *   # flake8: noqa
from .models import *

# Handle Bad Requests
@app.errorhandler(404)
def page_not_found(e):
    """Page Not Found"""
    return render_template('404.html'), 404

with app.app_context():
    db.init_app(app)
    db.create_all()

