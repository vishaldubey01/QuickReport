#!/usr/local/bin/python3
from flask import Flask
from flask import request
import requests
import automatedForm
import json
import os

#os.chdir('../')

app = Flask(__name__)

@app.route('/')
def index():
    instructions = 'This server is used for autocomplete maintenance forms, use /getdata to get all data and /forms with json to parse data. Made by Vishal, Ansh, Rami, and Nigel'
    return instructions
  
@app.route('/greet')
def say_hello():
    return 'Hello from Server'

@app.route('/getdata', methods=['GET'])
def getData():
    with open('allData.json') as f:
        paths = json.load(f)
    print(json.dumps(paths, indent=4, sort_keys=True))
    return paths

@app.route('/form', methods=['POST'])
def form():
    updateJsonFile(request.json)
    r = requests.get(request.json["picture"])
    with open('pic.png', 'wb') as f:
        f.write(r.content)
    request.json["picture"] = os.getcwd()+"/pic.png"
    automatedForm.start()
    automatedForm.navigateToForm(request.json["name"])
    automatedForm.fillForm(request.json)
    print(request.json)
    return 'submitted'

def updateJsonFile(inputs):
    jsonFile = open("allData.json", "r") # Open the JSON file for reading
    data = json.load(jsonFile) # Read the JSON into the buffer
    jsonFile.close() # Close the JSON file

    ## Working with buffered content
    name = inputs["name"] 
    data[name].append(inputs)

    ## Save our changes to JSON file
    jsonFile = open("allData.json", "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()

# driver function 
if __name__ == '__main__': 
    app.run(debug = True)