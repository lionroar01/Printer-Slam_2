from flask import Flask, render_template, request
import csv
from os import path
import click
import json
from itertools import combinations
import pandas as pd 

app = Flask(__name__)

with open('SLAM_printers.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('SLAM_printers.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:rows[1] for rows in reader}



@app.route('/', methods=['GET', "POST"])

def home():
    colours_1 = pd.read_csv('templates/ip.csv')
    colours_2 = colours_1.values.tolist()
    colours = [i[0] for i in colours_2]
    #colours = ['10.10.65.5','10.453.4','10.4.24.5']
    #for colours in colours:
    
    return render_template('home.html', colours=colours)



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
    
    #print(mydict)
    #data = request.form['mydict']



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form.getlist('a', type=str)
        rslt = ' '.join(data)
    x = 4
    pairs = combinations(range(1,x), 2)
    return render_template('index.html', **locals())
   

@app.route('/end_point_for_your_fn', methods=["POST"])
def your_fn():
    data = request.form['input']

if __name__ == '__main__':
   app.run(debug=True)