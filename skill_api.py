from flask_api import FlaskAPI
import pymongo

client = pymongo.MongoClient(<Atlas connection string>)

app = FlaskAPI(__name__)

@app.route("/skillup", methods=['GET', 'POST'])
def skillup():
    data = request.data






if __name__ == "__main__":
    intro = 'Running your app now!'
    print('Hello: {}'.format(intro))
    app.run(debug=True)