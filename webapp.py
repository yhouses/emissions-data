from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/response")
def format_dict_as_graph_points(data):
    with open('emissions.json') as carbon_increase:  
        carbon = json.load(carbon_increase)
    graph_points = ""
    for data in United_States:
        #{y: 2000, label: "CO2"}
        graph_points = graph_points + Markup(' { x: ' + str(data["Emissions"]["Type"]["C02"]) + ',  y: ' + str(data["Year"]) + '},')
    graph_points = graph_points [:-2]
    print(graph_points)
    return render_template('carbon-increase.html', data = carbon_increase)
    
if __name__=="__main__":
    app.run(debug=False)

