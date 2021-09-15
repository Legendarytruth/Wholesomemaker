from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import flask


app = Flask(__name__)

load_dotenv()

cluster = MongoClient(os.getenv("MONGODB_URL"))
levelling = cluster["discord"]["levelling"]


@ app.route('/')
def index():
    rankings = levelling.find().sort("xp", -1)
    return render_template('index.html', rankings=list(rankings))


if __name__ == "__main__":
    app.run(debug=True)
