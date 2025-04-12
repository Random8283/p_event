from django.shortcuts import render, loader
from django.http import HttpResponse
from .models import Events

# Create your views here.

def events_list(request):
    template=loader.get_template('event/events_list.html')
    events = Events.object.all()
    context = {'events':events}
    return HttpResponse(template.render(context,request))

