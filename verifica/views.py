from django.shortcuts import render

def view_a(request):
    materie = ["Matematica","Italiano","Inglese","Storia","Geografia"]
    context = {
        'materie' : materie
    }
    return render(request, "view_a.html", context)

def view_b(request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    studenti1 = []
    studenti2 = []
    studenti3 = []

    for i in range (0, 4):
        studenti1.append(voti['Giuseppe Gullo'][i])
    for i in range (0, 4):
        studenti2.append(voti['Antonio Barbera'][i])
    for i in range (0, 4):
        studenti3.append(voti['Nicola Spina'][i])
     
    context= {
        'studenti1': studenti1,
        'studenti2': studenti2,
        'studenti3': studenti3,
    }
    return render(request, "view_b.html", context)

def view_c(request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    
    media = 0

    dati1 = voti['Giuseppe Gullo']
    dati2 = voti['Antonio Barbera']
    dati3 = voti['Nicola Spina']

    for dato in dati1:
        media += dato[1]
        media1 = media/len(dati1)

    media = 0

    for dato in dati2:
        media += dato[1]
        media2 = media/len(dati2)

    media = 0

    for dato in dati3:
        media += dato[1]
        media3 = media/len(dati3)

    context= {
        'media1': media1,
        'media2': media2,
        'media3': media3
    }
    return render(request, "view_c.html", context)
