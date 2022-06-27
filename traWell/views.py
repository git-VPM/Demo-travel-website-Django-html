from django.shortcuts import render, HttpResponse
from .models import destinations
# Create your views here.

def tra(request):
    des = destinations.objects.all()
    return render(request, 'index.html',{'dest':des})