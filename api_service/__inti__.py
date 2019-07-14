from flask_api import FlaskAPI
from flask_pymongo import PyMongo

app = FlaskAPI(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://mb:mb@viaskillz-runjj.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)



import api_service.resources