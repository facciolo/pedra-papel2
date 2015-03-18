import random
a = 0
b = 0
print(""" Bem vindos ao pedra-papel-tesoura-lagarto-Spock!""")
while((a < 3) and (b < 3)):
    y = random.choice(["pedra","papel","tesoura","lagarto","spock"])
    x = input("Escolha alguma das opções! ")
    if x == "pedra" :
        print("O computador escolheu", y)
        if y == "tesoura" or y == "lagarto":
            print("Pedrada em geral mermão. voce ganhou!")
            a = a+1
            b = 0
        elif y == "papel" or y == "spock":
            print("A pedra virou pó. Perdeu")
            b = b+1
            a = 0
        else:
            print("Deu empate")
    if x == "papel":
        print("O computador escolheu", y)
        if y == "pedra" or y == "spock": 
            print("Nao sei como papel ganha de alguma coisa.Enfim, voce ganhou.")
            a = a+1
            b = 0
        elif y == "tesoura" or y == "lagarto":
            print("Porque voce escolheu papel?Perdeu.")
            b = b+1
            a = 0
        else:
            print("Deu empate")
    if x == "tesoura":
        print("O computador escolheu", y)
        if y == "papel" or y == "lagarto":
            print("A tesoura ta cortando geral! Voce venceu!")
            a = a+1
            b = 0
        elif y == "pedra" or y == "spock":
            print("Escolheu errado irmão. Perdeu.")
            b = b+1
            a = 0
        else:
            print("Deu empate")
    if x == "lagarto":
        print("O computador escolheu", y)
        if y == "spock" or y == "papel":
            print("Sai de perto! O lagartão ta louco!Voce venceu.")
            a = a+1
            b = 0
        elif y == "tesoura" or y == "pedra":
            print(" O lagartão foi morto ")
            b = b+1
            a = 0
        else:
            print("Deu empate")
    if x == "spock":
        print("O computador escolheu", y)
        if y == "tesoura" or y == "pedra":
            print("Vida longa a Spock! Voce venceu!")
            a = a+1
            b = 0
        elif y == "lagarto" or y == "papel":
            print("Spock perdeu =/")
            b = b+1
            a = 0
        else:
            print("Deu empate")
print("O JOGO ACABOU irmão")
if a>b:
    print("Ganhou parceiro! Parabens.")
if a<b:
    print("O computador te deu um sova , tente novamente.")    
            


        
   
    
    

    