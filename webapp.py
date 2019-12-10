from flask import Flask url_for, request, Markup, render_template, flash
import os
import json

app = Flask(__name__)

with open('county_demographics.json') as demographics_data:
    counties = json.load(demographics_data)

def get_state_options():
    listOfStates = []
    for county in counties:
        if county['State'] not in listOfStates:
            listOfStates.append(county['State'])
            state = county['State']
    options = ""
    for state in listOfStates:
        options = options + Markup("<option value=\"" + state + "\">" + state + "</option>")
    return options
    
def get_state_facts(state):
    income = 0
    
    for county in counties:
        if state == county['State']:
            income = county['Income']['Median Houseold Income']
    fact = Markup("<p>" + "Median household income for " + state + " is " + "$" + income + "</p>")
    return fact
    
@app.route("/")
def render_main():
    return render_template('index.html', options = get_state_options())

@app.route("/response")
def render_response():
    returnState = request.args['returnState']
    return render_template('index.html', options = get_state_options(), stateFact = get_state_facts(returnState))
    
if __name__=="__main__":
    app.run(debug=False)