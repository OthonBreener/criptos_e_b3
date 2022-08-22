from datetime import datetime
from dateparser import parse
from dataclasses import asdict, dataclass

@dataclass
class Cripto:
    '''
    A capitalização de mercado, ou Market Cap, é a quantidade de dinheiro que 
    custaria se você fosse comprar todas as ações emitidas de uma empresa ao 
    preço atual de mercado.

    Capitalização de mercado totalmente diluída (FDMC) = preço x fornecimento máximo. 
    Se o fornecimento máximo for nulo, FDMC = preço x fornecimento total. 
    Se o fornecimento máximo e o fornecimento total forem infinitos ou não 
    estiverem disponíveis, a capitalização de mercado totalmente diluída 
    será apresentada como - -.
    '''
    id: str
    simbolo: str
    nome: str
    valor: int
    alta_historica: int
    data_alta_historico: datetime
    porcentagem_de_alteracao_ath: float
    baixa_historica: int
    data_baixa_historico: datetime
    porcentagem_de_alteracao_atl: float
    captalizacao_de_mercado: int
    rank_de_captalizacao: int
    captalizacao_de_mercado_tdiluida: int
    volume_total: int
    alta_de_24h: int
    baixa_de_24h: int
    mundanca_de_preco_em_24h: int
    percentual_de_mudanca_de_preco_24h: int
    percentual_de_mudanca_de_preco_7d: int
    percentual_de_mudanca_de_preco_14d: int
    percentual_de_mudanca_de_preco_30d: int
    percentual_de_mudanca_de_preco_60d: int
    percentual_de_mudanca_de_preco_1a: int
    fornecimento_total: int
    fornecimento_maximo: int
    fornecimento_circulante: int
    ultima_atualizacao_dos_precos: datetime
    #sparkline_7d_usd: list[int]

    def __repr__(self) -> str:
        return f"Cripto(nome={self.nome}, id={self.id}, simbolo={self.simbolo})"

    def para_dicionario(self) -> dict[str, str | int | dict[str, int]]:
        return asdict(self)

    @classmethod
    def criar_novo(
        cls, moeda: str, market_data: dict[str, dict[str,str]], id: str, nome: str, simbolo: str
    ):
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
        #sparkline_7d_usd = market_data.get('sparkline_7d').get('price')

        alta_historica_data_datetime = parse(alta_historica_data.get(moeda))
        baixa_historica_data_datetime = parse(baixa_historica_data.get(moeda))
        ultima_atualizacao_dos_precos_datetime = parse(ultima_atualizacao_dos_precos)

        return cls(
            id=id, 
            nome=nome, 
            simbolo=simbolo,
            valor=preco_atual.get(moeda),
            alta_historica=alta_historica.get(moeda),
            data_alta_historico=alta_historica_data_datetime,
            porcentagem_de_alteracao_ath=porcentagem_de_alteracao_ath.get(moeda),
            baixa_historica=baixa_historica.get(moeda),
            data_baixa_historico=baixa_historica_data_datetime,
            porcentagem_de_alteracao_atl=porcentagem_de_alteracao_atl.get(moeda),
            captalizacao_de_mercado=captalizacao_de_mercado.get(moeda),
            captalizacao_de_mercado_tdiluida=captalizacao_de_mercado_tdiluida.get(moeda),
            volume_total=volume_total.get(moeda),
            alta_de_24h=alta_de_24h.get(moeda),
            baixa_de_24h=baixa_de_24h.get(moeda),
            mundanca_de_preco_em_24h=mundanca_de_preco_em_24h.get(moeda),
            percentual_de_mudanca_de_preco_24h=percentual_de_mudanca_de_preco_24h.get(moeda),
            percentual_de_mudanca_de_preco_7d=percentual_de_mudanca_de_preco_7d.get(moeda),
            percentual_de_mudanca_de_preco_14d=percentual_de_mudanca_de_preco_14d.get(moeda),
            percentual_de_mudanca_de_preco_30d=percentual_de_mudanca_de_preco_30d.get(moeda),
            percentual_de_mudanca_de_preco_60d=percentual_de_mudanca_de_preco_60d.get(moeda),
            percentual_de_mudanca_de_preco_1a=percentual_de_mudanca_de_preco_1a.get(moeda),
            rank_de_captalizacao=rank_de_captalizacao,
            fornecimento_total=fornecimento_total,
            fornecimento_maximo=fornecimento_maximo,
            fornecimento_circulante=fornecimento_circulante,
            ultima_atualizacao_dos_precos=ultima_atualizacao_dos_precos_datetime,
            #sparkline_7d_usd=sparkline_7d_usd,
        )
