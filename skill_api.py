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


@app.route("/listuser", methods=['POST'])
def listuser():
    print("listing user skills")
    mydata = mongo.db.data

    text = request.data.to_dict(flat=False)['text'][0]
    args = text.split(' ')
    myname = args[0]

    try:
        docdict = mydata.find_one({"name": myname}) #Debug this forsure probably
        print('document found for {}'.format(myname))
        print(docdict)
    except Exception as e:
        print('query failed with: {}'.format(e))
        docdict = False

    # {"_id":{"$oid":"5d2b52285028a4e0350e637d"},"name":"@michael.mu.sun","skills":{"python":{"$numberInt":"5"},"javascript":{"$numberInt":"2"}}}

    retVal = 'Skills for {} \n'.format(myname)
    for key,val in docdict["skills"].items():
        tmp = str(key) + '-' + str(val) + '\n'
        retVal += tmp


    print(retVal)

    return retVal

@app.route("/listskill", methods=['POST'])
def listskill():
    print("listing user skills")
    mydata = mongo.db.skill

    text = request.data.to_dict(flat=False)['text'][0]
    args = text.split(' ')
    myskill = args[0]

    try:
        docdict = mydata.find_one({"skill": myskill}) #Debug this forsure probably
        print('document found for {}'.format(myskill))
        print(docdict)
    except Exception as e:
        print('query failed with: {}'.format(e))
        docdict = {'names':[]}

    # {"_id":{"$oid":"5d2b52285028a4e0350e637d"},"name":"@michael.mu.sun","skills":{"python":{"$numberInt":"5"},"javascript":{"$numberInt":"2"}}}

    retVal = 'Top 10 skilled in {} \n'.format(myskill)
    for val in docdict["names"][:10]:
        tmp = str(val) + '\n'
        retVal += tmp


    print(retVal)

    return retVal




@app.route("/skillup", methods=['POST'])
def skillup():
    # Assume user, skills collections exist
    # data = request.args

    #
    # USER COLLECTION
    #
    
    mydata = mongo.db.data
    print("Upping a skill")
    print(request.data,type(request.data))
    text = request.data.to_dict(flat=False)['text'][0]
    print(text,type(text))
    args = text.split(' ')
    myname = args[0] 
    myskill = args[1]


    print('name {} skill {}'.format(myname,myskill))

    try:
        docdict = mydata.find_one({"name": myname}) #Debug this forsure probably
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
    
    #
    # FEED COLLECTION
    #
    #Logging the feed: Voter, Skill, Votee
    myfeed = mongo.db.feed
    mypoints = docdict["skills"][myskill]
    myvoter = request.data.to_dict(flat=False)['user_name'][0]
    myvotee = myname
    myskill = myskill
    feeddict = {
                    "voter": myvoter,
                    "votee": myvotee,
                    "skill": myskill,
                    "points": mypoints
                }
    myfeed.insert_one(feeddict)

    #
    # SKILL COLLECTION
    #
    dbskill = mongo.db.skill

    try:
        docdict = dbskill.find_one({"skill": myskill}) #Debug this forsure probably
        print('document found for {}'.format(myname))
        print(docdict)
    except Exception as e:
        print('query failed with: {}'.format(e))
        docdict = False

    if docdict:
        if myname in docdict["names"]:
            print('Name in names {} for {}'.format(myname,myskill))
        else:
            print('creating new name {} for {}'.format(myname,myskill))
            print(docdict,type(docdict['names']))
            docdict["names"].append(myname)
            dbskill.remove({"skill": myskill})
            dbskill.insert_one(docdict)
    else:
        print('creating new skill {} and user {}'.format(myskill,myname))
        docdict = {
                "skill": myskill,
                "names": [
                    myname
                ]
            }
        dbskill.insert_one(docdict)
    
    


    retVal = 'Added +1 {} to {}. Now at {}'.format(myskill,myname,mypoints)

    return retVal






if __name__ == "__main__":
    # intro = 'Running your app now!'
    # print('Hello: {}'.format(intro))
    host='0.0.0.0'

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)