#bonus em 2024
Constante_bonus = 1000

# 1) Solicite ao usuarío que digite o seu nome
nome_usuario = input("Digite o seu nome: ")

# 2) solicite ao usuario que digite o valor do seu salario
# converte a entrada para um numero de ponto flutuante

salario_usuario = float(input("Digite o seu salario: "))

# 3) Solicite ao usuario que digite o valor do bonus recebido
# converta a entrada para um numero de ponto flutuante
bonus_usuario = float(input("digite o seu bonus"))

# 4) Calcule o valor do bonus final
valor_do_bonus = Constante_bonus + salario_usuario * bonus_usuario

# 5) imprima a mensagm personalizada incluindo o nome do usuario e o valor do bonus.
print(f"O usuario {nome_usuario} possui o bonus de {valor_do_bonus}")


