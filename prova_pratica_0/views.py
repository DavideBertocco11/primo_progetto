from django.shortcuts import render

# Create your views here.
def index3(request):
    return render(request, "index3.html")

def somma(request):
    return render(request, "somma.html")

def media(request):
    return render(request, "media.html")
