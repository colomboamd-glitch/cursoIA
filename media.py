print ("="*50)
print ("SEJA BEM VINDO!!")
print ("="*50)


notaUm = float(input("digite a primeira nota do aluno "))
notaDois = float(input("digite a segunda nota do aluno "))
notaTres = float(input("digite a terceira nota "))
notaQuatro = float(input("digite a quarta nota "))

media = (notaUm + notaDois + notaTres + notaQuatro) /4

print (f"a media é {media}")

if media >= 6:
    print ("Parabéns! voçê está aprovado")
else:
    print ("Voçê está reprovado!")
