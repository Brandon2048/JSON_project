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
         material1 = material(request.args['buildings'], skyscraperdata),
         status1 = status(request.args['buildings'], skyscraperdata),
         location1 = location(request.args['buildings'], skyscraperdata),
         n = get_name(request.args['buildings'], skyscraperdata))
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

def status(buildings,skyscraperdata):
    status = ""
    for data in skyscraperdata:
        if data["name"] == buildings:
            status= data["status"]["current"]
    return status

def location(buildings,skyscraperdata):
    location = ""
    for data in skyscraperdata:
        if data["name"] == buildings:
            location = data["location"]["city"]
    return location

def height(buildings, skyscraperdata):
    height = 0
    for data in skyscraperdata:
        if data["name"] == buildings:
            height = height + data["statistics"]["height"]

    return round(height,2)

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

def get_name(buildings,skyscraperdata):
    name = ""
    for data in skyscraperdata:
        if data["name"] == buildings:
            name = data["name"]
    return name

@app.route("/p2")
def render_graph():
    with open('skyscrapers.json') as skyscraper_data:
        skyscraperdata = json.load(skyscraper_data)
    return render_template('graph.html', points = get_points(skyscraperdata))

def get_points(skyscraperdata):
    points = []
    options = ""
    for data in skyscraperdata:
        if data["name"] not in points:
            points.append(data["name"])    
            options = options + Markup('{ label: ' + '"' + str(data["name"]) + '"' ', y: ' + str(data["statistics"]["height"]) + ' },')
    return options

if __name__=="__main__":
    app.run(debug=True)
