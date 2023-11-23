
def f ():
    num1 = input("Digite o primeiro número:\n")
    num2 = input("Digite o segundo número:\n")
    return [num1, num2]


def soma():
    numero = f()
    print(f"Resultado: {int(numero[0]) + int(numero[1])}")

def sub():
    numero = f()
    print(f"Resultado: {int(numero[0]) - int(numero[1])}")

def mult():
    numero = f()
    print(f"Resultado: {int(numero[0]) * int(numero[1])}")
def div():
    numero = f()
    print(f"Resultado: {int(numero[0]) / int(numero[1])}")

fechar = True

while fechar:
    menu = input("OPÇÕES:\n1-Soma \n2-Sub \n3-Mult\n4-Div\n5-Sair\nDIGITE SUA OPÇÃO: ")
    menu = int(menu)
    if menu == 1:
        soma()
    elif menu == 2:
        sub()
    elif menu == 3:
        mult()
    elif menu == 4:
        div()
    elif menu == 5:
        fechar = False
    else:
        print("Você digitou errado")