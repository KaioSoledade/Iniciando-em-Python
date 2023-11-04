print("Ola Mundo")
try:
    print(5/0)
    break
except:
    print("Desculpe, algo deu errado...")
except (ValueError, ZeroDivisionError):
    print("Muito ruim...")
 



