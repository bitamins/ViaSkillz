from flask import Flask, escape, request

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'

app.run(debug=True, port=33507)