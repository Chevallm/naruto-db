#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
from flask import render_template
import json
from flask import request


app = Flask(__name__)

@app.route('/')
def index():
    with open("personnages.json") as file:
        d = json.load(file)
        print(d)
        return render_template('index.html', ninjas=d)

@app.route('/add', methods=['GET'])
def add():
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
