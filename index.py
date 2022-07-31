# import requests
# import string
# from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['DEBUG'] = True

# @app.route('/')
# def index():
#     city='Las Vegas'
#     url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=b21a2633ddaac750a77524f91fe104e7"
#     r=requests.get(url.format(city)).json()
#     print(r)

#     return render_template('weather.html')

# b21a2633ddaac750a77524f91fe104e7

import requests
import configparser
from flask import Flask ,render_template,request
import datetime
from datetime import datetime as curr_date





app=Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def weather_dashboard():
    return render_template('home.html')

@app.route('/results',methods=['POST'])
def render_results():
    zip_code=request.form.get("zipCode")

    api_key=get_api_key()
    data=get_weather_results(zip_code,api_key)
    temperature =round(data["main"]["temp"]-2)
    feels_like = "{0:.2f}".format(data["main"]["feels_like"])
    weather = data["weather"][0]["main"]
    location = data["name"]
    humidity=data["main"]["humidity"]
    date,time=str(datetime.datetime.now()).split(" ")
    wind=data["wind"]["speed"]
    t=time.split(":")
    temp=""
    for i in range(len(t)-1):
        if len(t[i])>3:
            tt=float(t[i])
            t1=int(tt)
        else:
            t1=int(t[i])
        if t1>12:
            t1=t1-12
        temp=temp+str(t1)
        if(i!=len(t)-2):
            temp=temp+":"
    time=temp
    day=curr_date.today().strftime("%A")
    months=["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"]
    result=data['weather'][0]['icon'];
    date=date.split("-")
    all_details=time+" "+"-"+" "+day+" "+months[int(date[1])]+" "+date[0]
    print(all_details)
    print(data)
    print(time)
    return render_template('results.html',location=location,result=result,temperature =temperature ,temp=temp,wind=wind,feels_like=feels_like,weather=weather,humidity=humidity,all_details=all_details)
    return "Zip_code: "+zip_code




def get_api_key():
    config=configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']


def get_weather_results(zip_code,api_key):
    url = "http://api.openweathermap.org" \
          "/data/2.5/weather?q={}&appid={}&units=metric".format(zip_code,api_key)
    r=requests.get(url)
    return r.json()

if __name__ == '__main__':
    app.run()



# print(get_weather_results("95129",get_api_key()))

