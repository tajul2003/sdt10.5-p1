from django.shortcuts import render
import datetime
# import TIME_FORMAT
# Create your views here.
def home(request):
      
    d ={
        'number': '',
        'title': "<p>You are <em>pretty</em> smart!</p>",
        'dict': [
    {'name': 'zed', 'age': 19},
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31},
],
        'empty':'',
        'value': datetime.datetime.now(),
        'name':'Hello I am Tajul',
        'age': 4,
        'Live':'Dhaka',
        'courses':['phitron','pHero','Ostad'],
        'learning':[
        {
            'id':1,
            'name':'python',
            'fee': 5000
        },
        {
            'id':2,
            'name':'Django',
            'fee': 10000
        },
        {
            'id':3,
            'name':'C',
            'fee': 1000
        }
    ]
    }
    return render(request, 'home.html',d)