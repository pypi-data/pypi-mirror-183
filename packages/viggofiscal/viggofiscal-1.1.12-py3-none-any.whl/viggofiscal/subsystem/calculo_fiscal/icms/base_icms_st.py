from decimal import Decimal
from viggofiscal.subsystem.calculo_fiscal.utils import round_abnt, to_decimal


class BaseIcmsST():

    def __init__(self, base_icms_proprio: Decimal, mva: Decimal,
                 valor_ipi: Decimal=Decimal('0.0')):
        self.base_icms_proprio = to_decimal(base_icms_proprio)
        self.mva = to_decimal(mva)
        self.valor_ipi = to_decimal(valor_ipi)

    def calcular_base_icms_st(self) -> Decimal:
        base_icms_st = (
            (self.base_icms_proprio + self.valor_ipi) * (1 + (self.mva / 100)))
        return round_abnt(base_icms_st, 2)
