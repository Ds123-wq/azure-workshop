from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Deepak Are you Ready Yes!! <img src= "https://myimagest.blob.core.windows.net/mytest/deepak.jpeg" />"
