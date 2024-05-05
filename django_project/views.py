import requests
from django.shortcuts import render


def homepage(request):
  # USING APIS 
  response = requests.get('https://api.github.com/events')
  data = response.json()
  result = data [0]  ["repo"]

  # SECOND API
  response2 = requests.get('https://dog.ceo/api/breeds/image/random')
  data2 = response2.json()
  result2 = data2  ["message"]

  # # THIRD API
  # response3 = requests.get('https://api.thedogapi.com/v1/images/search')
  # data3 = response3.json()
  # result3 = data3  [0] ["url"]

  
  return render(request, 'templates/index.html', {'result': result, 'result2': result2})