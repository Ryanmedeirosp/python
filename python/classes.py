class Conta:
    def __init__(self,):
        self.nome = ""
        self.status = ""
        self.numero = 0
        self.numero = int(self.numero)
        self.saldo = 0

    def criar_conta(self):
        self.nome = input("Insira seu nome:")
        self.status = 'ativa'
        self.numero = self.numero + 1
        
    
    def exibir_saldo(self):
        print(self.saldo)

    def dados_conta(self):
        print(f"NOME:{self.nome}\nSTATUS:{self.status}\nNÚMERO DA CONTA:{self.numero}\n")
    
    def mudar_status(self):

        self.status = input(f"Deseja mudar os status da conta\n1)DESATIVA\n2)ATIVA\n")
        
        
        if self.status == "1":
            self.status = "desativa"
            print("Sua conta foi desativada")
        
        elif self.status == "2":
            self.status = "ativa"
            print("Sua conta está ativa")
        
        else:
            print("erro")

class Caixa:
    def __init__(self,):
        self.saldo = 0
    
    def deposito(self):
        self.dep = input("Quanto deseja depositar:")
        self.dep = int(self.dep)
        self.saldo = self.saldo + self.dep

    def saque(self):
        self.valor = input("Quando desejar sacar:")
        self.valor = int(self.valor)
        if self.valor > self.saldo:
            print("saldo insuficiente")
            
        else:
            self.saldo = self.saldo - self.valor
            print("saque efetuado")
        
    def exibir(self):
        print(self.saldo)

banco = Conta()
caixa2 = Caixa()
sair = True

while sair:
    
    menu = input("1)Conta\n2)Caixa\n3)Sair\n")
    menu = int(menu)

    if menu == 1:
       
        print("Menu conta")
        conta = input("1)Criar conta\n2)Exibir saldo\n3)Dados da conta\n4)Mudar status\n")
        conta = int(conta)
        if conta == 1:
            banco.criar_conta()
        if conta == 2:
            print("Seu saldo é:")   
            caixa2.exibir()
        elif conta == 3:
            print("Seus dados são:")
            banco.dados_conta()
        elif conta == 4:
            banco.mudar_status()
        
    
    elif menu == 2:
        
        print("Menu caixa")
        atr = input("1)Deposito\n2)Saque\n3)saldo\n")
        atr = int(atr)
        if atr == 1:
            print("DEPOSITO")
            caixa2.deposito()
        
        elif atr == 2:
            print("SAQUE")
            caixa2.saque()
        
        elif atr == 3:
            caixa2.exibir()
        
        else:
            sair = False
        
    elif menu == 3: 
        sair = False
      
    else:
        print("DIGITOU ERRADO")






        




        
    


