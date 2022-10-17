from django.shortcuts import render

def index_generale(request):
    return render(request, "index_generale.html")

def base(request):
    return render(request, "base.html")