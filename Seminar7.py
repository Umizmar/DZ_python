# Seminar 7

# Задача 34:  

poem = 'пара-ра-рам рам-пам-папам па-ра-па-да'

def vowels_count(world:str):
    vowels_list = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
    vowels = 0
    for i in world:
        if i in vowels_list:
            vowels +=1
    return vowels

def ritm(ritm_list):
    for i in ritm_list:
        if i != ritm_list[0]:
            return 'Пам парам'
    return 'Парам пам-пам'

print (ritm(list(map(vowels_count,poem.split(' ')))))



# Задача 36:

def print_operation_table(operation, num_rows=6, num_columns=6):
    for x in range (num_columns):
        print()
        for y in range (num_rows):
             print (operation(x+1,y+1), end =" ")
             
    
print_operation_table(lambda x, y: x * y)