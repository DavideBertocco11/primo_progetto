#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Articolo, Giornalista
# Create your views here.
def home(request):
    #a = ""
    #g = ""

    #a = []
    #g = []

    #for art in Articolo.objects.all():
        #a += (art.titolo + "<br>")

        #a.append(art.titolo)

    #for gio in Giornalista.objects.all():
        #g += (gio.nome + "<br>")

        #g.append(gio.nome)

    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {"articoli": articoli, "giornalisti": giornalisti}
    print(context)
    return render(request, "homepage.html", context)

    #response = "Articoli:<br>" + a + "<br>Giornalisti<br>" + g

    #response = str(a) + "<br>" + str(g)
    #print(response)

    #return HttpResponse("<h1>" + response + "</h1>")

def articoloDetailView(request, pk):
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {"articolo": articolo}
    return render(request, "articolo_detail.html", context)