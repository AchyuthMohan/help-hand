from django.shortcuts import render

# Create your views here.
def menu(request):
    return render(request,"menu.html")

def ambulance(request):
    return render(request,"ambulance.html")

def medicines(request):
    return render(request,"medicines.html")

def blood(request):
    return render(request,"blood.html")

def homeassis(request):
    return render(request,"homeassis.html")

def others(request):
    return render(request,"others.html")
