from flask import Flask, url_for, render_template, request, Markup
import json
app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/response")
def format_dict_as_graph_points ():
    with open('emissions.json') as carbon_increase:  
        carbon = json.load(carbon_increase)
    graph_points = ""
    for data in carbon:
        if data ["Country"] == "United States":
            graph_points = graph_points + Markup(' { x: ' + str(data["Year"]) + ',  y: ' +  str(data["Emissions"]["Type"]["CO2"]) + '},')
    graph_points = graph_points [:-1]
    print(graph_points)
    return render_template('carbon-increase.html', data = graph_points)
    
@app.route("/response1")
def home():
    country = get_country_options ()
    return render_template('by-country.html', country_options = country, year_options=get_year_options() )
def get_country_options():
    with open('emissions.json') as demographics_data:
        country = json.load(demographics_data)
    states = []
    options = ""
    for c in country:
        options += Markup ("<option value=\"" + c["Country"] + "\">" + c["Country"] + "</options>")
    return options
    
def get_year_options():
    with open('emissions.json') as demographics_data:
        year = json.load(demographics_data)
    years = []
    for y in year:
        if y["Year"] not in years:
            years.append(y["Year"])
    options = ""
    for y in years:
        options += Markup ("<option value=\"" + str(y) + "\">" + str(y) + "</options>")
    return options
    
@app.route("/showFact")
def methane():
    methane = get_methane_options ()
    country = get_country_options ()
    return render_template('by-country.html', methane = methane, country_options = country, year_options=get_year_options())
def get_methane_options():
    with open('emissions.json') as result_data:
        methane = json.load(result_data)
    options = ""
    for m in methane:
        if str(m["Year"]) == request.args ["Year"] and m["Country"] == request.args["Country"]:
            options += Markup (m["Emissions"]["Type"]["CH4"])
    return options
    
@app.route("/showAmount")
def center():
    if "Country" not in request.args:
        country = get_country_options ()
        return render_template('by-year.html', country_options = country, year_options=get_year_options() )
    else: 
        nitrous = get_nitrous_options ()
        country = get_country_options ()
        return render_template('by-year.html', nitrous = nitrous, country_options = country, year_options=get_year_options())
def get_nitrous_options():
    with open('emissions.json') as result_data:
        nitrous = json.load(result_data)
    options = ""
    for n in nitrous:
        if str(n["Year"]) == request.args ["Year"] and n["Country"] == request.args["Country"]:
            options += Markup (n["Emissions"]["Type"]["N2O"])
    return options
    
    
if __name__=="__main__":
    app.run(debug=False)
    
    
   