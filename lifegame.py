#Trabalho extra jogo da vida

from cmath import pi
import random

def primo(n):
    primo = True
    for i in range(2,n):
        if(n%i==0):
            primo = False
    return primo

def primos(n):
    nu = 2
    while nu <= n:
        if primo(nu) == True:
            print("Números primos até 100:",nu)
        nu+=1

def soma(ini,fim):
    for i in range(ini,fim+1):
        ini+=i
        print("O somátorio de 1 a 10:",ini-1)

def fibo(n):
    a=1
    b=1
    print("Sequência de Fibonacci:",a)
    print("Sequência de Fibonacci:",b)
    for i in range(n-3):
        total = a + b
        b=a
        a= total
        print("Sequência de Fibonacci:",total)

def circulo(r):
    a = pi * r ** 2
    print("A área do círculo é",round(a,2))

def fatorial(n):
    u=1
    for i in range(1,n+1):
        u*=i
    print("O fatorial de",n,"é",u)

def div25(n):
    cont1 = 0
    nu =  1
    while cont1 < 5:
        if nu % 2 == 0 and nu % 5 == 0:
            print(nu,"é divísel por dois e por 5.")
            cont1 +=1
        nu+=1
   
def dado():
    dado = random.randint(1,6)
    print("O dado caiu no",dado)
    return dado

def matematica(njogador):
    print("Desafio matemático")
    dado1 = dado()
    if dado1 == 1:
        print("Mostre os números primos até 100")
        primos(100)
    if dado1 == 2:
        print("Faça o somatório de 1 até 100")
        soma(1,10)
    if dado1 == 3:
        print("Faça a série de fibonacci até o 10 elemento.")
        fibo(10)
    if dado1 == 4:
        print("Faça a área de um circulo com raio 2,5")
        circulo(2.5)
    if dado1 == 5:
        print("Faça o fatorial de 5")
        fatorial(5)
    if dado1 == 6:
        print("quais 5 primeiros números divisives por 2 e por 5")
        div25(5)

