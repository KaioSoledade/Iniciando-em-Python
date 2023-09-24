num1 = int(input("Escolha o primeiro numero:"))
num2 = int(input("Escolha o segundo numero:"))
num3 = int(input("Escolha o terceiro numero:"))

Num_maior = num1

if num2 > Num_maior:
    Num_maior = num2

if num3 > Num_maior:
    Num_maior = num3
    
Num_maior = str(Num_maior)
print("O maior numero é: " + Num_maior)