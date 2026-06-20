from django.shortcuts import render
import datetime
import requests
# Create your views here.
def index(request):
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city='London'

    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=9baf5a8c9406829f176d84b6c468dce2'
    PARAMS= {'units':'metric'}
    data=requests.get(url, params=PARAMS).json()
    
    # Check if the API response is valid
    if 'weather' in data:
        description=data['weather'][0]['description']
        icon=data['weather'][0]['icon'] 
        temp=data['main']['temp']
    else:
        description='City not found'
        icon='N/A'
        temp='N/A'

    day=datetime.date.today()

    return render(request,'index.html',{'description':description,'icon':icon,'temp':temp,'day':day})  