from django.shortcuts import render

def index(request):
    if request.method == "GET":
        odpoved = 0
    if request.method == "POST":
        try:
            a = int(request.POST["a"])
            b = int(request.POST["b"])
        except ValueError:
            return render(request, 'cisla/index.html', dict(odpoved="nespravne"))
        if(a>b):
            odpoved = "Vacsie cislo je A"
        elif(a>b):
            odpoved = "Vacsie cislo je A"
        else:
            odpoved = "Cisla sa rovnaju"
    return render(request, 'cisla/index.html', dict(odpoved=odpoved))

def parne(cislo):
    if(cislo % 2 == 0):
        return "Parne"
    else:
        return "Neparne"
    
#def prvoCislo(cislo):