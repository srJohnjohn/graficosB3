from tracemalloc import start
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from pandas_datareader import data as dados
import pandas as pd
import datetime
from .models import Acao
## biblioteca para plotar graficos

# Create your views here.

class AcoesView(ListView):
    model = Acao
    template_name = 'Acoes/grafico.html'
    #paginate_by = 25

    def get_queryset(self):
        self.object_list = Acao.objects.filter(nome='NomeAcao') #refatorar
        return self.object_list
    
    
# class AtualizarAcao(DetailView):
#     model = Acao
#     template_name = ''

    
    # ibovespa = ^BVSP
class IndexView(ListView):
    model = Acao
    template_name = 'Acoes/grafico.html'

    # cotacao_ibovespa = dados.DataReader('^BVSP', data_source='yahoo', start='01/01/2020', end='01/01/2021') #[High, Low, Open, Close, Volume, Adj Close, date]
    
    # print("ibov modificado")
    # ### editando o data table, para a data se torna um indice
    # modibov = cotacao_ibovespa.reset_index()
    # for d in modibov.itertuples():
    #     print('objeto d')
    #     print(d.Date.date())
    #     print('..................')
    #     #acao_dia = datetime.datetime.strptime(d["Date"], '%Y-%m-%d')
    #     ibov = Acao(
    #             nome='Ibovespa',
    #             codigo='BVSP',
    #             dia=d.Date.date(),
    #             high=d.High,
    #             low=d.Low,
    #             open=d.Open,
    #             close=d.Close,
    #             volume=d.Volume,
    #             adj_close=d[7],
    #             )

    #     ibov.save()
    # # tabela empresas 
    # tabale_empresas = pd.read_csv("Empresas.csv")
    # print("começando a ler dados das empresas")
    # for empresa in tabale_empresas.itertuples():
    #     print(empresa.Codigo)
    #     cotacao = dados.DataReader(empresa.Codigo + '.SA', data_source='yahoo', start='01/01/2020', end='01/01/2021')
    #     modimpresas = cotacao.reset_index()
    #     for d in modimpresas.itertuples():
    #         print(d.Date.date())
    #         q = Acao(
    #                 nome=empresa.Nome,
    #                 codigo=empresa.Codigo,
    #                 dia=d.Date.date(),
    #                 high=d.High,
    #                 low=d.Low,
    #                 open=d.Open,
    #                 close=d.Close,
    #                 volume=d.Volume,
    #                 adj_close=d[7],
    #                 )
    #         q.save()
            
    def get_queryset(self):
        self.object_list = Acao.objects.filter(codigo='BVSP')
        return self.object_list
        