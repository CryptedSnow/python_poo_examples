from jojo import *
    
jojo = JoJo()

while True:
  nome = str(input("Digite o nome do usuário: "))
  if nome.strip() == '':
    print("O nome do usuário não pode ficar vazio.")
  else:
    jojo.setNome(nome.title())
    break
while True:
  stand = str(input(f"Digite o nome do stand de {jojo.getNome()}: "))
  if stand.strip() == '':
    print(f"O nome do stand de {jojo.getNome()} não pode ficar vazio.")
  else:
    jojo.setStand(stand.title())
    break
while True:
  try:
    if (jojo.status_stand == False):
      print(f"O stand {jojo.getStand()} está desativado.")
      resposta_status = int(input("Deseja ativar? (0 - Não | 1 - Sim): "))
      if resposta_status == 1:
        jojo.setStatusStand(True)
        print(f"O Stand {jojo.getStand()} foi ativado.")
        break
      elif (resposta_status == 0):
        print(f"O Stand {jojo.getStand()} continuará inativo.")
        break
      else:
        print("Opção inválida, digite uma das respectivas opções.")
    else:
      print(f"O stand {jojo.getStand()} está ativado.")
      resposta_status = int(input("Deseja desativar? (0 - Não | 1 - Sim): "))
      if resposta_status == 1:
        jojo.setStatusStand(False)
        print(f"O Stand {jojo.getStand()} foi desativado.")
        break
      elif resposta_status == 0:
        print(f"O Stand {jojo.getStand()} continuará ativo.")
        break
      else:
        print("Opção inválida, digite uma das respectivas opções.")
  except (ValueError, TypeError):
    print("Campo deve conter apenas números inteiros, refaça a operação.");
  
jojo.falar()
del jojo