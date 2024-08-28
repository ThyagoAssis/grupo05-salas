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

# criacao do classe listview para exibição dos dados
class SalasListView(ListView):
    model = Reserva

# criacao da classe CreateView para cadastro dos dados
class SalasCreateView(CreateView):
    model = Reserva

    #campos de preenchimento
    fields = [ "sala" , "categoria", "filme", "data", "horario", "nome_responsavel", "email"]

    success_url = reverse_lazy('reserva')
# return render(request, 'sala/reserva_list.html',{'dados': sala})

# criacao da classe UpdateView para atualização dos dados
class SalasUpdateView(UpdateView):
    model = Reserva
    fields = ["sala", "categoria", "filme", "data", "horario", "nome_responsavel", "email"]
    template_name = 'sala/reserva_form.html'
    success_url = reverse_lazy('reserva')

# criacao da classe DeleteView para apagar os dados
class SalasDeleteView(DeleteView):
    model = Reserva
    fields = ["sala", "categoria", "filme", "data", "horario", "nome_responsavel", "email"]
    template_name = 'sala/reserva_form.html'
    success_url = reverse_lazy('reserva')

# criacao de classe para exibir a tela de inicio
class SalasListHomeView(ListView):
    model = Reserva
    succes_url = reverse_lazy('inicio')


def home(request):
    home = [ ('https://s2-gshow.glbimg.com/oQQhnGcszJuBbQcmLGrQ4dQ8MWE=/1200x/smart/filters:cover():strip_icc()/i.s3.glbimg.com/v1/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2024/D/J/fxLH8uRy2EpWUdAaASSg/marvelbrasil-449856715-1042043654208676-4375915367499994888-n.jpg',('DeadPool & Wolverine')),


    ]
    return render(request, 'sala/reserva_home.html' )