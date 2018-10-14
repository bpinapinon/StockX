# dependencies
from flask import Flask, render_template, jsonify, redirect
import pymongo
from pymongo import MongoClient


# create instance of Flask app
app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = MongoClient("mongodb://localhost:27017")
db = client.StockX_DB
# bubble = db.sneaker_bubble
bar = db.Sneaker_bar


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/bubble")
def bubble_chart():
    """Go to bubble chart page"""
    inventory = list(db.sneaker_bubble.find())
    print(inventory)
    return render_template("bubble.html", inventory=inventory)



if __name__ == "__main__":
    app.run(debug=True)