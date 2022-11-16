from flask import Flask, jsonify, request
import datetime as dt
import requests



app = Flask(__name__)


@app.route('/america',methods=['GET'])
def get_data():
    x = requests.get('http://worldtimeapi.org/api/timezone/America/Toronto')
    
    data = x.json()

    currentTime = data['datetime']

    date = dt.datetime.fromisoformat(currentTime).strftime('%d/%m/%Y')
    time = dt.datetime.fromisoformat(currentTime).strftime('%X')
    
    return jsonify(date,time) 

@app.route('/london',methods=['GET'])
def get_london():
    x = requests.get('http://worldtimeapi.org/api/timezone/Europe/London')
    
    data = x.json()

    currentTime = data['datetime']

    date = dt.datetime.fromisoformat(currentTime).strftime('%d/%m/%Y')
    time = dt.datetime.fromisoformat(currentTime).strftime('%X')
    
    return jsonify(date,time)  

@app.errorhandler(404) 
def invalid_route(e): 
    return "Invalid route."


if __name__ == '__main__':
    app.run()