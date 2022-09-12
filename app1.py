from flask import Flask, render_template, request
import csv
from os import path
import click
import json
from itertools import combinations
import pandas as pd 

app = Flask(__name__)

@app.route('/')
@app.route("/home")
def home():

    return render_template('home1.html', **locals())

x = '{ "Slam101_1":"10.161.18.196","Slam101_2":"10.161.18.36","Slam101_3":"10.161.18.194"}'

@app.route("/stationIP", methods=["GET", 'POST'])
def result():
    output = request.form.to_dict()
    name = output['name']

    def result_1():
        def in_list(targ_list, elem):
            return elem in targ_list
            y = json.loads(x)
        
            Station_ID = (y[("Station Name: (Example: 'Slam101_1') : ")])

            Sation = in_list(x, Station_ID) 
    

        

    return render_template('home1.html', name = "name", y = "y", Station_ID= 'Station_ID', Sation = 'Sation')




@app.route("/config", methods=["GET", 'POST'])
def config():
    choices = []
    with open(request.form['FLASK_WORK/IPs.csv'], 'r') as csvfile :
        reader = csv.reader(csvfile)
        titles = next(reader)
        for index, title in enumerate(titles,1):
            choice = 'choice-' + str(index)
            choices.append(title, request.form.get(choice))




@app.route('/slam_in_pcns', methods=['GET', 'POST'])
def in_pcns():
    slam = "mydict"
    return render_template('home.html', slam = "mydict") 




if __name__ == '__main__':
   app.run(debug=True)