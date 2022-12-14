import random
print('Добро пожаловать в числовую угадайку')

def is_valid(text, num):
    if text.isdigit() and 1 <= int(text) <= num:
        return True
    else:
        return False

game = True
while game:
    print()
    counter = 0
    print('Если хотите задать до какого числа будем играть,')
    max_digit = input('введите его, иначе будет от 1 до 100: ')
    if max_digit.isdigit():
        n = random.randint(1, int(max_digit))
    else:
        max_digit = 100
        n = random.randint(1, max_digit)
    print()

    while True:
        x = input(f'Введите целое число от 1 до {max_digit} включительно: ')
        if not is_valid(x, int(max_digit)):
            print(f'А может быть все-таки введем целое число от 1 до {max_digit}?')
            print()
            continue
        x = int(x)
        counter += 1
        if x > n:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif x < n:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        else:
            if counter == 1:
                print('Вы угадали с первого раза! Поздравляем!')
            elif counter < 8:
                print(f'Вы угадали с {counter} попыток, поздравляем!')
            else:
                print(f'Вы угадали с {counter}-ой попытки, поздравляем!')
            break
        print()
    print()
    answer = input('Сыграем еще? Ответьте да или нет: ')
    while not answer.lower() in ['да', 'нет']:
        print()
        answer = input('Я вас не понимаю, введите "да" или "нет": ')
        if answer.lower() in ['да', 'нет']:
            break
    if answer.lower() == 'нет':
        break
print()
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')