from re import U
from flask import Flask,jsonify,request
app=Flask(__name__)
tasks=[
    {
        'id':1,
        'title':u 'buy groceries',
        'description':u 'milk,cheese,pizza,fruit',
        'done':False
    },
    {
        'id':2,
        'title':u 'learn python',
        'description':u 'need a good python tutorial',
        'done':False
    }]
@app.route("/")
def hello_world():
    return "hello world"

@app.route("/add-data",methods=["POST"])
