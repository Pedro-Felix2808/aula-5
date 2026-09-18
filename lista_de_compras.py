produtos = []

def mostrar():
   for x in produtos:
      print(f"Sua lista é: {x}")

def cadastro():
    novo_produto = str(input("Digite o nome do produto: "))
    produtos.append(novo_produto)

def excluir():
    exclusao = str(input("Digite o item que você deseja excluir: "))
    produtos.remove(exclusao)

def modificar():
    modi = int(input("Digite o indice do produto que você deseja alterar: "))
    prod = str(input("Qual produto você quer colocar no lugar: "))  
    produtos[modi] = prod     



while True: 
   print("Lista de Compras")
   print("1 - mostrar lista")
   print("2 - cadastrar item na lista")
   print("3 - excluir item da lista")
   print("4 - modificar item da lista")
   print("0 - sair")

   opcao = input("Escolha uma opção: ")

   if opcao == "1":
      mostrar()

   elif opcao == "2":
       cadastro()

   elif opcao == "3":
       excluir()

   elif opcao == "4":
       modificar()

   elif opcao == "0":
    print("Saindo do sistema...")
    break
  
   else:
       print("Opção inválida, tente novamente!!!")          