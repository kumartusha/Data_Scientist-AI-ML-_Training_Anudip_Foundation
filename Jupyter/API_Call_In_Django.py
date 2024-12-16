from django.shortcuts import render, HttpResponse
import requests

url = 'https://api.openweathermap.org/data/2.5/weather?units=metric&q=modinagar&appid=8909baa00324102632b4fde2baa4d5f9'
data = requests.get(url).json()

print(data)

payload = {
        'city': data['name'], 
        'weather': data['weather'][0]['main'],
        # 'icon': data['weather'][0]['icons'],
        'kelvin_temperature': data['main']['temp'],
        'celcius_temperature': data['main']['temp'] - 273,
        'pressure': data['main']['pressure'],
        'humidity': data['main']['humidity']
    }
    
context = {'data': payload}
print(context)    