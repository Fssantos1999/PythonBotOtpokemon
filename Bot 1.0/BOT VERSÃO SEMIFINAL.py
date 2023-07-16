import pyautogui as bot
from time import sleep
import numpy as np
import keyboard
verde = (1054,40,21,12)
atacar = (1724,701,178,116)
region = bot.locateOnScreen('attack.png', confidence=0.8, region=atacar, grayscale=True)
vida = 0
hky = ('1','2','3','4','5')
#===================CORDENADAS PARA O BOT==============================
# ===================================================================== 
#AQUI ELE SELECIONA AS CORDENADAS QUANDO O A BOX COM O PEIXE VERDE ACESSO APARECE
peixe = input('Pesque um peixe e assim que ele estiver verde, Digite V E PRESSIONE ENTER')
if peixe == 'v':
    verde1= bot.locateOnScreen ('fish.png')
    print (verde1)
    sleep (2)
#AQUI O BOT PEGA A CORDENADA PARA CLICAR QUANDO O PEIXE VERDE APARECER
clicar = input('Selecione onde clicar  quando o peixe  estiver verde, Digite V E PRESSIONE ENTER')
if clicar =='v':
    clicar1 = bot.position()
    print (clicar1)
#SELECIONAR AGUA PARA PESCAR
ag = input('Selecione o lugar para pescar, MOVA O MOUSE PARA UM DIREÇÃO SOBRE A AGUA E Digite V ')
if ag == 'v': 
    agua = bot.position()
#========ATACAR==================================
atk= input('Selecione onde clicar na box para atacar o pokemon,Mas primiero pesque um pokemon para que a box seja reconhecida. Digite V E PRESSIONE ENTER')
if  atk == "v": 
    atk1 = bot.locateOnScreen('attack.png')
#==========SUBSTITUIR POKEMON ========================
life = print ('CASO O POKEMON MORRA SUBSTITUIRA POR OUTRO')

seg1=str(input("posicione seu mouse e digite s para marcar outro poke caso o seu morra 1 ")).lower
if seg1 == "s":
    sem1=bot.position()
seg2=str(input("posicione seu mouse e digite s para marcar outro poke caso o seu morra 2: ")).lower
if seg2 == "s":
    sem2=bot.position()
seg3=str(input("posicione seu mouse e digite s para marcar outro poke caso o seu morra 3: ")).lower
if seg3 == "s":
    sem3=bot.position()


#FUNÇÕES QUE O BOT EXECUTARA 
while True: 
    if bot.locateOnScreen('fish.png',confidence=0.8,region=verde1) != None:
        bot.moveTo(clicar1)
        bot.leftClick(clicar1)
        bot.moveTo(agua)
        sleep (1)
        bot.press ('h')
        bot.leftClick()
    if bot.locateOnScreen('attack.png',confidence=0.8,region=atk1,grayscale=True) != None:
        bot.moveTo(atk1)
        bot.leftClick(atk1) 
        sleep(0.5)
        bot.press(hky)
    if bot.locateOnScreen ('vida2.png'):
        if vida == 0: 
            bot.moveTo(sem1)
            sleep (0.5)           
            bot.click(sem1)
            bot.press(hky)
            sleep(1)
            vida +=1 
    if bot.locateOnScreen ('vida2.png'):
        if vida==1:
            bot.moveTo(sem2)
            sleep(0.5)
            bot.click(sem2)
            bot.press(hky)
            sleep(1)
            vida +=1
    if bot.locateOnScreen ('vida2.png'):     
        if vida==2: 
            bot.moveTo(sem3)
            sleep(1)
            bot.click(sem3)
            bot.press(hky)
        else:
            bot.press("shift" + ' q ' )          

