from django.shortcuts import render

# Create your views here.

def home(request):
    import requests
    import json

    news_api= requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=3fd6a63fde8e43c49c8e276ece90c27d")
    api= json.loads(news_api.content)
    return render(request, 'home.html', {'api':api})