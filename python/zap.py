class Carro:
    def __init__(self,modelo):
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self):
        self.velocidade = self.velocidade + 1

    def frear(self):
        if self.velocidade > 1:
            self.velocidade = self.velocidade - 1
        else:
            self.velocidade = 0

    def velocidade_atual(self):
        return self.velocidade