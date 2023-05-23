#Lesson2. Задача10
import random

coin_num = int(input('Сколько всего монеток? '))
coin_list = [random.randint(0, 1) for _ in range(coin_num)]
tails = eagle = 0

for i in coin_list:
    if i == 0:
        tails +=1
    else:
        eagle +=1

print(coin_list)
print(f'Минимальное количество переворотов - {eagle if eagle < tails else tails}')



# Задача 12
 
sum = int(input('Сумма? '))
mult = int(input('Произведение? '))

for i in range(1000):
    for j in range(1000):
        if i + j == sum and i * j == mult:
            break
        
    if i + j == sum and i * j == mult:
        print(f'Эти числа - {i} и {j}')
        break
else:
    print('Решения нет')


        

# Задача 14

N = int(input('Введите число '))
k = 0
while 2**k < N:
    print( 2**k, end = ' ')
    k +=1

    