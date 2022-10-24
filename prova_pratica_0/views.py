from django.shortcuts import render

def index_3(request):
    return render(request, "index_3.html")

def maxmin(request):
    import random
    var1 = random.randint(0, 10)
    var2 = random.randint(0, 10)
    context = {
        'var1' : var1,
        'var2' : var2,
        'somma' : var1 + var2,
    }
    return render(request, "maxmin.html", context)

def media(request):
    return render(request, "media.html")
