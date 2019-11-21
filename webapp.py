from flask import Flask, request, Markup, render_template, flash
import os
import json

app = Flask(_name_)

@app.route("index.html")
def get_state_options():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    listOfStates = []
    for county in counties:
        if county['State'] !in listOfStates:
            listOfStates.append(county['State'])
    options = ""
    for state in listOfStates:
        options = options + Markup("<option value=\"" + s + "\">" + s + "</option>")
    return options
	

if __name__=="__main__":
    app.run(debug=False)