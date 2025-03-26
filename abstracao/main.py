from moto import *

m1 = Moto()
while True:
    marca_moto = str(input("Digite a marca da moto: "))
    if marca_moto.strip() == '':
        print('A marca da moto não pode ficar vazia, digite novamente.')
    else:
        m1.setMarca(marca_moto.title())
        break
while True:
    modelo_moto = str(input("Digite o modelo da moto: "))
    if modelo_moto.strip() == '':
        print('O modelo da moto não pode ficar vazio, digite novamente.')
    else:
        m1.setModelo(modelo_moto.title())
        break
while True:
    cor_moto = str(input("Digite a cor da moto: "))
    if cor_moto.strip() == '':
        print('A cor da moto não pode ficar vazia, digite novamente.')
    else:
        m1.setCor(cor_moto.title())
        break
while True:
    try:
        ano_moto = int(input("Digite o ano de fabricação da moto: "))
        if ano_moto <= 0:
          print('O ano de fabricação da moto não pode ser menor ou igual a zero.')
        else:
          m1.setAno(ano_moto)
          break
    except (ValueError, TypeError):
        print("Apenas números inteiros são permitidos, refaça corretamente a operação.")
while True:
    try:
        valor_moto = float(input("Digite o valor da moto: "))
        if valor_moto <= 0:
          print('O valor da moto não pode ser menor ou igual a zero.')
        else:
          m1.setValor(valor_moto)
          break
    except (ValueError, TypeError):
        print("Apenas números são permitidos, refaça corretamente a operação.")
print("\n")
m1.interacao()
