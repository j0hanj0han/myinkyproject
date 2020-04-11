import requests
import pprint
import json

pp = pprint.PrettyPrinter(indent=4)
api_key = "316cb339b0ae48818f692bfb98c4f727"


def connect_to_api(city):
    try:
        response = requests.get(
            f"http://api.weatherstack.com/forecast?access_key={api_key}&query={city}"
        )
        json_data = json.loads(response.text)
        #print(json_data)
        return json_data
    except Exception as e:
        print(e)


# json_data = json.loads(response.text)
# print(pp.pprint(json_data))

def convert_am_to_pm():
    pass


def get_weather(city):
    json_data = connect_to_api(city)
    #print(json_data)
    date_forecast = str(list(json_data["forecast"].keys())[0])
    city_name = json_data["location"]["name"]
    region = json_data["location"]["region"]
    weather_text = json_data["current"]["weather_descriptions"][0]
    temperature_now = json_data["current"]["temperature"]
    temperature_min = json_data["forecast"][date_forecast]["mintemp"]
    temperature_max = json_data["forecast"][date_forecast]["maxtemp"]
    ensoleillement= json_data["forecast"][date_forecast]["sunhour"]
    uv_index= json_data["forecast"][date_forecast]["uv_index"]
    sunrise = json_data["forecast"][date_forecast]["astro"]["sunrise"]
    sunset = json_data["forecast"][date_forecast]["astro"]["sunset"]

    city_name = f"{city_name}, {region}"
    weather_text= f"Le temps est: {weather_text}"
    temperature_now = f"Température actuelle {temperature_now}°C"
    temperature_max=f=f"Température max {temperature_max}°C"
    ensoleillement= f"{ensoleillement} h de soleil aujourd'hui."
    uv= f"Indice UV {uv_index}/10."
    sunrise = f"Le soleil se lève à: {sunrise}"
    sunset= f"Le soleil se couche à: {sunset}"

    meteo = [city_name, weather_text, temperature_now, temperature_max, ensoleillement, uv, sunrise, sunset]
    print(*meteo)
    return meteo
     
     # lever / coucher du soleil
     # indice UV
     # les saints
     # humidity
     # heure d'ensoleillement

# if  __name__ == "__main__":
#     get_weather("La batie neuve ")
