import os
from flask_api import FlaskAPI
from flask_pymongo import PyMongo

# client = pymongo.MongoClient('mongodb+srv://mb:mb@viaskillz-runjj.mongodb.net/test?retryWrites=true&w=majority')

app = FlaskAPI(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://mb:mb@viaskillz-runjj.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route("/")
def index():
    text = 'hello this is the index'
    print(text)
    return text


@app.route("/skillup")
def skillup():
    # data = request.args
    
    test = {
        'andrew':{
            'python': 1
        }
    }
    mongo.db.test.insert_one(test)

    return 'test'






if __name__ == "__main__":
    # intro = 'Running your app now!'
    # print('Hello: {}'.format(intro))

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)