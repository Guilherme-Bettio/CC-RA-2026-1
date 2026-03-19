while True:
    login = input("insira seu login: \n1. admin \n2. convidado\n\n")
    if login == "admin" or login == "convidado":
        break
    print("opção invalida")
senha = input("insira sua senha\n")

if login == "admin" and senha == "1234":
    print("bem-vindo, administrador")
else:
    print("Sinto muito, você nao tem permissao para acessar o sistema")