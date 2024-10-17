from django.shortcuts import render
from accounts.models import Task, User
def home(request):
    contex = {
        'tasks': Task.objects.all()
    }
    return render(request,'home.html', contex)
# Create your views here.
