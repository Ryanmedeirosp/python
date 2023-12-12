aluno_lista = []
aluno = input("Digite o nome do aluno:")
aluno_lista.append(aluno)

n1 = input("Digite a sua nota:")
n1=float(n1)
n2 = input("Digite sua segunda nota:")
n2=float(n2)
trabextra = input("Digite sua nota do trabalho extra:")
trabextra=float(trabextra)
presença = input("Digite a presença do aluno:")
presença= float(presença)
media = (n1 + n2) / 2
media = media + trabextra
if media > 6 and presença >= 75:
    print("Aprovado")

else:
    print("reprovado")