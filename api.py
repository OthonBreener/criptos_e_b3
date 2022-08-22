from httpx import AsyncClient, get
from decoradores import medir_tempo, medir_tempo_assincrono


@medir_tempo
def buscar_todas_as_criptos_da_coingecko():

    criptos = get('https://api.coingecko.com/api/v3/coins/list')

    return criptos.json()


@medir_tempo_assincrono
async def buscar_todas_as_criptos_da_coingecko_assincrono():

    async with AsyncClient() as client:
        lista_de_criptos = await client.get('https://api.coingecko.com/api/v3/coins/list')

    return lista_de_criptos.json()


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