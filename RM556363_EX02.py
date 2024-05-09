"""
Cap 3 - Andar em círculos não é necessariamente ruim...
Exercício 2
"""

valor_carro = float(input("Digite o preço do carro: "))

preco_avista = valor_carro - (valor_carro * 0.2)

print(f"O preço final à vista com desconto de 20% é R$ {preco_avista:.2f}".replace(".", ","))

for i in range(6, 61, 6):
    preco_acrescimo = valor_carro + valor_carro * (i / 2 * 0.01)
    parcelas = preco_acrescimo / i
    print(f"O preço final parcelado em {i} X é de R$ {preco_acrescimo:.2f} "
          f"com parcelas de R$ {parcelas:.2f}".replace(".", ","))
