import requests
import json

def weather_api(city):
    api_key = "78e9acc9499f954807ced63fa94dbe5f"
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = json.loads(response.text)
    results = {}
    results['lon'] = data['coord']['lon']
    results['lat'] = data['coord']['lat']
    results['area'] = data['name']
    results['visibility'] = data['visibility']
    results['temp'] = data['main']['temp']
    results['feels_like'] = data['main']['feels_like']
    results['humidity'] = data['main']['humidity']
    return results

print(weather_api('New York'))



