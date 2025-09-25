import time
import random
import winsound

print('P.O.M.E.R.')
name = input('WHAT IS YOUR NAME ? ')
print('OK.')

time.sleep(3)
print('БИБА БОБА')
time.sleep(1)
print('OK.')

print(f'{name}, ВЫБОРА У ТЕБЯ НЕТ.')
print('ПОМЕР - ВИНТОВКА. 35-50 АТК/ВЫСТРЕЛ.')

enemyHP = random.randint(250, 500)
playerHP = random.randint(250, 500)

while True:
  c = input(f'{name}, 1 - ВЫСТРЕЛИТЬ 2 - СДАЮСЬ. ХП - {playerHP}. ХП ВРАЖИНЫ - {enemyHP}.')
  if c == 1:
    winsound.Beep(800, 500)
    enemyHP - random.randint(35, 50)
    print(f'ХЕРАК, У ВРАЖИНЫ {enemyHP}')
    winsound.Beep(750, 500)
    playerHP - random.randint(35, 50)
    print(f'АЙ, БОЛЬНО В НОГЕ, {playerHP} ХП')
