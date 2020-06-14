from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
import requests

def index(request):
    #url = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=1792447a7964370f854923bf80522be8&lat=37.487662&lon=126.976915'

    city = request.GET.get('city')
    url = 'http://api.openweathermap.org/data/2.5/weather?q='+ city +'&appid=1792447a7964370f854923bf80522be8'

    # return JsonResponse({'city':city})

    resp = requests.get(url=url, params=dict())
    data = resp.json() # Check the JSON Response Content documentation below

    return JsonResponse(data)

    # return JsonResponse({'key':'value'})


