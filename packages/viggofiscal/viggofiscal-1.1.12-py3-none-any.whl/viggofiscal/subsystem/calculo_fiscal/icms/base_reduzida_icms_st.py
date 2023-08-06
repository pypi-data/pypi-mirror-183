from decimal import Decimal
from viggofiscal.subsystem.calculo_fiscal.utils import round_abnt, to_decimal


class BaseReduzidaIcmsST():

    def __init__(self, base_icms_proprio: Decimal, mva: Decimal,
                 percentual_reducao_st: Decimal,
                 valor_ipi: Decimal=Decimal('0.0')):
        self.base_icms_proprio = to_decimal(base_icms_proprio)
        self.mva = to_decimal(mva)
        self.percentual_reducao_st = to_decimal(percentual_reducao_st)
        self.valor_ipi = to_decimal(valor_ipi)

    def calcular_base_reduzida_icms_st(self) -> Decimal:
        base_icms_st = self.base_icms_proprio * (1 + (self.mva / 100))
        base_icms_st = (
            base_icms_st - (base_icms_st * (self.percentual_reducao_st / 100)))
        base_reduzida_icms_st = base_icms_st + self.valor_ipi
        return round_abnt(base_reduzida_icms_st, 2)
