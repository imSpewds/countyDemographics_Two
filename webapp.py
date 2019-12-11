from flask import Flask, url_for, request, Markup, render_template, flash
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
    options = ""
    for state in listOfStates:
        options = options + Markup("<option value=\"" + state + "\">" + state + "</option>")
    return options
    
def get_state_facts(state):
    income = 0
    my_county = counties[0]['County']
    
    fact = ""
    for county in counties:
        if state == county['State']:
            income = county['Income']['Median Houseold Income']
            my_county = county['County']
    fact = fact + Markup("<p>" + "Median household income for " + my_county + " in " + state + " is " + "$" + str(income) + "</p>")
    return fact
    
@app.route("/")
def render_main():
    return render_template('index.html', options = get_state_options())

@app.route("/response")
def render_response():
    returnState = request.args['returnState']
    return render_template('index.html', stateFact = get_state_facts(returnState), options = get_state_options())
    
if __name__=="__main__":
    app.run(debug=False)
