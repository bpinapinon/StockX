
import sys
import os
import subprocess
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# dependencies
from flask import render_template, jsonify, redirect, abort, url_for
from StockX_v1 import app, db
from MongoDB_RecursiveCSVParser import MongoDB_RecursiveCSVParser

# Start MongoDB Server by making OS call "mongod"
mongod = subprocess.Popen('mongod' , shell = True)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/bar")
def bar():
    return render_template("bar.html")    

@app.route("/load")
def mongo_csv_load():
    flag = MongoDB_RecursiveCSVParser.load_csv()
    if (not flag): abort(405)
    return ('csv files loaded into MongoDB')


@app.route("/chartdata")
def chartdata():
    chartData = list()
    index = 1
    inventory = db.sneaker_bar.find()
    for r in inventory:
        r.pop('_id')
        r['No.'] = str(index);
        index += 1
        chartData.append(r)
    return jsonify({'chartData': chartData})

@app.route("/bubble")
def bubble_chart():
    """Go to bubble chart page"""
    return render_template("bubble.html")

@app.route("/bubbledata")
def getbubbledata():

    sneakers = bubble.find()

    sneakerList = []
    for sneaker in sneakers:
        print(sneaker)
        sneakerItem = {
            'brand':sneaker['Brand'],
            'color':sneaker['Color'],
            'retailPrice':sneaker['Retail_Price ($)'],
            'avgSalePrice':sneaker['Avg_Sale_Price ($)'],
            'noSales':sneaker['Number_of_Sales']
        }
        sneakerList.append(sneakerItem)
    return jsonify({'sneakerList': sneakerList})   

if __name__ == "__main__":
    app.run(debug=True)