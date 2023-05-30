# Lesson 4. Задача 22

import random

num1 = int(input('Первое число '))
num2 = int(input('Второе число '))
arr1 = [random.randint(0, 10) for _ in range(num1)]
arr2 = [random.randint(0, 10) for _ in range(num2)]

set1 = set(arr1)
set2 = set(arr2)

print(list(set1.intersection(set2)))


# Задача 24

N = random.randint(5, 10)
trees = [random.randint(20, 100) for _ in range(N)]
trees_up = [trees[-1],*trees[:],trees[0]]
tree_indx = 0

result = sum(trees_up[:3])


for i in range(len(trees_up)-2):
    if sum(trees_up[i:i+3]) > result:
        result = sum(trees_up[i:i+3])
        tree_indx = i-1


print(trees)
print(result)
print(trees[tree_indx])