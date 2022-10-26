import random
n = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')

def is_valid(text):
    if text.isdigit() and 1 <= int(text) <= 100:
        return True
    else:
        return False

while True:
    x = input('Введите целое число от 1 до 100 включительно: ')
    if not is_valid(x):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    x = int(x)
    if x > n:
        print('Ваше число больше загаданного, попробуйте еще разок')
    elif x < n:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    else:
        print('Вы угадали, поздравляем!')
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break