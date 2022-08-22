from asyncio import run
from decoradores import medir_tempo, medir_tempo_assincrono
from entidades import Cripto
from api import buscar_cripto_por_id
import matplotlib.pyplot as plt
from numpy import linspace

minhas_criptos_ids = [
    'bitcoin', 'ethereum'
]


class ApiCoingecko:

    def __init__(self, moeda: str):
        self.moeda = moeda
        self.__buscar_dados_por_id = buscar_cripto_por_id
    
    def __montar_classe_com_dados_da_cripto(self, cripto_id: str) -> Cripto:

        requisicao = run(self.__buscar_dados_por_id(cripto_id))

        return Cripto.criar_novo(
            moeda = self.moeda,
            id = requisicao.get('id'),
            nome = requisicao.get('nome'),
            simbolo = requisicao.get('symbol'),
            market_data = requisicao.get('market_data')        
        )

    def _retornar_classe_cripto(self, cripto_id: str):

        return self.__montar_classe_com_dados_da_cripto(cripto_id)

    def buscar_todos_dados_de_uma_cripto_pelo_id(self, cripto_id: str):

        dados = self._retornar_classe_cripto(cripto_id)

        return dados.para_dicionario()

    #def montar_grafico_sparkline_7d(self, cripto_id: str):
    #
    #    dados = self._retornar_classe_cripto(cripto_id)
    #
    #    coluna = dados.sparkline_7d_usd
    #    linha = linspace(1,7,len(coluna))
    #    
    #    plt.plot(linha, coluna)
    #    plt.show()