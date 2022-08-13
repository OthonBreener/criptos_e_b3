from asyncio import run, gather # gather executa varias corritinas ao mesmo tempo
from httpx import AsyncClient, get
from decoradores import medir_tempo, medir_tempo_assincrono
from entidades import Cripto

#@medir_tempo
#def buscar_todas_as_criptos_da_coingecko():
#
#    criptos = get('https://api.coingecko.com/api/v3/coins/list')
#
#    return criptos.json()
#
#buscar_todas_as_criptos_da_coingecko()


minhas_criptos_ids = [
    'bitcoin', 'ethereum'
]

@medir_tempo_assincrono
async def buscar_todas_as_criptos_da_coingecko_assincrono():

    async with AsyncClient() as client:
        lista_de_criptos = await client.get('https://api.coingecko.com/api/v3/coins/list')

    return lista_de_criptos.json()

lista_de_criptos = run(buscar_todas_as_criptos_da_coingecko_assincrono())


@medir_tempo_assincrono
async def buscar_cripto_por_nome(
    id: str, 
    valor_em_moedas: str = 'usd,brl',
    incluir_mudancas_em_24hrs: str = 'true', 
):

    url = (
        f'https://api.coingecko.com/api/v3/simple/price?ids={id}&vs_currencies='
        f'{valor_em_moedas}&include_24hr_change={incluir_mudancas_em_24hrs}'
    )

    async with AsyncClient() as client:
        cripto = await client.get(url)

    return cripto.json()


@medir_tempo_assincrono
async def buscar_cripto_por_id(id: str):

    url = f'https://api.coingecko.com/api/v3/coins/{id}'

    async with AsyncClient() as client:
        cripto = await client.get(url)

    return cripto.json()


