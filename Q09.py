x = float(input())
y = float(input())
operacao = input()
if operacao == "+":
    resultado = x + y
elif operacao == "-":
    resultado = x - y
elif operacao == "*":
    resultado = x * y
elif operacao == "/":
    resultado = x / y
print("O resultado da operação é:", resultado)