from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView, CreateView , UpdateView , DeleteView

from.models import Reserva

from django.urls import reverse_lazy
# Create your views here.

# lista de dicionarios onde contem as informacoes , simulacao de bd
"""def informacoes_view(request):
    sala = [
    {'sala' :'01', 'categoria' : 'Ação', 'Filme':'missao impossivel', 'data': '11/05/2024', 'horario': '2h30', 'responsavel': 'Jurandir', 'email': 'jurandir@gmail.com'},
    {'sala': '01', 'categoria': 'Ação', 'Filme': 'missao impossivel', 'data': '11/05/2024', 'horario': '2h30','responsavel': 'Jurandir', 'email': 'jurandir@gmail.com'},
    {'sala' :'01', 'categoria' : 'Ação', 'Filme':'missao impossivel', 'data': '11/05/2024', 'horario': '2h30', 'responsavel': 'Jurandir', 'email': 'jurandir@gmail.com'},
    {'sala' :'01', 'categoria' : 'Ação', 'Filme':'missao impossivel', 'data': '11/05/2024', 'horario': '2h30', 'responsavel': 'Jurandir', 'email': 'jurandir@gmail.com'}]"""

class SalasListView(ListView):
    model = Reserva


class SalasCreateView(CreateView):
    model = Reserva

    #campos de preenchimento
    fields = [ "sala" , "categoria", "filme", "data", "horario", "nome_responsavel", "email"]

    success_url = reverse_lazy('reserva')
# return render(request, 'sala/reserva_list.html',{'dados': sala})


class SalasUpdateView(UpdateView):
    model = Reserva
    fields = ["sala", "categoria", "filme", "data", "horario", "nome_responsavel", "email"]
    template_name = 'sala/reserva_form.html'
    success_url = reverse_lazy('reserva')

class SalasDeleteView(DeleteView):
    model = Reserva
    fields = ["sala", "categoria", "filme", "data", "horario", "nome_responsavel", "email"]
    template_name = 'sala/reserva_form.html'
    success_url = reverse_lazy('reserva')


