from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def intro():
    with open('skyscrapers.json') as skyscraper_data:
        skyscraperdata = json.load(skyscraper_data)
    return render_template('desc.html')

if __name__=="__main__":
    app.run(debug=True)
