from flask import Flask, request, Markup, render_template, flash
import os
import json

app = Flask(__name__)

"""def get_state_facts(state):
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)"""

def get_state_options():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    listOfStates = []
    for county in counties:
        if county['State'] not in listOfStates:
            listOfStates.append(county['State'])
    options = ""
    for state in listOfStates:
        options = options + Markup("<option value=\"" + state + "\">" + state + "</option>")
    return options

@app.route("/")
def render_main():
    return render_template('index.html', responseFromServer = get_state_options())
    
@app.route("/response")
def render_response():
    return render_template('response.html', responseFromServer2 = "hi")

if __name__=="__main__":
    app.run(debug=False)