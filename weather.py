from flask import Flask,render_template,request,abort
from flask.wrappers import Response
# import requests to make a request to api
import requests


app = Flask(__name__)
def tocelcius(temp):
    return str(round(float(temp) - 273.16,2))

@app.route('/',methods=['POST','GET'])
def weather():
    api_key = '82a3e79c71bcf0ba07c339131b6e3ec0'
    if request.method == 'POST':
        city = request.form['city']
    else:
        #for default name London
        city = 'London'

    # source contain json data from api
    try:
        source = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid='+api_key)
    except:
        return abort(404)
    # converting json data to dictionary

    list_of_data = source.json()

    # data for variable list_of_data
    try:
        data = {
            #"short_description": str(list_of_data['weather'][0]['description']),
            "description": str(list_of_data['name']) +' today has '+ str(list_of_data['weather'][0]['description']),
            "temp": tocelcius(list_of_data['main']['temp']) + 'C',
            "feels_like": tocelcius(list_of_data['main']['feels_like']) + 'C',
            "max_temp": tocelcius(list_of_data['main']['temp_max']) + 'C',
            "min_temp": tocelcius(list_of_data['main']['temp_min']) + 'C',
            "pressure": str(list_of_data['main']['pressure']) + 'hPa',
            "humidity": str(list_of_data['main']['humidity']) + '%',
            "wind_speed":str(list_of_data['wind']['speed']) + 'm/sec',
        }
        return render_template('index.html',data=data)
    except:
        abort(Response('No such place found: "'+city+'" Please refresh and try again..'))
     

if __name__ == '__main__':
    app.run(debug=True)
