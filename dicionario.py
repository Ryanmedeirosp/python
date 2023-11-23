nome = ""
lista = []

while nome != 3:
    print("1- NOVO USUÁRIO")
    print("2- LISTA COMPLETA")
    print("3- SAIR")
    
    Digite = input("Digite a opção:")
    Digite = int(Digite)
    if Digite == 1:
        dicionario = {"nome":"", "idade":""}

        print("\x1bc", end="") 
        nome = input("Digite seu nome:\n")
        dicionario["nome"] = nome
        idade = input("Digite sua idade:\n")
        dicionario["idade"] = idade
        for item in lista:
            if item["nome"] == nome and item["idade"] == idade:
                print("Usuário já cadastrado")
                nome=input("Digite outro nome:\n")
                idade=input("Digite a idade:\n")
                dicionario["idade"] = idade
                dicionario["nome"] = nome  
            else:
                dicionario["idade"] = idade
                
        loc = input("Digite sua localidade:\n")
        dicionario["localidade"] = loc
        salario = input("Digite seu salário:\n")
        dicionario["salário"] = salario

        lista.append(dicionario)

        print("\nUSUÁRIO CADASTRADO\n\n")

    elif Digite == 2:
        print("\x1bc", end="") 
        print(f"SUA LISTA É:{lista}")
              
    elif Digite == 3:
        nome = 3
    else:
        print("\x1bc", end="") 
        print("VOCÊ NÃO DIGITOU UMA OPÇÃO")
    
print(f"PROGRAMA ENCERRADO")       
