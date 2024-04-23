import random
number = random.randint(1,100)
while True:
    answer = int(input('Введите число:'))
    if answer == number:
        break
    elif answer > number:
        print('Нужно <')
    elif answer < number:
        print('Нужно >')
    elif answer == 101:
        break

print('Поздравляю вы угадали число!')   
