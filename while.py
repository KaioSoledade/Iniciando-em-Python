secret_number = 777

print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")

Num_cliente = int(input("Escolha um numero:"))
 
conter = 1
while conter:
    if Num_cliente == secret_number:
        print("Voce acertou, o numero correto era 777")
        conter-= 1
    elif Num_cliente != secret_number:
        print("Ha ha! Você está preso no meu loop!")


print("Muito bem, trouxa! Você está livre agora.")
