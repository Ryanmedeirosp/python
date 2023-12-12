peso = input("Digite seu peso:")
peso = int(peso)
altura = input("Digite sua altura:")
altura = float(altura)

print(f"Seu IMC é: {peso / altura**2}")
imc = peso / altura**2

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc <= 24.99:
    print("Peso normal")
elif imc >= 25 and imc <= 29.99:
    print("Sobrepeso")
elif imc >= 30:
    print("Obesidade")    