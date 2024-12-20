"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

try:
    n = int(input("Digite um número inteiro: "))

    if n % 2 == 0:
        print(f"O número {n} é par.")
    else:
        print(f"O número {n} é impar.")

except ValueError:
    print("Entrada inválida. Digite um número inteiro.")
