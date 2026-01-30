velocidade = float(input())
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print("Você foi multado")
    print("O valor da multa é:", multa)
else:
    print("Velocidade dentro do limite")