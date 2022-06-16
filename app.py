import json

from flask import Flask, render_template, request
import numpy as np
import pandas as pd

from function import *
import os


app  = Flask(__name__)

@ app.route('/',methods = ["GET","POST"])
def home_page():
    return render_template('home.html')


@app.route('/result',methods = ["GET","POST"])
def result():

    files = request.form["content"]
    location = request.form["content1"]
    mean_calculation(files,location)
    return " File Exported"











if __name__ == '__main__':
    app.run(debug=True)
    app.run(host ='0.0.0.0',debug  =true,post = os.environ['PORT])
