from decimal import Decimal
from viggofiscal.subsystem.calculo_fiscal.utils import round_abnt, to_decimal


class BaseIcmsProprio():

    def __init__(self, valor_produto: Decimal, valor_frete: Decimal,
                 valor_seguro: Decimal, despesas_acessorias: Decimal,
                 valor_desconto: Decimal, valor_ipi: Decimal=Decimal('0.0')):
        self.valor_produto = to_decimal(valor_produto)
        self.valor_frete = to_decimal(valor_frete)
        self.valor_seguro = to_decimal(valor_seguro)
        self.despesas_acessorias = to_decimal(despesas_acessorias)
        self.valor_desconto = to_decimal(valor_desconto)
        self.valor_ipi = to_decimal(valor_ipi)

    def calcular_base_icms_proprio(self) -> Decimal:
        base_icms_proprio = (
            self.valor_produto + self.valor_frete + self.valor_seguro +
            self.despesas_acessorias + self.valor_ipi - self.valor_desconto)
        return round_abnt(base_icms_proprio, 2)
