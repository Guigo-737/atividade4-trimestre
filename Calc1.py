print("------Calculadora------")
n1 = float(input ("informe um número "))
n2 = float(input ("informe outro número "))
operador = input("informe o operador(+,-,/,*)")

if operador == "+":
    resultado = n1 + n2
if operador == "-":
    resultado = n1 - n2
if operador == "*":
    resultado = n1 * n2
if operador == "/":
    resultado = n1 / n2

print(f"Resultado: {resultado}")