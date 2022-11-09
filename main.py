# Написать игру Black Jack
# Игрок это пользователь, диллер - программа.
# Цель игры - набрать количество очков 21.
# Игроку даются из колоды 2 карты. У карты есть номинал и масть
# Игрок может выполнить действия "Еще" или "Хватит"
# Действие "Еще" - ему дается еще 1 карта
# Если игрок тянет карту и его счет становится больше 21 то он проиграл (дилеру карты не раздаются)
# Действие "Хватит" - карты раздаются диллеру до тех пор пока он не выйграет (больше очков чем у игрока) или не проиграет (наберет более 21)
# В случае если у игрока и дилера одинаковое количество очков - это ничья
# Номиналы карт:
# от 2 до 10 очки соответствуют номиналу
# J, Q, K - 10 очков
# A - 1 или 11 (в пользу игрока)
# /*
# git config --global user.email "you@example.com"
# git config --global user.name "Your Name"
#
#'♠'
#'♣'
#'♥'
#'♦'

import random

def ochki(lis):
 sum_=0 
 for e in lis:
  if e[0].isdigit():
   if int(e[0])>=2 and int(e[0])<=9:
    sum_=sum_+int(e[0])  
   elif int(e[0])==1: 
    sum_=sum_+10
  else:
   if 'JDK'.find(e[0])!=-1:
    sum_=sum_+10  
   if 'A'.find(e[0])!=-1:
    sum_=sum_+11 
 return sum_


print("Игра в карты: Black Jack")
print("Старт")
kart=['2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','D♠','K♠','A♠','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','D♣','K♣','A♣','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','D♥','K♥','A♥','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','D♦','K♦','A♦']
random.shuffle(kart)
# print(kart)
ochKr=0
ochIgr=0
spIgrok=[]
slkrupe=[]
igrokkart_=""
krupekart=""
while True:
 igrokkart_=""
 print("Идет сдача 2 карт")
 spIgrok.append(kart.pop())
 spIgrok.append(kart.pop())
 print("Вам сданы 2 карты ")
 for e in spIgrok:
  igrokkart_+=e+' '
 # print(spIgrok)
 ochIgr=ochki(spIgrok)
 print(f"Вам выпали следующие карты: {igrokkart_} у вас {ochIgr} очков")
 if ochIgr==21:
  print(f"Вы выиграли! Вы набрали {ochIgr} очков")
  break
 while True:
  what=input("Вы хотите получить еще карту? Введите Еще если Хватить и любую клавишу если нет: ")
  if what.upper()=="ЕЩЕ":
   igrokkart_=""
   spIgrok.append(kart.pop())    
   ochIgr=ochki(spIgrok)
   for e in spIgrok:
    igrokkart_+=e+' '
   print(f"Вам выпали следующие карты: {igrokkart_} у вас {ochIgr} очков")
   if ochIgr==21:
    print(f"Вам выпали {igrokkart_}. Вы выиграли! Вы набрали {ochIgr} очков")
    break
   if ochIgr>21:
    print(f"Вам выпали {igrokkart_}. Вы проиграли! Вы набрали {ochIgr} очков")
    break
  elif what.upper()=="ХВАТИТ":
   break
  else:
   break
 print("Крупье сдает себе")
 slkrupe.append(kart.pop())
 slkrupe.append(kart.pop())
 print("Карты крупье 2 карты ")
 ochKr = ochki(slkrupe)
 for e in slkrupe:
  krupekart += e + ' '
 print(f"Карты крупье: {krupekart}  {ochKr} очков")
 print(f"Карты игрока: {igrokkart_}  {ochIgr} очков")
 if ochIgr == ochKr:
  print("У дилера и игрока одинаковое количество очков")
  print(f"У дилера {krupekart} очков {ochKr}")
  print(f"У игрока {igrokkart_} очков {ochIgr}")
 if ochIgr<ochKr:
  print("У дилера меньше очков. Карты сдаются дилеру")
  while ochKr<ochIgr:
   slkrupe.append(kart.pop())
   ochKr = ochki(slkrupe)
   krupekart=""
   for e in slkrupe:
    krupekart += e + ' '
   if ochIgr<ochKr:
    print(f"Дилер выиграл. У дилера {krupekart} очков {ochKr}")
    print(f"У игрока  {igrokkart_} очков {ochIgr}")
   if ochKr>21:
    print(f"Дилер проиграл у него перебор {krupekart} очков {ochKr}")
   if ochIgr == ochKr:
    print("У дилера и игрока одинаковое количество очков")
    print(f"У дилера {krupekart} очков {ochKr}")
    print(f"У игрока {igrokkart_} очков {ochIgr}")
  break

 