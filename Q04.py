preco = float(input())
percentual = float(input())
desconto = preco * percentual / 100
final = preco - desconto
print("O valor do desconto é:", desconto)
print("O valor a pagar é:", final)