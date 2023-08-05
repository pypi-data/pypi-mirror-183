from decimal import Decimal


def to_decimal(num):
    try:
        return Decimal(str(num))
    except Exception:
        return Decimal('0.0')


def to_decimal_n(num, n):
    try:
        num_str = '{:.' + str(n) + 'f}'
        num_str = num_str.format(num)
        return Decimal(num_str)
    except Exception:
        return Decimal('0.0')


def is_decimal(num):
    response = False
    if (to_decimal(num) - int(num)) > to_decimal('0.0'):
        response = True
    return response


def normalize_number_to_print(valor):
    valor_decimal = to_decimal(valor)
    if valor_decimal - int(valor_decimal) != 0:
        return '{:.2f}'.format(valor_decimal)
    else:
        return int(valor_decimal)


# verifica se um número é par
def se_e_par(n):
    n = int(n)
    if (n % 2) == 0:
        return True
    else:
        return False


# função criada para arredondar um valor usando a norma ABNT 5891/77
# onde valor=o valor a ser arredondado
# n=limitador da quantidade de casas
def round_abnt(valor, n: int):
    try:
        vl_str = str(valor)
        if '.' in vl_str:
            inteira, decimal = str(valor).split('.')
        else:
            inteira = str(valor)
            decimal = '00'
    except Exception:
        print('Erro na conversão do valor!')

    decimal = (decimal + ('0' * 10))
    if len(decimal) > (n+2):
        prox = int(decimal[n])
        pos_prox = int(decimal[n+1])
        if ((prox >= 5 and pos_prox != 0) or
           (prox == 5 and pos_prox == 0 and se_e_par(decimal[n-1]) is False)):
            aux = int(decimal[n-1]) + 1
            decimal = decimal[:n-1] + str(aux) + decimal[n:]
    decimal = decimal[:n]
    return Decimal(f'{inteira}.{decimal}')
