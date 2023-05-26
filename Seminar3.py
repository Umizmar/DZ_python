# Lesson3. Задача 16

import random

arr_num = int(input('Сколько чисел в массиве? '))
num = int(input('Ваше число- '))
arr = [random.randint(0, 10) for _ in range(arr_num)]
count = 0

for i in arr:
    if i == num:
        count += 1

print(arr)
print (count)

# Задача 18

arr_num = int(input('Сколько чисел в массиве? '))
x = int(input('Ваше число- '))
arr = [random.randint(0, 10) for _ in range(arr_num)]

num = abs(arr[0] - x)
m = arr[0]
for i in range(len(arr)):
    if abs(arr[i] - x) < num:
        num = abs(arr[i] - x)
        m = arr[i]

print(arr)
print(f'Наиболее близкое число от начала массива-{m}')

# Задача 20

world = str.upper(input('Ваше слово только английскими или только русскими буквами- '))
score = {"1":['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
         '2':['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'],
         '3':['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'],
         '4':['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'],
         '5':['K', 'Ж', 'З', 'Х', 'Ц', 'Ч'],
         '8':['J', 'X', 'Ш', 'Э', 'Ю'],
         '10':['Q', 'Z', 'Ф', 'Щ', 'Ъ']}
world_score = 0

for letter in world:
    for point, letters in score.items():
        if letter in letters:
            world_score += int(point)

print(world_score)