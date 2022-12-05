from django.shortcuts import render, get_object_or_404
from .models import Articolo, Giornalista
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.


# def home(request):
#     a = ""   tramite il += concateniamo i vari articoli e giornalisti
#     g = ""   e li stampiamo
#     for art in Articolo.objects.all():
#         a += (art.titolo + "<br>")

#     for gio in Giornalista.objects.all():
#         g += (gio.nome + "<br>")
#     response = "articoli:<br>" + a + "<br>Giornalisti:<br>" + g

#     return HttpResponse("<h1>" + response + "</h1>")

# def home(request):
#     a = []  possiamo creare una lista degli articoli e giornalisti
#     g = []  all'interno di un vettore
#     for art in Articolo.objects.all():
#         a.append(art.titolo)

#     for gio in Giornalista.objects.all():
#         g.append(gio.nome)

#     response = str(a) + "<br>" + str(g)
#     print(response)

#     return HttpResponse("<h1>" + response + "</h1>")

def home (request):
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {"articoli": articoli, "giornaisti": giornalisti}
    print(context)
    return render(request, "articoli.html", context)

def articoloDetailView(request, pk):
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {"articolo": articolo}
    return render(request, "articolo_detail.html", context)

class articoloDetailViewCB(DetailView):
    model = Articolo
    template_name = "articolo_detail.html"

class articoloListView(ListView):
    model = Articolo
    template_name = "lista_articoli.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articoli"] = Articolo.objects.all()
        return context

class GiornalistaDetailViewCB(DetailView):
    model = Articolo
    template_name = "giornalista_detail.html"

class GiornalistaListView(ListView):
    model = Articolo
    template_name = "lista_giornalisti.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articoli"] = Articolo.objects.all()
        return context