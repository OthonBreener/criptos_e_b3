from dataclasses import dataclass
from datetime import datetime


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
    valor_usd: int
    valor_brl: int
    alta_historica_usd: int
    alta_historica_brl: int
    data_alta_historico_usd: datetime
    data_alta_historico_brl: datetime
    porcentagem_de_alteracao_ath_usd: float
    porcentagem_de_alteracao_ath_brl: float
    baixa_historica_usd: int
    baixa_historica_brl: int
    data_baixa_historico_usd: datetime
    data_baixa_historico_brl: datetime    
    porcentagem_de_alteracao_atl_usd: float
    porcentagem_de_alteracao_atl_brl: float
    captalizacao_de_mercado_usd: int
    captalizacao_de_mercado_brl: int
    rank_de_captalizacao: int
    captalizacao_de_mercado_tdiluida_usd: int
    captalizacao_de_mercado_tdiluida_brl: int
    volume_total_usd: int
    volume_total_brl: int
    alta_de_24h_usd: int
    alta_de_24h_brl: int
    baixa_de_24h_usd: int
    baixa_de_24h_brl: int
    mundanca_de_preco_em_24h_usd: int
    mundanca_de_preco_em_24h_brl: int
    percentual_de_mudanca_de_preco_24h_usd: int
    percentual_de_mudanca_de_preco_24h_brl: int
    percentual_de_mudanca_de_preco_7d_usd: int
    percentual_de_mudanca_de_preco_7d_brl: int
    percentual_de_mudanca_de_preco_14d_usd: int
    percentual_de_mudanca_de_preco_14d_brl: int
    percentual_de_mudanca_de_preco_30d_usd: int
    percentual_de_mudanca_de_preco_30d_brl: int
    percentual_de_mudanca_de_preco_60d_usd: int
    percentual_de_mudanca_de_preco_60d_brl: int
    percentual_de_mudanca_de_preco_1a_usd: int
    percentual_de_mudanca_de_preco_1a_brl: int
    fornecimento_total: int
    fornecimento_maximo: int
    fornecimento_circulante: int
    ultima_atualizacao_dos_precos: datetime
    sparkline_7d_usd: list[int]

    @classmethod
    def criar_novo(
        cls, 
        id, 
        simbolo, 
        nome, 
        valor_usd, 
        valor_brl,
        alta_historica_usd,
        alta_historica_brl,
        data_alta_historico_usd,
        data_alta_historico_brl,
        porcentagem_de_alteracao_ath_usd,
        porcentagem_de_alteracao_ath_brl,
        baixa_historica_usd,
        baixa_historica_brl,
        baixa_historica_data_usd,
        baixa_historica_data_brl,
        porcentagem_de_alteracao_atl_usd,
        porcentagem_de_alteracao_atl_brl,
        captalizacao_de_mercado_usd,
        captalizacao_de_mercado_brl,
        rank_de_captalizacao,
        captalizacao_de_mercado_tdiluida_usd,
        captalizacao_de_mercado_tdiluida_brl,
        data_baixa_historico_usd,
        data_baixa_historico_brl,
        volume_total_usd,
        volume_total_brl,
        alta_de_24h_usd,
        alta_de_24h_brl,
        baixa_de_24h_usd,
        baixa_de_24h_brl,
        mundanca_de_preco_em_24h_usd,
        mundanca_de_preco_em_24h_brl,
        percentual_de_mudanca_de_preco_24h_usd,
        percentual_de_mudanca_de_preco_24h_brl,
        percentual_de_mudanca_de_preco_7d_usd,
        percentual_de_mudanca_de_preco_7d_brl,
        percentual_de_mudanca_de_preco_14d_usd,
        percentual_de_mudanca_de_preco_14d_brl,
        percentual_de_mudanca_de_preco_30d_usd,
        percentual_de_mudanca_de_preco_30d_brl,
        percentual_de_mudanca_de_preco_60d_usd,
        percentual_de_mudanca_de_preco_60d_brl,
        percentual_de_mudanca_de_preco_1a_usd,
        percentual_de_mudanca_de_preco_1a_brl,
        fornecimento_total,
        fornecimento_maximo,
        fornecimento_circulante,
        ultima_atualizacao_dos_precos,
        sparkline_7d_usd,
    ):
        data_alta_historico_usd
        data_alta_historico_brl
        data_baixa_historico_usd
        data_baixa_historico_brl
        ultima_atualizacao_dos_precos

        return cls(
            id=id, 
            nome=nome, 
            simbolo=simbolo,
            valor_usd=valor_usd,
            valor_brl=valor_brl,
            alta_historica_usd=alta_historica_usd,
            alta_historica_brl=alta_historica_brl,
            data_alta_historico_usd=data_alta_historico_usd,
            data_alta_historico_brl=data_alta_historico_brl,
            porcentagem_de_alteracao_ath_usd=porcentagem_de_alteracao_ath_usd,
            porcentagem_de_alteracao_ath_brl=porcentagem_de_alteracao_ath_brl,
            baixa_historica_usd=baixa_historica_usd,
            baixa_historica_brl=baixa_historica_brl,
            baixa_historica_data_usd=baixa_historica_data_usd,
            baixa_historica_data_brl=baixa_historica_data_brl,
            porcentagem_de_alteracao_atl_usd=porcentagem_de_alteracao_atl_usd,
            porcentagem_de_alteracao_atl_brl=porcentagem_de_alteracao_atl_brl,
            captalizacao_de_mercado_usd=captalizacao_de_mercado_usd,
            captalizacao_de_mercado_brl=captalizacao_de_mercado_brl,
            rank_de_captalizacao=rank_de_captalizacao,
            captalizacao_de_mercado_tdiluida_usd=captalizacao_de_mercado_tdiluida_usd,
            captalizacao_de_mercado_tdiluida_brl=captalizacao_de_mercado_tdiluida_brl,
            data_baixa_historico_usd=data_baixa_historico_usd,
            data_baixa_historico_brl=data_baixa_historico_brl,
            volume_total_usd=volume_total_usd,
            volume_total_brl=volume_total_brl,
            alta_de_24h_usd=alta_de_24h_usd,
            alta_de_24h_brl=alta_de_24h_brl,
            baixa_de_24h_usd=baixa_de_24h_usd,
            baixa_de_24h_brl=baixa_de_24h_brl,
            mundanca_de_preco_em_24h_usd=mundanca_de_preco_em_24h_usd,
            mundanca_de_preco_em_24h_brl=mundanca_de_preco_em_24h_brl,
            percentual_de_mudanca_de_preco_24h_usd=percentual_de_mudanca_de_preco_24h_usd,
            percentual_de_mudanca_de_preco_24h_brl=percentual_de_mudanca_de_preco_24h_brl,
            percentual_de_mudanca_de_preco_7d_usd=percentual_de_mudanca_de_preco_7d_usd,
            percentual_de_mudanca_de_preco_7d_brl=percentual_de_mudanca_de_preco_7d_brl,
            percentual_de_mudanca_de_preco_14d_usd=percentual_de_mudanca_de_preco_14d_usd,
            percentual_de_mudanca_de_preco_14d_brl=percentual_de_mudanca_de_preco_14d_brl,
            percentual_de_mudanca_de_preco_30d_usd=percentual_de_mudanca_de_preco_30d_usd,
            percentual_de_mudanca_de_preco_30d_brl=percentual_de_mudanca_de_preco_30d_brl,
            percentual_de_mudanca_de_preco_60d_usd=percentual_de_mudanca_de_preco_60d_usd,
            percentual_de_mudanca_de_preco_60d_brl=percentual_de_mudanca_de_preco_60d_brl,
            percentual_de_mudanca_de_preco_1a_usd=percentual_de_mudanca_de_preco_1a_usd,
            percentual_de_mudanca_de_preco_1a_brl=percentual_de_mudanca_de_preco_1a_brl,
            fornecimento_total=fornecimento_total,
            fornecimento_maximo=fornecimento_maximo,
            fornecimento_circulante=fornecimento_circulante,
            ultima_atualizacao_dos_precos=ultima_atualizacao_dos_precos,
            sparkline_7d_usd=sparkline_7d_usd,
        )


data = "2021-11-10T14:24:11.849Z"
converter = "%Y-%m-%dT%H:%M:%SZ"
