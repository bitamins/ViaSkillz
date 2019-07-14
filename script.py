from flask import Flask, escape, request

app = Flask(__name__)
myport = process.env.PORT || 5000
@app.route('/')
def hello_world():
    return 'Hello, World!'

app.run(port=myport)