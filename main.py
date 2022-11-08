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
print(kart)
spIgrok=[]
slDiler=[]

while True:
 print("Идет сдача 2 карт")
 # spIgrok('K♦')
 # spIgrok('A♦')
 spIgrok.append(kart.pop())
 spIgrok.append(kart.pop())

 print("Вам сданы 2 карты ")
 print(spIgrok)
 s=ochki(spIgrok)
 kart_=""
 for e in spIgrok:
  kart_+=e+' ' 
 print(f"Вам выпали следующие карты: {kart_} у вас {s} очков")  
 if s==21:
  print(f"Вы выиграли! Вы набрали {s} очков")
  break
 while True:
  what=input("Вы хотите получить еще карту? Введите Еще если Хватить и любую клавишу если нет: ")
  if what.upper()=="ЕЩЕ":
   kart_=""
   spIgrok.append(kart.pop())    
   s=ochki(spIgrok)
   for e in spIgrok:
    kart_+=e+' '
   print(f"Вам выпали следующие карты: {kart_} у вас {s} очков")
   if s==21:
    print(f"Вам выпали {kart_}. Вы выиграли! Вы набрали {s} очков")
    break
   if s>21:
    print(f"Вам выпали {kart_}. Вы проиграли! Вы набрали {s} очков")
    break
  elif what.upper()=="ХВАТИТ":
   break
  else:
   break

 break

 