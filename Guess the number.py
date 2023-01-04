from random import randint


def is_valid(strin, n):
    if strin.isdigit():
        if 1 <= int(strin) <= (n + 1):
            return True
        else:
            return False
    else:
        return False


def check_answer():
    answer = input('Сыграем еще? ').lower()
    if answer == 'да':
        game_body()
    elif answer == 'нет':
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
    else:
        print('Введите ответ: \'да\' или \'нет\' ')
        check_answer()


def game_body():
    print('Добро пожаловать в числовую угадайку')
    n = input('Введите число для правой границы диапазона: ')
    while not n.isdigit():
        n = input('Введите ЧИСЛО для правой границы диапазона: ')
    n = int(n)
    number = randint(0, n)
    user_number = 0
    counter = 0
    while number != user_number:
        print('Введите число от 1 до', n)
        user_number = input()
        if not is_valid(user_number, n):
            print('А может быть все-таки введем целое число от 1 до', n)
        else:
            user_number = int(user_number)
            counter += 1
            if number > user_number:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif number < user_number:
                print('Ваше число больше загаданного, попробуйте еще разок')
            elif number == user_number:
                print('Вы угадали, поздравляем!')
    print('Число ваших попыток', counter)
    check_answer()


game_body()
input('Для выхода нажмите ENTER')
