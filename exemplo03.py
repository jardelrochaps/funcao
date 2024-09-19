
def calcular_pagamento(qtd_horas, salario):
    horas = float(qtd_horas)
    meu_salario = float(salario)

    valor_hora = meu_salario / horas

    #Calcular hora extra
    if horas > 160:

        hora_extra = horas - 160
        valor_hora += (hora_extra * (1.5 * valor_hora)) / 160

    return valor_hora
valor = calcular_pagamento(162, 5000)

print('Valor semanal: %.2f' %valor)
