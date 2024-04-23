import random
number = random.randint(1,100)
while True:
    answer = int(input('Введите число:'))
    if answer == number:
        print('Вы правы!')
        break
    elif answer > number:
        print('Нужно <')
    elif answer < number:
        print('Нужно >')
    elif answer == 101:
        break
    