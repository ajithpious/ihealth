from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
import plotly.express as px

# https://industrial.api.ubidots.com/api/v1.6/devices/esp32/var/values/?page_size=10&token=BBFF-Bfw8lO95m9pzKw8zE0Zupzw5OrKDQ0
import requests


def home(request):
    return render(request,"home.html")
def patients(request):
    return render(request,"patients.html")
def patient(request):
    url="https://industrial.api.ubidots.com/api/v1.6/devices/esp32/var/values/"
    params={"page_size":100,"token":"BBFF-Bfw8lO95m9pzKw8zE0Zupzw5OrKDQ0"}
    r = requests.get(url = url, params = params)
    data = r.json()
    results=data['results']
    time=float(results[0]['created_at']/1000)
    dt_object = datetime.fromtimestamp(time)
    values=[]
    time=[]
    for result in results:
        values.append(result['value'])
        a=float(result["created_at"]/1000)
        date=datetime.fromtimestamp(a)
        time.append(date)
    fig=px.line(x=time,y=values,labels={"x":"time","y":"Body Temparature"})
    graph=fig.to_html()
    context={"graph":graph}
    return render(request,"patient.html",context=context)
def getdata(request):
    url="https://industrial.api.ubidots.com/api/v1.6/devices/esp32/temp/values/"
    params={"page_size":1,"token":"BBFF-Bfw8lO95m9pzKw8zE0Zupzw5OrKDQ0"}
    r = requests.get(url = url, params = params)
    return HttpResponse(r,content_type="application/json")
