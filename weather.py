from flask import Flask, render_template, request

# import json to load JSON data to a python dictionary
import json

# urllib.request to make a request to api
import urllib.request


app = Flask(__name__)

def tocelcius(temp):
    return str(round(float(temp) - 273.16,2))

@app.route('/', methods =['POST', 'GET'])
def weather():
	if request.method == 'POST':
		city = request.form['city']
		# cityr = city.replace(" ","_")
	else:
		# for default name mathura
		city = 'mathura'

	# your API key will come here
	api = 'b46f0e4315193962446ddec655e09491'

	# source contain json data from api
	source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api).read()

	# converting JSON data to a dictionary
	list_of_data = json.loads(source)

	# data for variable list_of_data
	data = {
		"country_code": str(list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
        "temp": str(list_of_data['main']['temp']) + 'k',
        "temp_cel": tocelcius(list_of_data['main']['temp']) + ' C',
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
        "cityname":str(city),
	}
	print(data)
	return render_template('index.html', data = data)



if __name__ == '__main__':
	app.run(debug = True)
