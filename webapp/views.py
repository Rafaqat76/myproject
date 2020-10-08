from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,"webapp/home.html")


def property(request):
    return render(request, "webapp/property.html")


def homeloan(request):
    return render(request, "webapp/homeloan.html")


def personalloan(request):
    return render(request, "webapp/personal.html")


def businessloan(request):
    return render(request, "webapp/business.html")


def about(request):
    return render(request, "webapp/about.html")


def contact(request):
    return render(request, "webapp/contact.html")


def vehicle(request):
    return render(request, "webapp/vehicle.html")


def consulting(request):
    return render(request, "webapp/consulting.html")