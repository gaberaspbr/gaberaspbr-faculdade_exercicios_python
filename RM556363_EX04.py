"""
Cap 3 - Andar em círculos não é necessariamente ruim...
Exercício 4
"""
verificador = 0
ir = 0.0

while verificador != 1:
    tipo_invest = int(input("Qual investimento deseja resgatar"
                            "\n1- CDB\n2- LCI\n3- LCA"
                            "\nDigite sua opção: "))
    if tipo_invest == 1 or tipo_invest == 2 or tipo_invest == 3:
        verificador = 1
    else:
        print("Opção invalida")

verificador = 0

while verificador != 1:
    valor_invest = float(input("Quanto deseja resgatar? "))
    if valor_invest < 0:
        print("Por favor digite um número positivo")
    else:
        verificador = 1

verificador = 0

while verificador != 1:
    dias = int(input("Qual foi a quantidade de dias que o valor foi mantido investido? "))
    if dias < 0:
        print("Por favor digite um número positivo de dias.")
    else:
        verificador = 1

if tipo_invest == 1:
    if dias <= 180:
        ir = valor_invest * 0.225
    elif dias > 180 and dias <= 360:
        ir = valor_invest * 0.2
    elif dias > 360 and dias <= 720:
        ir = valor_invest * 0.175
    else:
        ir = valor_invest * 0.15
    print(f"Imposto de renda a ser pago: {ir:.2f}".replace(".", ","))
else:
    print("Investimento isento de Imposto de renda")


