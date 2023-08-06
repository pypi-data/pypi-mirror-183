from decimal import Decimal
from viggofiscal.subsystem.calculo_fiscal.icms.base_icms_proprio \
    import BaseIcmsProprio
from viggofiscal.subsystem.calculo_fiscal.icms.valor_icms_proprio \
    import ValorIcmsProprio
from viggofiscal.subsystem.calculo_fiscal.utils import to_decimal


class Icms00():

    def __init__(self, valor_produto: Decimal, valor_frete: Decimal,
                 valor_seguro: Decimal, despesas_acessorias: Decimal,
                 valor_ipi: Decimal, valor_desconto: Decimal,
                 aliq_icms_proprio: Decimal):
        self.valor_produto = to_decimal(valor_produto)
        self.valor_frete = to_decimal(valor_frete)
        self.valor_seguro = to_decimal(valor_seguro)
        self.despesas_acessorias = to_decimal(despesas_acessorias)
        self.valor_ipi = to_decimal(valor_ipi)
        self.valor_desconto = to_decimal(valor_desconto)
        self.aliq_icms_proprio = to_decimal(aliq_icms_proprio)
        self.base_icms = BaseIcmsProprio(
            valor_produto, valor_frete, valor_seguro, despesas_acessorias,
            valor_desconto, valor_ipi)

    def base_icms_proprio(self):
        return self.base_icms.calcular_base_icms_proprio()

    def valor_icms_proprio(self) -> Decimal:
        return ValorIcmsProprio(
            self.base_icms_proprio(), self.aliq_icms_proprio).\
            calcular_valor_icms_proprio()
