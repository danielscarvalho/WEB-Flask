
# -*- coding: utf-8 -*-
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import jsonify, request
import json
import time
import platform
import sys
import math

app = Flask(__name__)

def avg(list):
    return sum(list) / float(len(list))

@app.route('/')
def hello_world():
    return jsonify({"message": 'Hello from Flask!', \
                    "who": "I am the robot!"})

@app.route('/now')
def now():
    vdate, vtime = time.strftime("%d/%m/%Y %H:%M:%S").split(" ")
    return jsonify({"date":vdate, "time":vtime})

@app.route('/cow')
def cow():
    cow="""
         (__)
         (oo)
  /-------\/
 / |     ||
*  ||----||
   ^^    ^^
   Cow
        """

    return("<html><body><pre>" + \
           cow + \
           "</pre></body></html>")

@app.route('/info')
def info():
    version, release = sys.version_info[:2]
    python_version = str(version) + "." + str(release)
    return jsonify({"platform":platform.platform(), \
                    "python": python_version })

@app.route('/fsum', methods=['GET', 'POST'])
def fsum():
    content = request.json

    return jsonify({"sum" : sum(content["values"]), \
                    "max" : max(content["values"]), \
                    "min" : min(content["values"]), \
                    "average" : avg(content["values"]), \
                    "count": len(content["values"])})

@app.route('/fatorial/<valor>')
def fatorial(valor):
    return jsonify({"valor": valor, \
                    "fatorial": math.factorial(int(valor))})

# Execução local!!!
if __name__ == '__main__':
    app.run(debug=True)


