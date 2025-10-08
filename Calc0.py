print("------Calculadora------")
n1 = float(input ("informe um número "))
n2 = float(input ("informe outro número "))

resultado1 = n1 + n2
print("o resultado da soma é:", resultado1)

resultado2 = n1 * n2
print("o resultado da multiplicação é:", resultado2)

resultado3 = n1 - n2
print("o resultado da subitração é:", resultado3)

if(n2 == 0):
    print("não é possivel dividir por zero")
else:
    resultado4 = n1 / n2
    print("o resultado da divisão é:", resultado4)