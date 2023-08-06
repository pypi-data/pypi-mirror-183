from decimal import Decimal
from viggofiscal.subsystem.calculo_fiscal.utils import round_abnt, to_decimal


class ValorIcmsProprio():

    def __init__(self, base_calculo: Decimal, aliq_icms_proprio: Decimal):
        self.base_calculo = to_decimal(base_calculo)
        self.aliq_icms_proprio = to_decimal(aliq_icms_proprio)

    def calcular_valor_icms_proprio(self):
        return round_abnt(
            (self.aliq_icms_proprio / 100 * self.base_calculo), 2)
