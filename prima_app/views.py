from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,"homepage.html")

# Create your views here.
def welcome(request):
    return render(request,"welcome.html")

# Create your views here.
def lista(request):
    return render(request,"lista.html")