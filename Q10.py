valor_casa = float(input())
salario = float(input())
anos = int(input())
prestacao = valor_casa / (anos * 12)
if prestacao <= salario * 0.3:
    print("Empréstimo aprovado")
else:
    print("Empréstimo negado")
print("O valor da prestação mensal é:", prestacao)