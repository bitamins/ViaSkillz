from flask_api import FlaskAPI
import pymongo

client = pymongo.MongoClient('mongodb+srv://mb:mb@viaskillz-runjj.mongodb.net/test?retryWrites=true&w=majority')

app = FlaskAPI(__name__)

@app.route("/")
def index():
    text = 'hello this is the index'
    print(text)
    return text


@app.route("/skillup", methods=['GET', 'POST'])
def skillup():
    data = request.data






if __name__ == "__main__":
    intro = 'Running your app now!'
    print('Hello: {}'.format(intro))
    app.run(debug=True)