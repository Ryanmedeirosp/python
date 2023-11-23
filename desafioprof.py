num = []
contador = 0
maior = 0

while contador < 5:
    numeros = input("Digite um número:")
    num.append(int(numeros))
    contador = contador+1
for i in num:
    if i > maior:
        maior = i
print(maior)