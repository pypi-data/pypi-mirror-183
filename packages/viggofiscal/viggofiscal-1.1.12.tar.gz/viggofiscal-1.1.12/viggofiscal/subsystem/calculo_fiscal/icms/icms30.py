from decimal import Decimal
from viggofiscal.subsystem.calculo_fiscal.icms.base_reduzida_icms_proprio \
    import BaseReduzidaIcmsProprio
from viggofiscal.subsystem.calculo_fiscal.icms.base_icms_proprio \
    import BaseIcmsProprio
from viggofiscal.subsystem.calculo_fiscal.icms.icms00 \
    import Icms00
from viggofiscal.subsystem.calculo_fiscal.icms.valor_icms_proprio \
    import ValorIcmsProprio
from viggofiscal.subsystem.calculo_fiscal.utils import round_abnt, to_decimal
from viggofiscal.subsystem.calculo_fiscal.icms.base_icms_st \
    import BaseIcmsST
from viggofiscal.subsystem.calculo_fiscal.icms.base_reduzida_icms_st \
    import BaseReduzidaIcmsST
from viggofiscal.subsystem.calculo_fiscal.icms.valor_icms_st \
    import ValorIcmsST


class Icms30():

    def __init__(self, valor_produto: Decimal, valor_frete: Decimal,
                 valor_seguro: Decimal, despesas_acessorias: Decimal,
                 valor_ipi: Decimal, valor_desconto: Decimal,
                 aliq_icms_proprio: Decimal, aliq_icms_st: Decimal,
                 mva: Decimal, percentual_reducao_st: Decimal=Decimal('0.0')):
        self.valor_produto = to_decimal(valor_produto)
        self.valor_frete = to_decimal(valor_frete)
        self.valor_seguro = to_decimal(valor_seguro)
        self.despesas_acessorias = to_decimal(despesas_acessorias)
        self.valor_ipi = to_decimal(valor_ipi)
        self.valor_desconto = to_decimal(valor_desconto)
        self.aliq_icms_proprio = to_decimal(aliq_icms_proprio)
        self.aliq_icms_st = to_decimal(aliq_icms_st)
        self.mva = to_decimal(mva)
        self.percentual_reducao_st = to_decimal(percentual_reducao_st)
        self.bc_icms_proprio = BaseIcmsProprio(
            valor_produto, valor_frete, valor_seguro, despesas_acessorias,
            valor_desconto)

    # ICMS Próprio
    def base_icms_proprio(self) -> Decimal:
        return self.bc_icms_proprio.calcular_base_icms_proprio()

    def valor_icms_proprio(self) -> Decimal:
        valor_icms_proprio = ValorIcmsProprio(
            self.base_icms_proprio(), self.aliq_icms_proprio).\
            calcular_valor_icms_proprio()
        return valor_icms_proprio

    def valor_icms_desonerado(self) -> Decimal:
        return self.valor_icms_proprio()

    # ICMS ST
    def base_icms_st(self) -> Decimal:
        if self.percentual_reducao_st == Decimal('0.0'):
            self.bc_icms_st = BaseIcmsST(self.base_icms_proprio(), self.mva,
                                         self.valor_ipi)
            return self.base_icms_st().calcular_base_icms_st()
        else:
            self.bc_reduzida_icms_st = BaseReduzidaIcmsST(
                self.base_icms_proprio(), self.mva, self.percentual_reducao_st,
                self.valor_ipi)
            return self.bc_reduzida_icms_st.calcular_base_reduzida_icms_st()

    def valor_icms_st(self) -> Decimal:
        valor_icms_st = ValorIcmsST(
            self.base_icms_st(), self.aliq_icms_st, self.valor_icms_proprio()).\
            calcular_valor_icms_st()
        return valor_icms_st