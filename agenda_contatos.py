def adicionar_contato(lista_contatos, nome_contato, numero_contato, email_contato):
  contatos = {"nome": nome_contato, "número": numero_contato, "email": email_contato, "favorito": False}
  lista_contatos.append(contatos)
  return

def visualizar_contatos(lista_contatos):
  print("\nAgenda de contatos\n")
  for indice, contato in enumerate(lista_contatos, start=1):
    status = "✓" if contato["favorito"] else " "
    nome = contato["nome"]
    numero = contato["número"]
    email = contato["email"]
    print(f"{indice}. [{status}] Nome: {nome} - Telefone: {numero} - Email: {email}\n")
  return

def editar_contato(lista_contatos, indice_atualizado, novo_nome, novo_numero, novo_email):
  lista_contatos[indice_atualizado]["nome"] = novo_nome
  lista_contatos[indice_atualizado]["número"] = novo_numero
  lista_contatos[indice_atualizado]["email"] = novo_email
  print(f"Contato {indice_atualizado + 1} atualizado com sucesso.\n")
  return

def marcar_favorito(lista_contatos, indice_favorito):
  lista_contatos[indice_favorito]["favorito"] = True
  print(f"Contato número {indice_favorito + 1} marcado com sucesso.\n")
  return

def desmarcar_favorito(lista_contatos, indice_favorito):
  lista_contatos[indice_favorito]["favorito"] = False
  print(f"Contato número {indice_favorito + 1} desmarcado com sucesso.\n")
  return

def visualizar_contatos_favoritos(lista_contatos):
  print("\nSeus contatos marcados como favoritos\n")
  for indice, contato in enumerate(lista_contatos, start=1):
    if contato["favorito"] == True:
      status = "✓" if contato["favorito"] else " "
      nome = contato["nome"]
      numero = contato["número"]
      email = contato["email"]
      print(f"{indice}. [{status}] Nome: {nome} - Telefone: {numero} - Email: {email}\n")
  return

def apagar_contato(lista_contatos, indice_excluir):
  if lista_contatos[indice_excluir]["favorito"] == False:
    excluir_contato = lista_contatos[indice_excluir]
    lista_contatos.remove(excluir_contato)
    print(f"Contato {indice_excluir + 1} removido com sucesso.\n")
  
  else:
    print("Você não pode apagar um contato salvo como favorito.\n")
  return

lista_contatos = []

while True:
  
  print("1. Adicionar um contato")
  print("2. Visualizar contatos")
  print("3. Editar um contato")
  print("4. Marcar/desmarcar um contato como favorito")
  print("5. Ver lista de contatos favoritos")
  print("6. Apagar um contato")
  print("7. Encerrar programa")

  escolha = input("\nDigite o número da opção desejada: ")

  if escolha == "1":
    nome_contato = input("Digite o nome do contato: ")
    numero_contato = input("Digite o número de telefone do contato: ")
    email_contato = input("Digite o email do contato: ")
    adicionar_contato(lista_contatos, nome_contato, numero_contato, email_contato)

  elif escolha == "2":
    visualizar_contatos(lista_contatos) 

  elif escolha == "3":
    visualizar_contatos(lista_contatos)
    indice = int(input("Digite o número do contato que deseja editar: "))
    indice_atualizado = indice - 1 
    if indice_atualizado >= 0 and indice_atualizado < len(lista_contatos):
      novo_nome = input("Digite o novo nome do contato: ")
      novo_numero = input("Digite o novo telefone do contato: ")
      novo_email = input("Digite o novo email do contato: ")
      editar_contato(lista_contatos, indice_atualizado, novo_nome, novo_numero, novo_email) 
    else:
      print("Digite um número de contato válido.\n")
  
  elif escolha == "4":
    escolha_favoritar = input("Digite 1 para marcar um contato como favorito ou 2 para desmarcar um contato como favorito: ")
    if escolha_favoritar == "1":
      visualizar_contatos(lista_contatos)
      indice_favorito = (int(input("Digite o número do contato que deseja favoritar: "))) - 1
      marcar_favorito(lista_contatos, indice_favorito)
          
    elif escolha_favoritar == "2":
      visualizar_contatos(lista_contatos)
      indice_favorito = (int(input("Digite o número do contato que deseja desfavoritar: "))) - 1
      desmarcar_favorito(lista_contatos, indice_favorito)

    else:
      print("Digite uma opção válida.")  

  elif escolha == "5":
    visualizar_contatos_favoritos(lista_contatos)

  elif escolha == "6":
    visualizar_contatos(lista_contatos)
    indice_excluir = (int(input("Digite o número do contato que deseja excluir: "))) - 1
    apagar_contato(lista_contatos, indice_excluir)

  elif escolha == "7":
    break

print("Programa encerrado")