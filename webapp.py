from flask import Flask, url_for, render_template, request

app = Flask(__webapp__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/response")
def format_dict_as_graph_points(data):
    graph_points = ""
    for carbon in United States:
        #{y: 2000, label: "CO2"}
        graph_points = graph_points + Markup(' { y: ' to str(data[Emmissions{CO2}]) + ' { x: ' to str(data[Country{United States}]) + ', label:
    graph_points = graph_points [:-2]
    print(graph_points)
    return render_template('carbon-increase.html', data = graph_points)
    
if __name__=="__main__":
    app.run(debug=False)

