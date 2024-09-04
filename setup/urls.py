"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#from sala.views import informacoes_view
from sala.views import SalasListView, SalasCreateView , SalasUpdateView, SalasDeleteView, SalasListHomeView, home, SolicitarDadosView, EncerrarSessaoView


urlpatterns = [
    path('admin/', admin.site.urls),


    path('', home, name='inicio'),

    path('reserva/',  SalasListView.as_view(), name='reserva'),

    path('cadastro/', SalasCreateView.as_view(), name="reserva_list"),

    path('edicao/<int:pk>/', SalasUpdateView.as_view(), name='edicao'),

    path('delete/<int:pk>/', SalasDeleteView.as_view(), name='delete'),

    #sessoes
    path('sessao/', SolicitarDadosView.as_view(), name="reserva_section"),

    path('encerra_sessao/', EncerrarSessaoView.as_view(), name="reserva_section_fim")
]

