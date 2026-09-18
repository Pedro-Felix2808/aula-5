def circulo ():
    raio = float(input("Digite o valor do raio do circulo: "))
    area = 3.14 * raio * raio
    print(f"A área do circulo é igual a: {area}")

def triangulo ():
    base = float(input("Digite o valor da base do triângulo: "))
    altura = float(input("Digite o valor da altura do seu triângulo: "))
    area = (base * altura) / 2  
    print(f"A área do seu triângulo vai ser igual a: {area}")

def quadrado ():
    lado = float(input("Digite o valor do lado do quadrado: "))
    area = lado * lado   
    print(f"A área do seu quadrado vai ser igual a: {area}")

def retangulo():
    largura = float(input("Digite a largura do seu retângulo: ")) 
    comprimento = float(input("Digite o comprimento do seu retângulo: "))
    area = largura * comprimento
    print(f"A área do seu retângulo vai ser igual a: {area}")   


def paralelogramo():
    base = float(input("Digite o valor da base do seu paralelogramo: "))
    altura = float(input("Digite a altura do seu paralelogramo: "))
    area = base * altura
    print(f"A área do seu paralelogramo vai ser igual a: {area}")


def losango():
    dma = float(input("Digite o valor da diagonal maior do seu losango: "))
    dme = float(input("Digite o valor da diagonal menor do seu losango: "))
    area = (dma * dme) / 2
    print(f"A área do seu losango vai ser igual a: {area}")

def trapezio():
    basema = float(input("Digite o valor da sua base maior do seu trapézio: "))
    baseme = float(input("Digite o valor da base menor do seu trápezio: "))
    altura = float(input("Digite o valor da altura do seu trapézio: "))
    soma = basema + baseme
    area = (soma * altura) / 2
    print(f"A áre do seu trapézio vai ser igual a: {area}")


while True: 
   print("Áreas das formas geométricas")
   print("1 - circulo")
   print("2 - triângulo")
   print("3 - quadrado")
   print("4 - retângulo")
   print("5 - paralelogramo")
   print("6 - losango")
   print("7 - trapézio")
   print("0 - sair")

   opcao = input("Escolha uma opção: ")

   if opcao == "1":
      circulo()

   elif opcao == "2":
       triangulo()

   elif opcao == "3":
       quadrado()

   elif opcao == "4":
       retangulo()
   
   elif opcao == "5":
       paralelogramo()

   elif opcao == "6":
       losango()

   elif opcao == "7":
        trapezio()

   
   elif opcao == "0":
    print("Saindo do sistema...")
    break
  
   else:
       print("Opção inválida, tente novamente!!!")                   

