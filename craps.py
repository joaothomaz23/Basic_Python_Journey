import random
def jogarCraps():
    n = random.randint(2,12)
    return n
aux = 1
print('ESSE É UM PROGRAMA QUE JOGA CRAPS, SE VOCÊ NÃO SABE AS REGRAS PESQUISE NO GOOGLE')
while aux != 0:
    jogador = int(input('Deseja jogar os dados? (S=1;N=0)'))
    aux = jogador
    if jogador == 1:
        num = jogarCraps()
        print('Você tirou o número: ',num)
        if num == 7 or num == 11:
            print('Parabéns!! Você ganhou!!')
            aux = 0
        elif num == 2 or num == 3 or num == 12:
            print('Que pena! Você perdeu!!')
            aux = 0
        else:
            print('Ponto, você precisa tirar o número {} novamente para ganhar'.format(num))
            aux2 = 1
            while aux2 != 0:
                num2 = jogarCraps()
                jogador2 = int(input('Deseja jogar os dados? (S=1;N=0)'))
                aux2 = jogador2
                if jogador2 == 1:
                    num2 = jogarCraps()
                    print('Você tirou o número: ',num2)
                    if num2 == num:
                        print('Parabèns!! Você ganhou!!')
                        aux2 = 0
                    elif num2 == 7:
                        print('Que pena! Você perdeu!')
                        aux2 = 0
                
                    
            
