count = 0
#while count <= 10:
while True:
    on = input ('Введите "а" для замыкания или размыкания цепи, \n\
А если хотите выйти, напишите "exit": ')
    if on == 'a' and count %2 == 0:
        print ('Лампочка выключена')
        count += 1
    elif on == 'exit':
        break
    else:
        print ('Лампочка включена')
        count +=1