def jogo():
    print("O jogo vai começar.")
    loop = loop1 = True

    casajog1 = casajog2 = filhojog1 = filhojog2 = 0
    direito2 = medicina2 = artes2 = letras2 = geografia2 = historia2 = False
    reseta = reseta2 = dadinho2 = morreu2 = filhos2 = morreu2 = mat2 = dadinho2 = formouu2 = casaar2 = divorciou2 = loterica2 = famosso2 = False
    dadinho = mat = morreu1 = formouu = filhos = casaar = direito = medicina = artes = letras = geografia = historia = divorciou = loterica = famosso  = False
    jogador1 = 1
    jogador2 = 2 
    while loop:
        print("Vez do jogador 1 ")
        jog1dado = dado()
        casajog1 += jog1dado
        print("Jogador",jogador1,"vá para a casa",casajog1)
        if casajog1 == 1 or casajog1 == 3 or casajog1 == 10 or casajog1 == 17:
            print("Jogador 1 você vai jogar o desafio do dado. \n")
            print("Jogue o dado, se cair no 1 avança 1 casa, se cair no 3 recua uma casa, e se cair no 6 perdeu uma rodada. \n")
            dadinho = True 
            dado1 = dado()
            if dado1 == 1:
                print("Avança 1 casa")
                casajog1+=1
                print(18*"-")
            if dado1 == 3:
                print("Recua 1 casa.")
                casajog1 -= 1
                print(18*"-")
            if dado1 == 6:
                print("Perde uma rodada.")
                print(18*"-") 
                rodada1 = -1
            if dado1 == 2 or dado1 == 4 or dado1 == 5:
                print("Nada vai acontecer")
                print(18*"-")
        if casajog1 == 2 or casajog1 == 8 or casajog1 == 18:
            morreu1 = True
            print("Jogador",jogador1,"morreu ao cair na casa",casajog1)
            print("Jogador",jogador1,"vamos ver sua trajetoria.")
            if morreu1 == True:
                print("O jogador 1 morreu.")
            if dadinho == True:
                print("O jogador 1 jogou o desafio do dado.")
            if mat == True:
                print("O jogador 1 jogou o desafio matemático.")
            if formouu == True:
                print("O jogador 1 se formou.")
                if medicina == True:
                        print("O jogador 1 se formou em medicina!")
                if historia == True:
                    print("O jogador 1 se formou em história!")
                if geografia == True:
                    print("O jogador 1 se formou em geografia!")
                if artes == True:
                    print("O jogador 1 se formou em artes!")
                if letras == True:
                    print("O jogador 1 se formou em letras!")
                if direito == True:
                    print("O jogador 1 se formou em direito!")
            if filhos == True:
                print("O jogador 1 teve filho.")
            if casaar == True:
                print("O jogador 1 se casou.")
            if divorciou == True:
                print("O jogador 1 se divorciou.")
            if loterica == True:
                print("O jogador 1 ganhou na loteria")
            if famosso == True:
                print("O jogador 1 é famoso.")
            if reseta == True:
                print("O jogador 1 teve a vida resetada.")

            print("O jogador 2 ganhou. Vamos ver seu histórico")
            if morreu2 == True:
                print("O jogador 2 morreu.")
            if dadinho2 == True:
                print("O jogador 2 jogou o desafio do dado.")
            if mat2 == True:
                print("O jogador 2 jogou o desafio matemático.")
            if formouu2 == True:
                print("O jogador 2 se formou.")
                if medicina2 == True:
                        print("O jogador 2 se formou em medicina!")
                if historia2 == True:
                    print("O jogador 2 se formou em história!")
                if geografia2 == True:
                    print("O jogador 2 se formou em geografia!")
                if artes2 == True:
                    print("O jogador 2 se formou em artes!")
                if letras2 == True:
                    print("O jogador 2 se formou em letras!")
                if direito2 == True:
                    print("O jogador 2 se formou em direito!")
            if filhos2 == True:
                print("O jogador 2 teve filho.")
            if casaar2 == True:
                print("O jogador 2 se casou.")
            if divorciou2 == True:
                print("O jogador 2 se divorciou.")
            if loterica2 == True:
                print("O jogador 2 ganhou na loteria")
            if famosso2 == True:
                print("O jogador 2 é famoso.")
            if reseta2 == True:
                print("O jogador 2 teve a vida resetada!")
            if dadinho2 == False and reseta2 == False and mat2 == False and formouu2 == False and filhos2 == False and casaar2 == False and divorciou2 == False and loterica2 == False and famosso2 == False:
                print("Nada aconteceu na vida do jogador 2.")
            loop = loop1 = False
        if casajog1 == 4 or casajog1 == 11 or casajog1 == 19:
            print("Jogador 1 caiu no desafio matemático, jogue o dado e faça seu desafio.")
            matematica(jogador1) 
            mat = True
        if casajog1 == 5:
            formouu = True
            print("Jogador 1 você vai se formar, você caiu na casa 4",casajog1,".Jogue o dado para ver a área.")
            dado2 = dado()
            if dado2 == 1:
                print("O jogador",jogador1,"se formou em direito.")
                direito = True
            if dado2 == 2:
                print("O jogador",jogador1,"se formou em medicina.")
                medicina = True
            if dado2 == 3:
                print("O jogador ",jogador1," se formou em artes visuais.")
                artes = True
            if dado2 == 4:
                print("O jogador",jogador1,"se formou em história.")
                historia = True
            if dado2 == 5:
                print("O jogador",jogador1,"se formou em geografia.")
                geografia = True
            if dado2 == 6:
                print("O jogador",jogador1,"se formou em letras.")
                letras = True
        if casajog1 == 6 or casajog1 == 9 or casajog1 ==13:
            print("Jogador 1 você caiu na casa",casajog1,"você vai ter filhos.")
            filhos = True
            print("jogue o dado para ver se serão gemeos")
            dado3 = dado()
            if dado3 == 5:
                filhojog1 = 2
                filhojog1 += filhojog1
                print("O jogador 1 teve gemeos.")
            if dado3 != 5:
                filhojog1 = 1
                filhojog1 += filhojog1
                print("O jogador 1 teve um filho.")
            filhojog1+=filhojog1
        if casajog1 == 7 or casajog1 == 16:
            print("Jogador 1 você caiu na casa",casajog1,"você vai se casar")
            casaar = True
            print("o jogador 1 casou.")
        if casajog1 == 12:
            print("Jogador 1 caiu na casa",casajog1,"vamos ver se você irá se divorciar.")
            if casaar == True:
                divorciou = True
                print("O jogador 1 você era casado, agora está divorciado.")
            if casaar == False:
                divorciou = False
                print("O jogador 1 não era casado, nada aconteceu.")
        if casajog1 == 14:
            print("Jogador 1 caiu na casa",casajog1,"você ganhou na loteria. Jogue o dado para ver seu prêmio.")
            loterica = True
            dado4 = dado()
            if dado4 == 1:
                print("Ganho 2,50 no bolão.")
            if dado4 == 2:
                print("Ganhou 5 mil.")
            if dado4 == 3:
                print("Ganhou 50 mil.")
            if dado4 == 4:
                print("Ganhou 500 mil.")
            if dado4 == 5:
                print("Ganhou 5 milhões.")
            if dado4 == 6:
                print("Ganhou 100 milhões.")
        if casajog1 == 15:
            print("Jogador 1 você caiu na casa",casajog1,"você vai ser famoso!!!!!!")
            famosso = True
            print("o jogador 1 é famoso")
        if casajog1 == 20:
            print("Jogador 1 você caiu na casa",casajog1,"infelizmente todo seujogo será zerado.")
            reseta = True
            dadinho = mat = formouu = filhos = casaar = divorciou = loterica = famosso = False
            casajog1 = 0
        if casajog1 >= 21:
            print("Jogador 1 você caiu na casa",casajog1,"VOCÊ CONSEGUIU IR ATÉ O FINAL E GANHOU!!!!!")
            print("Fim de jogo.")
            print("Jogador 1 ganhou")
            print("Agora veremos as trajetórias dos jogadores. \n")
            print("Trajetória do jogador 1 ")
            if dadinho == True:
                print("O jogador 1 jogou o desafio do dado.")
            if mat == True:
                print("O jogador 1 jogou o desafio matemático.")
            if formouu == True:
                print("O jogador 1 se formou.")
            if filhos == True:
                print("O jogador 1 teve filho.")
            if casaar == True:
                print("O jogador 1 se casou.")
            if divorciou == True:
                print("O jogador 1 se divorciou.")
            if loterica == True:
                print("O jogador 1 ganhou na loteria")
            if famosso == True:
                print("O jogador 1 é famoso.")
            if reseta == True:
                print("Jogador 1 você teve a vida resetada!!")
            if dadinho == False and reseta == False and mat == False and formouu == False and filhos == False and casaar == False and divorciou == False and loterica == False and famosso == False:
                print("Nada aconteceu na vida do jogador 1.")
            print("Jogador 2 você perdeu vamos ver o seu histórico.")
            if dadinho2 == True:
                print("O jogador 2 jogou o desafio do dado.")
            if mat2 == True:
                print("O jogador 2 jogou o desafio matemático.")
            if formouu2 == True:
                print("O jogador 2 se formou.")
            if filhos2 == True:
                print("O jogador 2 teve filho.")
            if casaar2 == True:
                print("O jogador 2 se casou.")
            if divorciou2 == True:
                print("O jogador 2 se divorciou.")
            if loterica2 == True:
                print("O jogador 2 ganhou na loteria")
            if famosso2 == True:
                print("O jogador 2 é famoso.")
            if reseta2 == True:
                print("O jogador 2 teve a vida resetada!")
            if dadinho2 == False and reseta2 == False and mat2 == False and formouu2 == False and filhos2 == False and casaar2 == False and divorciou2 == False and loterica2 == False and famosso2 == False:
                print("Nada aconteceu na vida do jogador 2.")
            loop = loop1 = False
        if loop1:
            print(30*"-")
            print("Vez do jogador 2! ")
            jog2dado = dado()
            casajog2 += jog2dado
            print("Jogador",jogador2,"vá para a casa",casajog2)
            if casajog2 == 1 or casajog2 == 3 or casajog2 == 10 or casajog2 == 17:
                print("Jogador 2 você vai jogar o desafio do dado. \n")
                print("Jogue o dado, se cair no 1 avança 1 casa, se cair no 3 recua uma casa, e se cair no 6 perdeu uma rodada. \n")
                dadinho2 = True 
                dado5 = dado()
                if dado5 == 1:
                    print("Avança 1 casa")
                    casajog2+=1
                    print(18*"-")
                if dado5 == 3:
                    print("Recua 1 casa.")
                    casajog2 -= 1
                    print(18*"-")
                if dado5 == 6:
                    print("Perde uma rodada.")
                    print(18*"-") 
                    rodada1 = -1
                if dado5 == 2 or dado5 == 4 or dado5 == 5:
                    print("Nada vai acontecer")
                    print(18*"-")
            if casajog2 == 2 or casajog2 == 8 or casajog2 == 18:
                morreu2 = True
                print("Jogador",jogador2,"morreu ao cair na casa",casajog2)
                print("Jogador",jogador2,"vamos ver sua trajetoria.")
                if morreu2 == True:
                    print("O jogador 2 morreu.")
                if dadinho2 == True:
                    print("O jogador 2 jogou o desafio do dado.")
                if mat2 == True:
                    print("O jogador 2 jogou o desafio matemático.")
                if formouu2 == True:
                    print("O jogador 2 se formou.")
                if filhos2 == True:
                    print("O jogador 2 teve filho")
                if casaar2 == True:
                    print("O jogador 2 se casou.")
                if divorciou2 == True:
                    print("O jogador 2 se divorciou.")
                if loterica2 == True:
                    print("O jogador 2 ganhou na loteria")
                if famosso2 == True:
                    print("O jogador 2 é famoso.")
                    if medicina2 == True:
                        print("O jogador 2 se formou em medicina!")
                    if historia2 == True:
                        print("O jogador 2 se formou em história!")
                    if geografia2 == True:
                        print("O jogador 2 se formou em geografia!")
                    if artes2 == True:
                        print("O jogador 2 se formou em artes!")
                    if letras2 == True:
                        print("O jogador 2 se formou em letras!")
                    if direito2 == True:
                        print("O jogador 2 se formou em direito!")
                if reseta2 == True:
                    print("O jogador 2 teve a vida resetada.")
                if dadinho2 == False and reseta2 == False and mat2 == False and formouu2 == False and filhos2 == False and casaar2 == False and divorciou2 == False and loterica2 == False and famosso2 == False:
                    print("Nada aconteceu na vida do jogador 2.")

                print("Jogador 1 você ganhou veja se histórico.")
                if dadinho == True:
                    print("O jogador 1 jogou o desafio do dado.")
                if mat == True:
                    print("O jogador 1 jogou o desafio matemático.")
                if formouu == True:
                    print("O jogador 1 se formou.")
                    if medicina == True:
                        print("O jogador 1 se formou em medicina!")
                    if historia == True:
                        print("O jogador 1 se formou em história!")
                    if geografia == True:
                        print("O jogador 1 se formou em geografia!")
                    if artes == True:
                        print("O jogador 1 se formou em artes!")
                    if letras == True:
                        print("O jogador 1 se formou em letras!")
                    if direito == True:
                        print("O jogador 1 se formou em direito!")
                if filhos == True:
                    print("O jogador 1 teve filho")
                if casaar == True:
                    print("O jogador 1 se casou.")
                if divorciou == True:
                    print("O jogador 1 se divorciou.")
                if loterica == True:
                    print("O jogador 1 ganhou na loteria")
                if famosso == True:
                    print("O jogador 1 é famoso.")
                if reseta == True:
                    print("O jogador 1 teve a vida resetada.")
                if dadinho == False and reseta == False and mat == False and formouu == False and filhos == False and casaar == False and divorciou == False and loterica == False and famosso == False:
                    print("Nada aconteceu na vida do jogador 1.")
                loop = loop1 = False
            if casajog2 == 4 or casajog2 == 11 or casajog2 == 19:
                print("Jogador 2 caiu no desafio matemático, jogue o dado e faça seu desafio.")
                matematica(jogador1)
                mat2 = True
            if casajog2 == 5:
                print("Jogador 2 você vai se formar, você caiu na casa ",casajog2,".Jogue o dado para ver a área.")
                formouu2 = True
                dado6 = dado()
                if dado6 == 1:
                    print("O jogador",jogador2,"se formou em direito.")
                    direito2 = True
                if dado6 == 2:
                    print("O jogador",jogador2,"se formou em medicina.")
                    medicina2 = True
                if dado6 == 3:
                    print("O jogador ",jogador2," se formou em artes visuais.")
                    artes2 = True
                if dado6 == 4:
                    print("O jogador",jogador2,"se formou em história.")
                    historia2 = True
                if dado6 == 5:
                    print("O jogador",jogador2,"se formou em geografia.")
                    geografia2 = True
                if dado6 == 6:
                    print("O jogador",jogador2,"se formou em letras.")
                    letras2 = True
            if casajog2 == 6 or casajog2 == 9 or casajog2 ==13:
                print("Jogador 2 você caiu na casa",casajog2,"você vai ter filhos.")
                filhos2 = True
                dado7 = dado()
                if dado7 == 5:
                    filhojog2 = 2
                    filhojog2 += filhojog2
                    print("O jogador 2 teve gemeos.")
                if dado7 != 5:
                    filhojog2 = 1
                    filhojog2 += filhojog2
                    print("O jogador 2 teve um filho.")
                filhojog2+=filhojog2
            if casajog2 == 7 or casajog2 == 16:
                print("Jogador 2 você caiu na casa",casajog2,"você vai se casar")
                casaar2 = True
                print("o jogador 2 casou.")
            if casajog1 == 12:
                print("Jogador 2 caiu na casa",casajog2,"vamos ver se você irá se divorciar.")
                if casaar2 == True:
                    divorciou2 = True
                    print("O jogador 2 você era casado agora está divorciado.")
                if casaar2 == False:
                    divorciou2 = False
                    print("O jogador 2 não era casado, nada aconteceu.")
            if casajog2 == 14:
                print("Jogador 2 caiu na casa",casajog2,"você ganhou na loteria. Jogue o dado para ver seu prêmio.")
                loterica2 = True
                dado8 = dado()
                if dado8 == 1:
                    print("Ganho 2,50 no bolão.")
                if dado8 == 2:
                    print("Ganhou 5 mil.")
                if dado8 == 3:
                    print("Ganhou 50 mil.")
                if dado8 == 4:
                    print("Ganhou 500 mil.")
                if dado8 == 5:
                    print("Ganhou 5 milhões.")
                if dado8 == 6:
                    print("Ganhou 100 milhões.")
            if casajog2 == 15:
                print("O jogador 2 caiu na casa",casajog2,"Você vai ser famoso.")
                famosso2 = True
                print("o jogador 2 é famoso")
            if casajog2 == 20:
                reseta2 = True
                print("Jogador 2 você caiu na casa",casajog2,"o seu jogo será zerado e você começara novamente.")
                dadinho2 = mat2 = formouu2 = filhos2 = casaar2 = divorciou2 = loterica2 = famosso2 = False
                casajog2 = filhojog2 = 0
            if casajog2 >= 21:
                print("Jogador 2 você caiu na casa",casajog2,"VOCÊ CONSEGUIU IR ATÉ O FINAL E GANHOU!!!!!")
                print("Fim de jogo.")
                print("Jogador 2 ganhou")
                print("Vamos rever as trajetórias dos jogadores \n")
                print("Trajetória do jogador 2 \n")
                if dadinho2 == True:
                    print("O jogador 2 jogou o desafio do dado.")
                if mat2 == True:
                    print("O jogador 2 jogou o desafio matemático.")
                if formouu2 == True:
                    print("O jogador 2 se formou.")
                    if medicina2 == True:
                        print("O jogador 2 se formou em medicina!")
                    if historia2 == True:
                        print("O jogador 2 se formou em história!")
                    if geografia2 == True:
                        print("O jogador 2 se formou em geografia!")
                    if artes2 == True:
                        print("O jogador 2 se formou em artes!")
                    if letras2 == True:
                        print("O jogador 2 se formou em letras!")
                    if direito2 == True:
                        print("O jogador 2 se formou em direito!")
                if filhos2 == True:
                    print("O jogador 2 teve filho")
                if casaar2 == True:
                    print("O jogador 2 se casou.")
                if divorciou2 == True:
                    print("O jogador 2 se divorciou.")
                if loterica2 == True:
                    print("O jogador 2 ganhou na loteria")
                if famosso2 == True:
                    print("O jogador 2 é famoso.")
                if reseta2 == True:
                    print("O jogador 2 teve a vida resetada.")
                if dadinho2 == False and reseta2 == False and mat2 == False and formouu2 == False and filhos2 == False and casaar2 == False and divorciou2 == False and loterica2 == False and famosso2 == False:
                    print("Nada aconteceu na vida do jogador 2.")

                print("Jogador 1 você perdeu vamos ver o seu histórico.")
                if dadinho == True:
                    print("O jogador 1 jogou o desafio do dado.")
                if mat == True:
                    print("O jogador 1 jogou o desafio matemático.")
                if formouu == True:
                    print("O jogador 1 se formou.")
                    if medicina == True:
                        print("O jogador 1 se formou em medicina!")
                    if historia == True:
                        print("O jogador 1 se formou em história!")
                    if geografia == True:
                        print("O jogador 1 se formou em geografia!")
                    if artes == True:
                        print("O jogador 1 se formou em artes!")
                    if letras == True:
                        print("O jogador 1 se formou em letras!")
                    if direito == True:
                        print("O jogador 1 se formou em direito!")
                if filhos == True:
                    print("O jogador 1 teve filho ")
                if casaar == True:
                    print("O jogador 1 se casou.")
                if divorciou == True:
                    print("O jogador 1 se divorciou.")
                if loterica == True:
                    print("O jogador 1 ganhou na loteria")
                if famosso == True:
                    print("O jogador 1 é famoso.")
                if reseta == True:
                    print("O jogador 1 teve a vida resetada.")
                if dadinho == False and reseta == False and mat == False and formouu == False and filhos == False and casaar == False and divorciou == False and loterica == False and famosso == False:
                    print("Nada aconteceu na vida do jogador 1.")
                loop = loop1 = False

jogar = jogo()
