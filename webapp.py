from flask import Flask, request, Markup, render_template, flash
import os
import json

app = Flask(__name__)

def get_state_facts(state):
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    fact = 0
    for key in counties:
        if key["State"] == state:
            fact = state["Income"]["Median Household Income"]
    return fact

def get_state_options():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    listOfStates = []
    for county in counties:
        if county['State'] not in listOfStates:
            listOfStates.append(county['State'])
    options = ""
    for state in listOfStates:
        options = options + Markup("<option value=\"" + state + "\">" + state + "</option>" + "<p>" + get_state_facts(state) + "</p>")
    return options

@app.route("/")
def render_main():
    return render_template('index.html', responseFromServer = get_state_options())
    
if __name__=="__main__":
    app.run(debug=False)