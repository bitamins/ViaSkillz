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