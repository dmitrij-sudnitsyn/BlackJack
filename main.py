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
import random
print("Игра в карты: Black Jack")
print("Старт")
kart=[6,7,8,9,10,'J','D','K','A']*4
print(kart)
spIgrok=[]
slDiler=[]
a=""
random.shuffle(kart)
while True:
 print("Идет сдача 2 карт")   
 try:
  a=kart.pop()  
  print(a)  
  spIgrok.append(int(a))    
 except ValueError:
  if 'JDK'.find(a):
   spIgrok.append(10)     
  if 'A'.find(a):
   spIgrok.append(11)     

 try:
  a=kart.pop()  
  print(a)
  spIgrok.append(int(a))    
 except ValueError:
  if 'JDK'.find(a):
   spIgrok.append(10)     
  if 'A'.find(a):
   spIgrok.append(11)     
 break  
print(spIgrok)



# for e in kart:
#   print(e," ")  
# # //while  