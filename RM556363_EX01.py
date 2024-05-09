"""
Cap 3 - Andar em círculos não é necessariamente ruim...
Exercício 1
"""

segunda = 0
terca = 0
quarta = 0
quinta = 0
sexta = 0

colaboradores = int(input("Quantos colaboradores participarão da votação? "))
contador = 0

while contador != colaboradores:
    dia = int(input("Qual dia da semana você prefere para participar da live!"
                    "\nDigite o número referente ao dia de sua preferência\n"
                    "1- Segunda-feira\n2- Terça-feira\n3- Quarta-feira\n"
                    "4- Quinta-feita\n5- Sexta-feira\nDigite aqui: "))
    if dia == 1:
        segunda += 1
        contador += 1
    elif dia == 2:
        terca += 1
        contador += 1
    elif dia == 3:
        quarta += 1
        contador += 1
    elif dia == 4:
        quinta += 1
        contador += 1
    elif dia == 5:
        sexta += 1
        contador += 1
    else:
        print("Opção invalida, vote novamente")

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("\nSegunda-feira foi o dia mais votado!")
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("\nTerça-feira foi o dia mais votado!")
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print("\nQuarta-feira foi o dia mais votado!")
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print("\nQuinta-feira foi o dia mais votado!")
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print("\nSexta-feira foi o dia mais votado!")
else:
    print("\nTivemos um empate, melhor realizar uma nova votação!")

print(f"\nResultado da votação")
print(f"segunda: {segunda}, terça: {terca}, quarta: {quarta}, quinta: {quinta}, sexta: {sexta}")
