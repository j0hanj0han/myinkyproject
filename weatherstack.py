import requests
import pprint
import json

pp = pprint.PrettyPrinter(indent=4)
city="Montpellier"
api_key="316cb339b0ae48818f692bfb98c4f727"


def connect_to_api():
    try:
        response = requests.get(f"http://api.weatherstack.com/forecast?access_key={api_key}&query={city}")
        json_data = json.loads(response.text)
        print(json)
        return json_data
    except Exception as e: 
        print(e)
# json_data = json.loads(response.text)
# print(pp.pprint(json_data))


def get_weather():
    json_data = connect_to_api()
    city_name=json_data['request']['query']
    weather_text=json_data['current']['weather_descriptions'][0]
    temperature_now=json_data['current']['temperature']
    date_forecast = str(list(json_data['forecast'].keys())[0])
    temperature_min=json_data['forecast'][date_forecast]['mintemp']
    temperature_max=json_data['forecast'][date_forecast]['maxtemp']



    print('------------------')
    print('Météo pour la ville de :', city_name)
    print('Temps actuel:', weather_text)
    print('Température actuelle:', temperature_now)
    print('Temperature minimale:', temperature_min)
    print('Temperature maximale:', temperature_max)
    print('-------------------')
    meteo=[city_name, weather_text, temperature_now, temperature_min, temperature_max]
    return meteo
    
# if  __name__ == "__main__":
#     get_weather()
    