"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
try:
    n = int(input("Digite que horas são: (00 - 23) "))

    if 0 <= n <= 11:
        print("Bom dia.")

    elif 12 <= n <= 17:
        print("Boa tarde.")

    elif 18 <= n <= 23:
        print("Boa noite.")

    else:
        print("Digite um horário válido. (00 - 23)")

except ValueError:
    print("Entrada inválida. Digite um número inteiro.")

