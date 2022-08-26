from flask import Flask, render_template, redirect, url_for, Response, request, session
import pandas as pd
import plotly.graph_objects as go
import requests
import json
import plotly
import plotly.express as px


app = Flask(__name__,template_folder='templates')

def air_graph(labels,values):
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    #fig.show()
    plot_air = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return plot_air

#l = ["CO","NO2","OZONE","PM10","PM25","SO2"]3
#v = [1.453,25.291,8.032,52.24,21.943,1.898]
#air_graph(l,v)

# ROUTES
@app.route('/')
def home():
    return render_template('main_o.html')

@app.route("/success", methods=["GET", "POST"])
def ozone():
    city = request.form['city']
    city = city.upper()
    url = "https://api.ambeedata.com/ghg/latest/by-place"
    querystring = {"place":city}
    headers = {
        'x-api-key': "45bc722a000629ee4bb92e0158710002d1c69cafa0b199e6f262a6ad46b4d9d0",
        'Content-type': "application/json"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    #print(response.text)
    return render_template("success_o.html") 
if __name__ == "__main__":
    app.run(debug=True)