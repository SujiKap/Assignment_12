# +
from flask import Flask, render_template, redirect
from pymongo import MongoClient
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection locally
conn = 'mongodb://localhost:27017'
client = MongoClient(conn)
# connect to a database
db = client.mars_app
#mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
print (db)

@app.route("/")
def index():
    mars = db.mars.find_one()
    return render_template("index.html", listings=mars)

@app.route("/scrape")
def scraper():
    mars = db.mars
    listings_data = scrape_mars.scrape()
    mars.update({}, listings_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=False)
# -


