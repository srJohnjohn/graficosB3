from multiprocessing import get_context
from tracemalloc import start
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Acao
import logging
logins = logging.getLogger('django')


# Create your views here.

class AcoesView(ListView):
    model = Acao
    template_name = 'Acoes/grafico.html'
    

    def get_context_data(self, **kwargs):
        lista_acoes = []
        tabale_empresas = pd.read_csv("Empresas.csv")
        for empresa in tabale_empresas.itertuples():
            lista_acoes.append(empresa.Codigo)
        context = super().get_context_data(**kwargs)
        context['acoes'] = lista_acoes
        self.object_list = Acao.objects.filter(codigo=self.kwargs['codigo']) #refatorar
        context['nome'] =  self.object_list.first().nome
        
        logins.info(f'buscando dados da acao {self.object_list.first().nome} no banco')
        return context

    def get_queryset(self):
        self.object_list = Acao.objects.filter(codigo=self.kwargs['codigo']) #refatorar
        
        return self.object_list
    
    
class IndexView(ListView):
    model = Acao
    template_name = 'Acoes/grafico.html'

    def get_context_data(self, **kwargs):
        logins.info('buscando dados da acao Ibovespa no banco')
        lista_acoes = []
        tabale_empresas = pd.read_csv("Empresas.csv")
        for empresa in tabale_empresas.itertuples():
            lista_acoes.append(empresa.Codigo)
        context = super().get_context_data(**kwargs)
        
        context['acoes'] = lista_acoes
        context['nome'] =  "Ibovespa"
        return context
    
    def get_queryset(self):
        self.object_list = Acao.objects.filter(codigo='BVSP')
        return self.object_list


class AtualizarAcao(DetailView):
    model = Acao
    template_name = ''

    
    
        