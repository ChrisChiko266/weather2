from django import template

import datetime

# register template library
register = template.Library()

############################################
###### define weather icon variables #######
############################################

#cloudy and sunny
cs = "https://www.flaticon.com/free-icons/sky"

#clear night sky with stars
cnss = "https://www.flaticon.com/free-icons/sky"

#sun
s = "/static/services/images/weather/sun.png"

#night rain
nr = "https://www.flaticon.com/free-icons/jotta-cloud"

#rainy day
rd = "/static/services/images/weather/rain.png"

# storm
sr = "static/services/images/weather/storm.png"

# thunderstorm
thunder = "/static/services/images/weather/thunderstorm.jpg"

# blue sky
clear = "/static/services/images/weather/blue-sky.jpg"


@register.simple_tag
def date_days(indexable, i):
    print(indexable[i].split('-'))

    return indexable[i]

@register.simple_tag
def get_temperature(indexable, i):
    return round(indexable[i])

@register.simple_tag
def get_date(indexable, i):
    return format_date(indexable[i].split('-'))

def format_date(indexable):
    d = datetime.datetime(int(indexable[0]), int(indexable[1]), int(indexable[2]))

    return d.strftime("%A")

@register.simple_tag
def weather_forecast(indexable, i):
    if indexable[i] <= 3:
        return s 
    elif indexable[i] > 50 and indexable[i] < 68 or indexable[i] >= 80 and indexable[i] <= 82:
        return rd
    elif indexable[i] >= 95 and indexable[i] <= 99:
        return sr 
    else: 
        return 4

@register.simple_tag
def weather_code(indexable, i):
    if indexable[i] <= 3:
        return clear
    elif indexable[i] > 50 and indexable[i] < 68 or indexable[i] >= 80 and indexable[i] <= 82:
        return rd
    elif indexable[i] >= 95 and indexable[i] <= 99:
        return thunder
    else: 
        return 4
