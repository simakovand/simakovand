
a = True
while True:
    on = input ('Введите "а" для замыкания или размыкания цепи, \n\
А если хотите выйти, напишите "exit": ')
    if on == 'a' and a == True:
        print ('Лампочка включена')
        if a == True:
            a = False
#        print(a)
    elif on == 'a' and a == False:
        if a == False:
            a = True
        print('Лампочка выключена')
#        print(a)
    elif on == 'exit':
        break
    else:
        print ('Лампочка выключена')
#        print(a)
