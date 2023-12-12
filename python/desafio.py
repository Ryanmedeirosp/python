nome = input("Digite seu nome completo:\n")
email = input("Digite seu email:\n")

nome = nome.title()

email1 = email.find("@")

usuario = ( nome[0]  )
email = (email[0] + "****" + email[email1:])


print(f"Parabéns, {nome},o úsuario:{usuario}, foi criado com sucesso !")
print(f"Enviamos para, {email}, sua senha de acesso" )
print(f"Atenção, ao entrar pela primeira vez com , {usuario}, modifique sua senha para uma maior segurança")