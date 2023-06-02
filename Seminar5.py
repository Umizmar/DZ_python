# Задача 26

def degree(a,b,res):    
    if b == 1:
        return res
    res *=a
    return degree(a,b-1,res)

a = int(input('Число '))
b = int(input('Степень '))
print(f(a,b,a))

# Задача 28

def sum_num(a,b):
    if b == 0:
        return a
    return sum_num(a+1,b-1)


a = int(input('Первое число '))
b = int(input('Второе число '))
print(sum_num(a,b))