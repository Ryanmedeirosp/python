class Aluno:
    def __init__(self):
        self.nome = ""
        self.notas = []
        self.idade = 0 

    def media(self):
        return (self.notas[0] + self.notas[1]) / 2
        
    def aprovacao(self):
        media = self.media()
        if  media>= 7:
            print("aprovado")
            return 'aprovado'
        else:
            print("reprovado") 
            return 'reprovado'


nome = input("Digite seu nome:")
idade = input("Digite sua idade:")
nota1 = input("Digite a primeira nota:")
nota2 = input("Digite a segunda nota:")

meualuno = Aluno()
meualuno.nome = nome
meualuno.idade = idade
meualuno.notas = [float(nota1), float(nota2)]
media = meualuno.media()
status = meualuno.aprovacao()
print(media)
print(status)


