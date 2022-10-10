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

def variabili(request):
    context = {
        'var1':'Prima variabile',
        'var2':'Seconda variabile',
        'var3':'Terza variabile',
    }
    return render(request, "variabili.html", context)
def chi_siamo(request):
    return render(request, "chi_siamo.html")
    
def index(request):
    return render(request, "index.html")