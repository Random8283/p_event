from django.shortcuts import render, loader
from django.http import HttpResponse
from .models import Events

# Create your views here.

def events_list(request):
    events = Events.objects.all()
    return render(request,'event/events_list.html',{'events': events})