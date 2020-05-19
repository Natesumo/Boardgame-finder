from django.views.generic import TemplateView
from django.shortcuts import render
import requests

def index(request):
   response = requests.get('https://www.boardgameatlas.com/api/search?order_by=popularity&ascending=false&pretty=true&client_id=SB1VGnDv7M')
   api = response.json()
   gamedata = api['games']
   return render(request, 'index.html', { 'gamedata': gamedata })



def search(request):
   gamedata = None
   if request.POST.get('userinput'):
      text = request.POST.get('userinput')
      response = requests.get('https://www.boardgameatlas.com/api/search?name=%s&fuzzy_match=true&pretty=true&client_id=SB1VGnDv7M' % text)
      api = response.json()
      gamedata = api['games']
   try:
      return render(request, 'search.html', { 
         'gamedata': gamedata,
         'has_error': request.method == 'POST' and len(gamedata) == 0
      })
   except:
      # handle the error
      return render(request, 'search.html')
