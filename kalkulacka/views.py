from django.shortcuts import render

def index(request):
    if request.method == "GET":
        vysledok = 0
    if request.method == "POST":
        try:
            a = int(request.POST["a"])
            b = int(request.POST["b"])
            operator = request.POST["operator"]
        except ValueError:
            return render(request, 'kalkulacka/index.html', dict(vysledok="nespravne"))

        if operator == "+":
            vysledok = a + b
        elif operator == "-":
            vysledok = a - b
        elif operator == "*":
            vysledok = a * b
        else:
            if(b == 0):
                vysledok = "skus rozmyslat"
            else:
                vysledok = a / b
    return render(request, 'kalkulacka/index.html', dict(vysledok=vysledok))