def montar_objeto_com_dados():

    for cripto_id in minhas_criptos_ids:
        dados = run(buscar_cripto_por_id(cripto_id))

        market_data = dados.get('market_data')
        preco_atual = market_data.get('current_price')
        alta_historica = market_data.get('ath')
        alta_historica_data = market_data.get('ath_date')
        porcentagem_de_alteracao_ath = market_data.get('ath_change_percentage')
        baixa_historica = market_data.get('atl')
        baixa_historica_data = market_data.get('atl_date')
        porcentagem_de_alteracao_atl = market_data.get('atl_change_percentage')
        captalizacao_de_mercado = market_data.get('market_cap')
        rank_de_captalizacao = market_data.get('market_cap_rank')
        captalizacao_de_mercado_tdiluida = market_data.get('fully_diluted_valuation')
        volume_total = market_data.get('total_volume')
        alta_de_24h = market_data.get('high_24h')
        baixa_de_24h = market_data.get('low_24h')

        mundanca_de_preco_em_24h = market_data.get('price_change_24h_in_currency')
        percentual_de_mudanca_de_preco_24h = market_data.get('price_change_percentage_24h_in_currency')
        percentual_de_mudanca_de_preco_7d = market_data.get('price_change_percentage_7d_in_currency')
        percentual_de_mudanca_de_preco_14d = market_data.get('price_change_percentage_14d_in_currency')
        percentual_de_mudanca_de_preco_30d = market_data.get('price_change_percentage_30d_in_currency')
        percentual_de_mudanca_de_preco_60d = market_data.get('price_change_percentage_60d_in_currency')
        percentual_de_mudanca_de_preco_1a = market_data.get('price_change_percentage_1y_in_currency')
        fornecimento_total = market_data.get('total_supply')
        fornecimento_maximo = market_data.get('max_supply')
        fornecimento_circulante = market_data.get('circulating_supply')
        ultima_atualizacao_dos_precos = market_data.get('last_updated')
        sparkline_7d_usd = market_data.get('sparkline_7d').get('price')


        yield Cripto.criar_novo(
            id = dados.get('id'),
            nome = dados.get('nome'),
            simbolo = dados.get('symbol'),
            valor_usd = preco_atual.get('usd'),
            valor_brl = preco_atual.get('brl'),
            alta_historica_usd = alta_historica.get('usd'),
            alta_historica_brl = alta_historica.get('brl'),
            data_alta_historico_usd = alta_historica_data.get('usd'),
            data_alta_historico_brl = alta_historica_data.get('brl'),
            porcentagem_de_alteracao_ath_usd = porcentagem_de_alteracao_ath.get('usd'),
            porcentagem_de_alteracao_ath_brl = porcentagem_de_alteracao_ath.get('brl'),
            baixa_historica_usd = baixa_historica.get('usd'),
            baixa_historica_brl = baixa_historica.get('brl'),
            data_baixa_historico_usd = baixa_historica_data.get('usd'),
            data_baixa_historico_brl = baixa_historica_data.get('brl'),
            porcentagem_de_alteracao_atl_usd = porcentagem_de_alteracao_atl.get('usd'),
            porcentagem_de_alteracao_atl_brl = porcentagem_de_alteracao_atl.get('brl'),
            captalizacao_de_mercado_usd = captalizacao_de_mercado.get('usd'),
            captalizacao_de_mercado_brl = captalizacao_de_mercado.get('brl'),
            rank_de_captalizacao = rank_de_captalizacao,
            captalizacao_de_mercado_tdiluida_usd = captalizacao_de_mercado_tdiluida.get('usd'),
            captalizacao_de_mercado_tdiluida_brl = captalizacao_de_mercado_tdiluida.get('brl'),
            volume_total_usd = volume_total.get('usd'),
            volume_total_brl = volume_total.get('brl'),
            alta_de_24h_usd = alta_de_24h.get('usd'),
            alta_de_24h_brl = alta_de_24h.get('brl'),
            baixa_de_24h_usd = baixa_de_24h.get('usd'),
            baixa_de_24h_brl = baixa_de_24h.get('brl'),
            mundanca_de_preco_em_24h_usd = mundanca_de_preco_em_24h.get('usd'),
            mundanca_de_preco_em_24h_brl = mundanca_de_preco_em_24h.get('brl'),
            percentual_de_mudanca_de_preco_24h_usd = percentual_de_mudanca_de_preco_24h.get('usd'),
            percentual_de_mudanca_de_preco_24h_brl = percentual_de_mudanca_de_preco_24h.get('brl'),
            percentual_de_mudanca_de_preco_7d_usd = percentual_de_mudanca_de_preco_7d.get('usd'),
            percentual_de_mudanca_de_preco_7d_brl = percentual_de_mudanca_de_preco_7d.get('brl'),
            percentual_de_mudanca_de_preco_14d_usd = percentual_de_mudanca_de_preco_14d.get('usd'),
            percentual_de_mudanca_de_preco_14d_brl = percentual_de_mudanca_de_preco_14d.get('brl'),
            percentual_de_mudanca_de_preco_30d_usd = percentual_de_mudanca_de_preco_30d.get('usd'),
            percentual_de_mudanca_de_preco_30d_brl = percentual_de_mudanca_de_preco_30d.get('brl'),
            percentual_de_mudanca_de_preco_60d_usd = percentual_de_mudanca_de_preco_60d.get('usd'),
            percentual_de_mudanca_de_preco_60d_brl = percentual_de_mudanca_de_preco_60d.get('brl'),
            percentual_de_mudanca_de_preco_1a_usd = percentual_de_mudanca_de_preco_1a.get('usd'),
            percentual_de_mudanca_de_preco_1a_brl = percentual_de_mudanca_de_preco_1a.get('brl'),
            fornecimento_total = fornecimento_total,
            fornecimento_maximo = fornecimento_maximo,
            fornecimento_circulante = fornecimento_circulante,
            ultima_atualizacao_dos_precos = ultima_atualizacao_dos_precos,
            sparkline_7d_usd = sparkline_7d_usd,
        )

'''
Para fazer o gráfico:

import matplotlib.plyplot as plt
from numpy import linspace


coluna = cripto.sparkline_7d_usd
linha = np.linspace(1,7,len(coluna))

plt.plot(linha, coluna)
plt.show()
'''