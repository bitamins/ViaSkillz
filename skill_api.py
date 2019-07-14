import os
from flask_api import FlaskAPI
from flask_pymongo import PyMongo
from flask import request
from werkzeug.datastructures import ImmutableMultiDict
import json

# client = pymongo.MongoClient('mongodb+srv://mb:mb@viaskillz-runjj.mongodb.net/test?retryWrites=true&w=majority')

app = FlaskAPI(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://mb:mb@viaskillz-runjj.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route("/")
def index():
    text = 'hello this is the index'
    print(text)
    return text


@app.route("/listskill", methods=['POST'])
def listskill():
    pass  


@app.route("/skillup", methods=['POST'])
def skillup():
    # Assume user, skills collections exist
    # data = request.args
    
    mydata = mongo.db.data
    # print(flask.request)
    print("Upping a skill")
    print(request.data,type(request.data))
    # myname = text['name']
    # myskill = text['skill']
    # imd = ImmutableMultiDict
    text = request.data.to_dict(flat=False)['text'][0]
    print(text,type(text))
    args = text.split(' ')
    myname = args[0] 
    myskill = args[1]


    print('name {} skill {}'.format(myname,myskill))

    try:
        docdict = mydata.find({"name": myname}) #Debug this forsure probably
        print('document found for {}'.format(myname))
        print(docdict)
    except Exception as e:
        print('query failed with: {}'.format(e))
        docdict = False
    if docdict:
        if myskill in docdict["skills"]:
            print('updating skill {} for {}'.format(myskill,myname))
            docdict["skills"][myskill] += 1
        else:
            print('creating new skill {} for {}'.format(myskill,myname))
            docdict["skills"][myskill] = 1
        mydata.remove({"name": myname})
    else:
        print('creating new skill {} and user {}'.format(myskill,myname))
        docdict = {
                "name": myname,
                "skills": {
                    myskill:1
                }
            }
    
    mydata.insert_one(docdict)

    # # QUERYING FROM MONGODB
    # if mydata.find({'name':name}):
    #     # if name exists
    #     result = mydata.update_one({name:{skill:}},{})
    # else:
    #     # if name not exist yet
    #     if mydata.find({"skills".skill:})
    #     result = mydata.insert_one(
    #     [{   
    #         "name": myname,
    #         "skills":[
    #             {skill:1}
    #         ]
    #     }]
    #     )

    retVal = 'Added +1 {} to {}'.format(myskill,myname)

    return retVal






if __name__ == "__main__":
    # intro = 'Running your app now!'
    # print('Hello: {}'.format(intro))
    host='0.0.0.0'

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)