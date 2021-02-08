from random import randrange
from emoji import emojize

pedra = emojize(':fist:', use_aliases=True)
papel = emojize(':hand:', use_aliases=True)
tesoura = emojize(':v:', use_aliases=True)
pJog = 0
pCPU = 0
cont = 1
decisao = 's'

while True:
    print('#---------------------#')
    print('# Pedra Papel Tesoura #')
    print('#---------------------#')
    print('#       Placar        #')
    print('# Jogador   |   CPU   #')
    print('#   ',pJog,'     |   ',pCPU,'   #')
    print('#---------------------#')
    print('#  1 -> Pedra   ',(pedra),'  #')
    print('#  2 -> Papel   ',(papel),'  #')
    print('#  3 -> Tesoura ',(tesoura),'   #')
    print('#---------------------#')
    escolhaJogador = input('Escolha sua arma: ')
    escolhaCPU = randrange(3)

    if escolhaCPU == 0:
        txtCPU = pedra
    if escolhaCPU == 1:
       txtCPU = papel
    if escolhaCPU == 2:
        txtCPU = tesoura

    if escolhaJogador == '1':
        txtJog = pedra
    if escolhaJogador == '2':
        txtJog = papel
    if escolhaJogador == '3':
        txtJog = tesoura

    print('Jogador escolheu:',txtJog)
    print('CPU escolheu:',txtCPU)


    if txtJog == pedra and txtCPU == tesoura:
        pJog = pJog+1
        print('Jogador ganhou, possui',pJog,'pontos')
     
    if txtJog == papel and txtCPU == pedra:
        pJog = pJog+1
        print('Jogador ganhou, possui',pJog,'pontos')

    if txtJog == tesoura and txtCPU == papel:
        pJog = pJog+1
        print('Jogador ganhou, possui',pJog,'pontos')

    if txtJog == pedra and txtCPU == papel:
        pCPU = pCPU+1
        print('CPU ganhou, possui',pCPU,'pontos')     

    if txtJog == papel and txtCPU == tesoura:
        pCPU = pCPU+1
        print('CPU ganhou, possui',pCPU,'pontos')
    if txtJog == tesoura and txtCPU == pedra:
        pCPU = pCPU+1
        print('CPU ganhou, possui',pCPU,'pontos')
       
    if txtJog == pedra and txtCPU == pedra:
        print('Empate')
      
    if txtJog == papel and txtCPU == papel:
        print('Empate')
    if txtJog == tesoura and txtCPU == tesoura:
        print('Empate')

    decisao = input('Quer continuar? (S/N): ')

    if decisao == 'n':
        if pJog>pCPU:
            print('Jogador venceu')
        if pJog<pCPU:
            print('CPU venceu')
        break
    if decisao == 'N':
        if pJog>pCPU:
            print('Jogador venceu')
        if pJog<pCPU:
            print('CPU venceu')
        break
