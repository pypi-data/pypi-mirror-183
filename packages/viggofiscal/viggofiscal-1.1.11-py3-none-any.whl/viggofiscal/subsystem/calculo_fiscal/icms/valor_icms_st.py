from decimal import Decimal
from viggofiscal.subsystem.calculo_fiscal.utils import round_abnt, to_decimal


class ValorIcmsST():

    def __init__(self, base_calculo_st: Decimal, aliq_icms_st: Decimal,
                 valor_icms_proprio: Decimal):
        self.base_calculo_st = to_decimal(base_calculo_st)
        self.aliq_icms_st = to_decimal(aliq_icms_st)
        self.valor_icms_proprio = to_decimal(valor_icms_proprio)

    def calcular_valor_icms_st(self):
        valor_icms_st = (
            (self.base_calculo_st * (self.aliq_icms_st / 100)) - 
            self.valor_icms_proprio)
        return round_abnt(valor_icms_st, 2)
