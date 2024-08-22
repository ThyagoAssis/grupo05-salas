from django.shortcuts import render


def home(request):
    return render(request, "reserva/reserva.html")
# Create your views here.
