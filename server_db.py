
# -*- coding: utf-8 -*-
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import jsonify, request
import json
import os

DBFILE = 'db/database.json'
DBMAXFILESIZE = 1048576 #1 MB
DBFILELOCK = False

app = Flask(__name__)

def checkFileSize():
    if os.path.getsize(DBFILE) <= DBMAXFILESIZE:
        print("file size: ", os.path.getsize(DBFILE))
        return True
    else:
        return False

def checkDbOpen():
    pass

def writeDb(dicData):
    
    dbfile = open(DBFILE, 'w')
    dbfile.write(json.dumps(dicData))
    dbfile.close()

def readDb():
    dbfile = open(DBFILE, 'r')
    dbdata = dbfile.read()
    dbfile.close()
    print ("dbdata: ",dbdata)
    if len(dbdata.strip()) < 1:
        return {} #retorna dicionário vazio
    else: 
        return json.loads(dbdata.replace("'", "\""))

@app.route('/')
def root():
    data = readDb()
    return jsonify({"keys" : list(data.keys())})

@app.route('/read/<key>')
def read_key(key):
    data = readDb()
    val = data[key]
    return jsonify({"key" : key, "value": val})

@app.route('/read/all')
def read_all():
    data = readDb()
    return jsonify(data)

@app.route('/write/<key>/<value>')
def write_key(key, value):
    if checkFileSize():
        data = readDb()
        data[key] = value
        writeDb(data)
        return jsonify({"write": "ok"})
    else:
        return jsonify({"write": "Error!! DB File size exceded!!"})

@app.route('/delete/<key>')
def delete_key(key):
    data = readDb()
    if key in list(data.keys()):
        del data[key]
        writeDb(data)
        return jsonify({"delete": "ok"})
    else:
        return jsonify({"delete": "fail", "key": key, "error": "Key not found!!"})

# Execução local!!!
# Remova esta parte para executar no Python Anywhere!!!
if __name__ == '__main__':
    app.run(debug=True)

