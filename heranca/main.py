from carro import *

c1 = Carro()
while True:
    marca_carro = str(input("Digite a marca do carro: "))
    if marca_carro.strip() == '':
        print('A marca do carro não pode ficar vazia, refaça a operação.')
    else:
        c1.setMarca(marca_carro.title())
        break
while True:
    modelo_carro = str(input("Digite o modelo do carro: "))
    if modelo_carro.strip() == '':
        print('O modelo do carro não pode ficar vazio, refaça a operação.')
    else:
        c1.setModelo(modelo_carro.title())
        break
while True:
    cor_carro = str(input("Digite a cor do carro: "))
    if cor_carro.strip() == '':
        print('A cor do carro não pode ficar vazio, refaça a operação.')
    else:
        c1.setCor(cor_carro.title())
        break
while True:
    try:
        ano_carro = int(input("Digite o ano de fabricação do carro: "))
        if ano_carro <= 0:
          print('O ano de fabricação do carro não pode ser menor ou igual a zero, refaça a operação.')
        else:
          c1.setAno(ano_carro)
          break
    except (ValueError, TypeError):
        print("Apenas números inteiros são permitidos, refaça a operação.")
while True:
    try:
        valor_carro = float(input("Digite o valor do carro: "))
        if valor_carro <= 0:
          print('O valor do carro não pode ser menor ou igual a zero, refaça a operação.')
        else:
          c1.setValor(valor_carro)
          break
    except (ValueError, TypeError):
        print("Apenas números são permitidos, refaça a operação.")
print("\n")
c1.interacao()
