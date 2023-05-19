#Lesson1. Задача2

num = int(input('Введите трехзначное число: '))
sum1 = num//100
num = num - sum1 * 100
sum2 = num// 10
num = num - sum2 *10

print(sum1 + sum2 + num)

#Задача4

s = int(input('Сделано журавликов всего: '))
x = int(s/6)    # Петя = Серёжа = x, Петя + Серёжа = 2x, Катя = 4x => 6x = s
print (f'Петя-{x} Серёжа-{x} Катя-{4*x}')
if s%6 != 0:
    print(f'Возможно, остальные дети еще-{s%6}')

#Задача6

ticket = int(input('Введите номер билета: '))
num1 = ticket//100000
ticket = ticket - num1 * 100000
num2 = ticket// 10000
ticket = ticket - num2 *10000
num3 = ticket// 1000
ticket = ticket - num3 *1000
num4 = ticket// 100
ticket = ticket - num4 *100
num5 = ticket// 10
ticket = ticket - num5 *10
if num1 + num2 + num3 == num4 + num5 + ticket:
    print('Билет счастливый')
else:
    print('Билет обычный')

#Задача8

m = int(input('Введите количество долек в высоту: '))
n = int(input('Количество долек в ширину: '))
k = int(input('Сколько долек хотите отломить: '))

if (k<m and k<n) or (k >= m*n and (m%k != 0 or n%k != 0 or k%m != 0 or k%n != 0)):
    print('Это невозможно!')
else:
    print('Можно отломать!')
    
