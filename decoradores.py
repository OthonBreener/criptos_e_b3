from functools import wraps
from time import time

def medir_tempo(funcao):

    @wraps(funcao)
    def medidor(*args, **kwargs):

        tempo_inicial = time()

        resultado = funcao(*args, **kwargs)
        nome_da_funcao = funcao.__name__

        tempo_decorrido = time() - tempo_inicial

        print(f'[{tempo_decorrido:0.8f}s] {nome_da_funcao}')

        return resultado
    
    return medidor


def medir_tempo_assincrono(funcao):

    @wraps(funcao)
    async def medidor(*args, **kwargs):

        tempo_inicial = time()

        resultado = await funcao(*args, **kwargs)
        nome_da_funcao = funcao.__name__

        tempo_decorrido = time() - tempo_inicial

        print(f'[{tempo_decorrido:0.8f}s] {nome_da_funcao}')

        return resultado
    
    return medidor