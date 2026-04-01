from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import *
# Create your views here.
def addtask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')
