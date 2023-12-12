from zap import Carro  
    
meucarro = Carro(modelo ="Ferrari 911")
meucarro.acelerar()
meucarro.acelerar()
meucarro.acelerar()
meucarro.acelerar()
print(meucarro.velocidade_atual())
meucarro.frear()
print(meucarro.velocidade_atual())