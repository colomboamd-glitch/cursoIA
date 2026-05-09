print ("-"*50)
print ("sistema de autenticação")


nomeUsuario = input("digite seu nome ")
senhaUsuario = input ("digite sua senha ")

if nomeUsuario == "Colombo" and senhaUsuario == "1234":
    print ("acesso liberado!")
else:
    print ("acesso negado! verifique as informações de login e senha")
