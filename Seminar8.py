import os

class Phonebook():
    def __init__(self, phonebookpath = "phonebook.txt" ):
        self.phonebookpath = phonebookpath
        self.phbook = self.readphonebook()

    def readphonebook(self):
        with open(self.phonebookpath, encoding='utf-8') as p:
            temp = p.read().splitlines()
            phbook =[]
            for line in temp:
                phbook.append(line.split(' '))
            return phbook

    def savephonebook(self):
        surname = input('Введите фамилию-')
        name = input('Введите имя-')
        middlename = input('Введите отчество-')
        phone = input('Введите номер телефона-')
        self.phbook.append([surname,name,middlename,phone])
        input(f'Абонент добавлен')
        self.rewritephonebook()
        

    def selectphonebook(self):
        data = input('Введите имя или фамилию или отчество или номер телефона-')
        for self.line in self.phbook:
            for i in self.line:
                if data.upper() == i.upper():
                    return ' '.join(self.line)
        input('''Такого абонента нет в списке
                [anykey] -- Главное меню ''')
        self.startmenu()
    
    def changephonebook(self):
        clear = lambda: os.system ('cls')
        clear()

        print(f'Выбран: {self.selectphonebook()}')
        print (''' 
        [1] -- Изменить фамилию 
        [2] -- Изменить имя 
        [3] -- Изменить отчество 
        [4] -- Изменить номер телефона
        [5] -- Главное меню''')

        try:
            while True:
                num = int(input())
                if num == 1:
                    self.line[num-1] = input('Введите фамилию-')
                    input(f'Фамилия изменена')
                    self.rewritephonebook()
                elif num == 2:
                    self.line[num-1] = input('Введите имя-')
                    input(f'Имя изменено')
                    self.rewritephonebook()
                elif num == 3:
                    self.line[num-1] = input('Введите отчество-')
                    input(f'Отчество изменено')
                    self.rewritephonebook()
                elif num == 4:
                    self.line[num-1] = input('Введите номер телефона-')
                    input(f'Номер телефона изменен')
                    self.rewritephonebook()
                elif num == 5:
                    self.startmenu()
                else:
                    print('Нет такого пункта, попробуйте еще')
        except:
            print('error. Некорректный ввод')
            exit
                
            

    def removephonebook(self):
        if input(f'Удалить абонента {self.selectphonebook()}? д - да, любая другая клавиша для отмены ').lower() == 'д':
            self.phbook.remove(self.line)
            input(f'Абонент удален')
            self.rewritephonebook()
        else:
           self.startmenu()
            
        

    def rewritephonebook(self):
        with open(self.phonebookpath, 'w+', encoding='utf-8') as p:
            p.seek(0)
            for i in self.phbook:
                p.write(' '.join(i)+'\n')
        self.startmenu()  
        

    def startmenu(self):

        clear = lambda: os.system ('cls')
        clear()

        print ('''Choose your way 
                [1] -- Посмотреть всех 
                [2] -- Поиск абонента
                [3] -- Добавить абонента
                [4] -- Изменить абонента
                [5] -- Удалить абонента
                [6] -- Выход''')
        
        try:
            while True:
                choosenum = int(input())
                if choosenum == 1:
                    with open(self.phonebookpath, encoding='utf-8') as p:
                        print(p.read())
                elif choosenum == 2:
                    print(self.selectphonebook())
                elif choosenum == 3:
                    self.savephonebook()
                elif choosenum == 4:
                    print(self.changephonebook())
                elif choosenum == 5:
                    print(self.removephonebook())
                elif choosenum == 6:
                    exit
                else:
                    print('Нет такого пункта, попробуйте еще')
        except:
            print('error. Некорректный ввод')
            exit
        
userini = Phonebook() 
userini.startmenu()      