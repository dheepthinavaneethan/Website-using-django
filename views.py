from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html')

def aboutus(request):
    return render(request, 'myapp/aboutus.html')

def contactus(request):
    return render(request, 'myapp/contactus.html')
