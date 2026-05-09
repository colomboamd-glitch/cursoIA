print("-" * 50)
print("bem vindo")
print("-" * 50)

nome = input("digite seu nome:") #input recebe dados do teclado do usuario
email = input ("digite seu email:")
cidade = input ("qual a sua cidade?")
estado = input ("qual o seu estado")
país = input ("qual o seu país")
#idadeAtual = int(input ("digite sua idade"))
#idadeFutura = idadeAtual + 1
anoAtual = int(input ("qual o ano atual"))
anoNascimento = int(input ("digite o ano do seu nascimento"))
idadeAtual = anoAtual - anoNascimento

print (f"Olá {nome}, o seu email é: {email}, sua cidade é: {cidade}, seu estado é: {estado}, seu país é: {país}, a sua idade é {idadeAtual} ") #o f minusculo antes das aspas permite qua eu trabalhe co variaveis na frase, {} servem para eu chamar um variavel para dentro da frase



