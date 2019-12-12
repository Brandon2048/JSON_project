from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    with open('skyscrapers.json') as skyscraper_data:
        skyscraperdata = json.load(skyscraper_data)
    return render_template('desc.html')

@app.route("/p1")
def render_data():
    with open('skyscrapers.json') as skyscraper_data:
        skyscraperdata = json.load(skyscraper_data)
    if 'buildings' in request.args:
        return render_template('data.html', buildings = get_building_options(skyscraperdata),
         height1 = height(request.args['buildings'], skyscraperdata),
         floors1 = floors(request.args['buildings'], skyscraperdata),
         material1 = material(request.args['buildings'], skyscraperdata))
    else:
        return render_template('data.html', buildings = get_building_options(skyscraperdata))

def get_building_options(skyscraperdata):
    buildings = []
    print("Render")
    for data in skyscraperdata:
        if data["name"] not in buildings:
            buildings.append(data["name"])
    options = ""
    for data in buildings:
        options = options + Markup("<option value=\"" + data + "\">" + data + "</option>")
    return options

def height(buildings, skyscraperdata):
    height = 0
    for data in skyscraperdata:
        if data["name"] == buildings:
            height = height + data["statistics"]["height"]

    return height

def floors(buildings, skyscraperdata):
    floors = 0
    for data in skyscraperdata:
        if data["name"] == buildings:
            floors = floors + data["statistics"]["floors above"]

    return floors

def material(buildings, skyscraperdata):
    material = ""
    for data in skyscraperdata:
        if data["name"] == buildings:
            material = data["material"]
    return material

if __name__=="__main__":
    app.run(debug=True)
