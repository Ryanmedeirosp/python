import requests
resposta = requests.get("https://jsonplaceholder.typicode.com/users")
if resposta.status_code == 200:
    dados = resposta.json()

for i in dados:
    print(i['id'],i['name'])

valor = True

while valor:
    print("\nMENU")
    print("a- exibir post")
    print("b- Liste os usuários")
    print("c- sair")
    opc = input("Qual opc você quer:")

    if opc == 'a':
        num_usuario = input("Digite Id do usuario:")
        num_usuario = int(num_usuario)
        get = requests.get(f"https://jsonplaceholder.typicode.com/posts?userId={num_usuario}")
        if get.status_code == 200:
            busca = get.json()
        for i in busca:
            print(i['title'])
    
    elif opc == 'b':
        for i in dados:
            print(f"\n{i['id']} {i['name']}")

    elif opc == 'c':
        valor = False
    
   
    