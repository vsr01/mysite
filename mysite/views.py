from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    #return HttpResponse("Home Page")
    return render(request,'homepage.html')
def about(request):
    #return HttpResponse("About")
    return render(request,'about.html')