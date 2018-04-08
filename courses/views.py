from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice
from .forms import ChoiceForm

from backend.UMDSchedule import *

def index(request):
    context = {}
    return render(request, 'courses/index.html', context)


def results(request):
    
    context = request.POST.getlist('choice')

    string=""
    for i in context:
        if i != "":
            if string == "":
                string=i
            else:
                string=string + ","+i
                

    answer = schedule(string)

    toReturn = []
    for i in answer:
        toReturn.append(i.get_section_id())
    return render(request, 'courses/results.html', {'context':toReturn})

