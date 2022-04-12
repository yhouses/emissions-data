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
    
def home ():
    years = get_year_options ()
    return render_template('by_country.html', year_options = year)
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
def home():
    methane = get_methane_options ()
    return render_template('by_country.html', year_options = year)
def get_methane_options():
    with open('emissions.json') as result_data:
        methane = json.load(result_data)
    methane = []
    for m in methane:
    if m == ["Year"] + ["Country"]
        options += Markup (m["Emissions"]["Type"]["CH4"])
    return options
    
    
if __name__=="__main__":
    app.run(debug=False)
    
    
   