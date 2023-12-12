
nome = input("Digite seu nome:")
peso = input("Digite seu peso:")
peso = int(peso)
altura = input("Digite sua altura:")
altura = float(altura)

print(f"Seu IMC é: {peso / altura**2}")
imc = peso / altura**2

if imc < 18.5:
    print("Abaixo do peso")
    f = open("texto.txt","a")
    f.write(f"{nome} esta magro(a) e tem IMC de: {imc}\n")
    f.close()
elif imc >= 18.5 and imc <= 24.99:
    print("Peso normal")
    f = open("texto.txt","a")
    f.write(f"{nome} esta normal e tem IMC de: {imc}\n")
    f.close()
elif imc >= 25 and imc <= 29.99:
    print("Sobrepeso")
    f = open("texto.txt","a")
    f.write(f"{nome} esta com sobrepeso(a) e tem IMC de: {imc}\n")
    f.close()
elif imc >= 30:
    print("Obesidade")    
    f = open("texto.txt","a")
    f.write(f"{nome} esta obeso(a) e tem IMC de: {imc}\n")
    f.close()

