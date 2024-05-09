"""
Cap 3 - Andar em círculos não é necessariamente ruim...
Exercício 3
"""

divida = float(input("Digite o valor da dívida: "))
juros = 0.0
valor_juros = 0.0
total_juros = 0.0
parcela = 1
valor_parcelas = 0.0

for i in range(3, 16, 3):
    valor_juros = divida * juros
    total_juros = divida + valor_juros
    valor_parcelas = total_juros / parcela
    print(f"Total:R$ {total_juros:.2f} Juros:R$ {valor_juros:.2f} Número de parcelas:{parcela}"
          f" Valor da Parcela:R$ {valor_parcelas:.2f}".replace(".", ","))
    if parcela == 1:
        juros = 0.1
    else:
        juros += 0.05
    parcela = i
