import random
n = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')

def is_valid(text):
    if text.isdigit() and 1 <= int(text) <= 100:
        return True
    else:
        return False

counter = 0

while True:
    x = input('Введите целое число от 1 до 100 включительно: ')
    if not is_valid(x):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    x = int(x)
    counter += 1
    if x > n:
        print('Ваше число больше загаданного, попробуйте еще разок')
    elif x < n:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    else:
        print('Вы угадали, поздравляем!')
        if counter == 1:
            print('Вы угадали с первого раза!')
        elif counter < 8:
            print(f'Вы угадали с {counter} попыток')
        else:
            print(f'Вы угадали с {counter}-ой попытки')
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break