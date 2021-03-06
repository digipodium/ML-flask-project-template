import logging

from flask import Flask
try:
    from sklearn.externals import joblib
except:
    import joblib

# create logger for app
logger = logging.getLogger('app')
logger.setLevel(logging.INFO)

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT)

app = Flask(__name__)
app.config.from_object("app.config")

# unpickle my models
MODELS = {
    "iris": {
        "estimator" : joblib.load('models/iris/model.pkl'),
        "target_names": ['setosa', 'versicolor', 'virginica']
    }
}

from .views import *   # flake8: noqa


# Handle Bad Requests
@app.errorhandler(404)
def page_not_found(e):
    """Page Not Found"""
    return render_template('404.html'), 404
