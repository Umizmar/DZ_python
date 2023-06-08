# Seminar 6

# Задача 30


a1 = int(input('первый элемент '))
d = int(input('разность '))
n = int(input('количество элементов '))

for i in range(n):
    print(a1+i*d)


# Задача 32
nums = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min = int(input('минимальное число '))
max = int(input('максимальное число '))
for i in range(len(nums)):
    if min <= nums[i] <= max:
        print (i, end=' ')