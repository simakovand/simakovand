count = 0
while count <= 10:
    on = input('Введите "а" для замыкания или размыкания цепи: ')
    if on == 'a' and count %2 == 0:
        print ('Лампочка выключена')
        count += 1
    else:
        print ('Лампочка включена')
        count +=1
