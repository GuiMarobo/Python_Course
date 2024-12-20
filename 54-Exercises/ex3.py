"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

name = str(input("Digite o seu primeiro nome: "))

if 1 <= len(name) <= 4:
    print("Seu nome é curto.")

elif 5 <= len(name) <= 6:
    print("Seu nome é normal.")

elif len(name) > 6:
    print("Seu nome é muito grande")

else:
    print("Entrada inválida. Por favor digite seu nome!")