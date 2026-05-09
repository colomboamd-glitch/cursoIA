listaNotas = []# criamos uma lista vazia

print ("-"*40)
print ("Bem vindo a I.A que calcula notas e media final ")

while True:
    notas = input("Digite a nota que deseja inserir (digite sair para parar): ")

    if notas.lower() == "sair": # comando lower abriga a entrada ser minúscula
        break
    else:
        listaNotas.append(float(notas))# insere dados em lista
media = sum(listaNotas) / len(listaNotas)

print (f"a media final do aluno é {media:.2f}") # :.2f limita a saída

if media >= 6:
    print ("APROVADO")
else:
    print("REPROVADO")