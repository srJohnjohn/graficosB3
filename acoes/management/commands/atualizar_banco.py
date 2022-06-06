from cgitb import handler
from django.core.management.base import BaseCommand
from pandas_datareader import data as dados
import pandas as pd
import datetime
import time
from acoes.models import Acao

class Command(BaseCommand):

    def handle(self, *args, **options):
        

        help = 'buscando dado do ibovespa'    
        #ibovespa = '^BVSP'
        

        cotacao_ibovespa = dados.DataReader('^BVSP', data_source='yahoo', start=(datetime.datetime.now() - datetime.timedelta(hours=24)).date(), end=datetime.datetime.now().date()) #[High, Low, Open, Close, Volume, Adj Close, date]
        
        print("ibov modificado")
        ### editando o data table, para a data se torna um indice
        modibov = cotacao_ibovespa.reset_index()
        for d in modibov.itertuples():
            print('objeto d')
            print(d.Date.date())
            print('..................')
            #acao_dia = datetime.datetime.strptime(d["Date"], '%Y-%m-%d')
            ibov = Acao(
                    nome='Ibovespa',
                    codigo='BVSP',
                    dia=d.Date.date(),
                    high=d.High,
                    low=d.Low,
                    open=d.Open,
                    close=d.Close,
                    volume=d.Volume,
                    adj_close=d[7],
                    )

            ibov.save()
        #tabela empresas 
        print("começando a ler dados das empresas")
        tabale_empresas = pd.read_csv("Empresas.csv")
        for empresa in tabale_empresas.itertuples():
            print(empresa.Codigo)
            cotacao = dados.DataReader(f'{empresa.Codigo}.SA', data_source='yahoo', start=(datetime.datetime.now() - datetime.timedelta(hours=24)).date(), end=datetime.datetime.now().date())
            modimpresas = cotacao.reset_index()
            for d in modimpresas.itertuples():
                print(d.Date.date())
                q = Acao(
                        nome=empresa.Nome,
                        codigo=empresa.Codigo,
                        dia=d.Date.date(),
                        high=d.High,
                        low=d.Low,
                        open=d.Open,
                        close=d.Close,
                        volume=d.Volume,
                        adj_close=d[7],
                        )
                q.save()
                