
def calcular_pagamento(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    taxa = float(valor_hora)

    if horas <= 40:
        salario = horas * taxa
    else:
        hora_extra = horas - 40
        salario = 40 * taxa + (hora_extra * (1.5 * taxa))

    return salario
semana = calcular_pagamento(40,75)
mes = 4 * semana
print('Valor semanal: ', semana)
print('Valor mensal: ', mes)