from flask import Flask, render_template, request

import websockets
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
    print(mydict)



@app.route('/', methods=['GET', "POST"])

def home():
    colours_1 = pd.read_csv('templates/ip.csv')
    colours_2 = colours_1.values.tolist()
    colours = [i[0] for i in colours_2]

    SlamID_1 = pd.read_csv('templates/slamID.csv')
    SlamID_2 = SlamID_1.values.tolist()
    SlamID = [i[0] for i in SlamID_2]

    with open('SLAM_printers.csv', mode='r') as infile:
        reader = csv.reader(infile)
        with open('SLAM_printers.csv', mode='w') as outfile:
            writer = csv.writer(outfile)
            mydict = {rows[0]:rows[1] for rows in reader}

            All_station = zip(colours, SlamID)
    #colours = ['10.10.65.5','10.453.4','10.4.24.5']
    #for colours in colours:
    
    return render_template('home2.html', colours = colours, SlamID=SlamID,All_station= All_station)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000 )