email_recebido = input("Digite seu email: ")
if len(email_recebido) < 11:
    print("1) O email informado não passou pelos critérios de validação, tente novamente")
elif email_recebido.find("@") < 0:
    print("2) O email informado não passou pelos critérios de validação, tente novamente")
elif email_recebido == None: 
    print("3) O email informado não passou pelos critérios de validação, tente novamente")
elif email_recebido[0].isnumeric():
     print("4) O email informado não passou pelos critérios de validação, tente novamente")
elif not email_recebido[0].isalpha()  : 
    print("5) O email informado não passou pelos critérios de validação, tente novamente")
else :
    print("Parabéns")

    



