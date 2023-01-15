import json
from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geoip2 import GeoIP2
import requests
import geoip2.webservice


api_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=97f889bc794743fbbbe29c2f582eee76'

def home(request):
    country, region, city, lat, lon, timezone = get_loc(request)

    get_weather = "https://api.open-meteo.com/v1/forecast?latitude="+str(lat)+"&longitude="+str(lon)+"&current_weather=True&hourly=temperature_2m&daily=weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset&timezone=auto"
    weather = requests.get(get_weather).json()  
    print(weather)
    daily = weather['daily']
    
    context = {'country':country, 'region':region, 'city':city, 'weather': weather, 'timezone':timezone,
        'time': daily['time'], 'min_temp': daily['temperature_2m_min'], 'max_temp': daily['temperature_2m_max'],
        'current_weather': weather['current_weather'], 'weather_type': daily['weathercode']
    }

    return render(request, 'main/index.html', context)

def get_loc(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]

    else:
        ip = request.META.get('REMOTE_ADDR')

    

    geolocation_json = get_geolocation_data(ip)
    geolocation_data = json.loads(geolocation_json)
    country = geolocation_data['country']
    region = geolocation_data['region']
    city = geolocation_data['city']
    lat = geolocation_data['latitude']
    lon = geolocation_data['longitude']
    time = geolocation_data['timezone']

    return country, region, city, lat, lon, time

def get_geolocation_data(ip):
    response = requests.get(api_url)
    
    return response.content
