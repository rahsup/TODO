from django.http import HttpResponse
from django.shortcuts import render
from todo.models import *
def home(request):
    task=Task.objects.filter(is_completed=False).order_by('-update_at')
    context={
        'task':task,
    }
    return render(request,'home.html',context )