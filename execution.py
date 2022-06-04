import random
from pandas import DataFrame
#import numpy as np
import json


# контроль правильности ввода
def chk_in(text):
    while True:
        try:
            x = int(input(text))
            break
        except ValueError:
            print("Что-то пошло не так :( Попробуйте, пожалуйста, ещё раз: цифры нужно вводить цифрами :) ")
    return(x)

# определение количества быков и коров в паре чисел
def bk(number_2_guess, guess_try):
    b = 0 # количество быков
    k = 0 # количество коров
    common = set(number_2_guess) & set(guess_try) # находим пересечение множества цифр загаданного числа и введенного
    if len(common) != 0:
        for el in list(common):
            if number_2_guess.index(el) == guess_try.index(el):
                b += 1
            else:
                k += 1
    return((b,k))

# Подпрограмма "игрок угадывает число, загаданное компьютером". Возвращает число ходов игрока до победы
def user_guess():
        print("Я загадал 4-значное число, все цифры которого различны. Попробуй его угадать:")
        num_list = list(range(10)) 
        num_list1 = [str(i) for i in num_list]
        to_guess = random.sample(num_list1, 4)
        num_2_guess = ''.join(to_guess)
        tries_count = 0
        while True:
            guess_try = str(chk_in('попытка №' + str(tries_count + 1) + ': '))
            while len(guess_try) < 4:
                guess_try = '0' + guess_try
            tries_count += 1
            ans = bk(list(num_2_guess), list(guess_try))
            if ans[0] < 4:
                print('Быков: ', ans[0], ', коров: ', ans[1])
            elif ans[0] == 4:
                print("Ура! Ты угадал моё число!")
                print('Число попыток, всего-навсего: ', tries_count)
                break
        return(tries_count)
    
# Подпрограмма "компьютер угадывает число, загаданное игроком". Возвращает число ходов компьютера до победы
def comp_guess():
    turn = 0
    input('Загадайте число из четырёх разных цифр. Когда будете готовы, нажмите Enter.')
    answer = combinations
    while True:
        turn += 1
        new_answer = []
        guess = answer[0]
        print('Предположим ', ''.join(guess))
        by = chk_in('Сколько угадано быков? ')
        cow = chk_in('Сколько угадано коров? ')
        while by + cow > 4:
            print('Быков и коров не может быть больше четырёх, посчитайте ещё раз, пожалуйста :)')
            by = chk_in('Сколько угадано быков? ')
            cow = chk_in('Сколько угадано коров? ')
        if (by, cow) == (4, 0):
            print('Вы загадали', ''.join(guess))
            break
        for var in answer:
            if bk(var, guess) == (by, cow):
                new_answer.append(var)
        answer = new_answer
        if len(answer) == 1:
            print('Вы загадали', ''.join(answer[0]))
            break
        if len(answer) == 0:
            print('Вы где-то ошиблись :(')
            turn = 0
            break
    return(turn)
	
# подготовка к игре
combinations = [] #список всех допустимых последовательностей
for i in range(123, 9877):
    if i < 1000:
        a = ['0']
    else:
        a = []
    for j in str(i):
        a.append(j)
    if len(a) == len(set(a)):
        combinations.append(tuple(a))
        

# обеспечение учета результатов игроков
def sort_rating(rating_table):
    """"Сортировка словаря с данными о результатах игроков по возрастанию результата"""
    sorted_rating = {}
    sorted_keys = sorted(rating_table, key=rating_table.get)
    for w in sorted_keys:
        sorted_rating[w] = rating_table[w]

    return sorted_rating


def add_new_user(username, personal_best, rating_table):
    """"Добавление нового резльтата в словарь (датафрейм формируется при необходимости)"""
    if username not in rating_table.keys():
        rating_table[username] = personal_best
    else:
        if rating_table[username] > personal_best:
            rating_table[username] = personal_best
            
        else:
            rating_table[username] += 0
            
            
    result = sort_rating(rating_table)
    return result


with open("users_rating_dict.json", "r") as json_file: #читаем из файла словарь с данными о результатах игроков
    users_rating_dict_json = json_file.read()
users_rating_dict = json.loads(users_rating_dict_json)


# НАЧАЛО ИГРЫ
# небольшое приветствие для игрока
print('Это игра БЫКИ И КОРОВЫ! Кто готов напрячь мозги и повеселиться?')
print('* * * * *')
# правила игры
print('Немного о сути и ходе игры')
print('')
print('Суть игры:')
print('Цель логической игры "Быки и Коровы" -- за наименьшее количество попыток угадать, какое число загадано противником (цифра в числе не повторяются!). В нашем случае пользователь соревнуется с искусственным интеллектом!')
print('')
print('Как же числа отгадываются? В этом помогают обозначения в виде быков и коров. Бык -- это такая цифра задуманного числа, которое стоит на ВЕРНОЙ позиции. Корова -- это цифра задуманного числа, которая стоит НЕ НА СВОЕЙ позиции.')
print('')
a = ''.join(random.choice(combinations))
b = ''.join(random.choice(combinations))
ab = bk(a,b)
print('Например, загадано число ', a, 'Противник говорит: ', b, '. Ответом на такую попытку будет: быков -', ab[0], 'и коров -', ab[1])
print('')
print('Ход игры:')
print('1. Пользователь вводит своё имя, а также указывает числом количество раундов игры.')
print('* * *')
print('2. По окончании каждого раунда у игрока спрашивается, хочет ли он продолжить дальше (вдруг указано большое количество раундов). Если ответ отрицательный, то тогда итог подводится на основании сыгранных раундов, даже если сыгран один раунд.')
print('* * *')
print('3. В начале каждого раунда разыгрывается, кому достаётся первый ход: пользователю или компьютеру.')
print('* * *')
print('4. Если первый ход достаётся пользователю, то тогда он отгадывает число, загаданное компьютером.')
print('* * *')
print('5. Если первый ход достаётся компьютеру, то тогда он отгадывает число, загаданное игроком. Во время того, как компьютер делает попытки угадать число, пользователь должен внимательно вписывать в качестве ответов, сколько быков и коров получилось в этой попытке.')
print('* * *')
print('6. После того, как кончились все раунды, происходит подсчёт баллов и выдаётся окончательный результат.')
print('')
print('НАЧНЁМ ИГРУ!')

username = input('Введите Ваше имя: ')
print('* * * * *')
print('Сколько раундов Вы хотели бы разыграть? Введите количество раундов ниже')
number_rounds = chk_in('Желаемое число раундов: ')
win_user = 0 # кол-во побед игрока
win_computer = 0 # кол-во побед компьютера
for i in range(number_rounds):
    print('РАУНД ', i + 1)
    # задаём, кто первым загадывает
    first_turn = random.choice('12')
    if first_turn == '1':
        print('Первый ход достаётся игроку', username)
        fs_u = user_guess() # число ходов, за которое задуманное число отгадано игроком
        fs_c = comp_guess() # число ходов, за которое задуманное число отгадано компьютером
        while fs_c == 0:
            if input('Давайте переиграем? Д/Н ').lower() == 'д':
                fs_c = comp_guess()
            else:
                print('Жаль, но тогда победа за компьютером...')
                break
    if first_turn == '2':
        print('Первый ход достаётся компьютеру')
        fs_c = comp_guess() # число ходов, за которое задуманное число отгадано компьютером
        while fs_c == 0:
            if input('Давайте переиграем? Д/Н ').lower() == 'д':
                fs_c = comp_guess()
            else:
                print('Жаль, но тогда победа за компьютером...')
                break
        fs_u = user_guess() # число ходов, за которое задуманное число отгадано игроком
    
    print('Вы угадали число за ', fs_u, 'ходов.', 'Компьютер угадал число за', fs_c, 'ходов')


"""Теперь у нас есть все данные для пополнения словаря"""
users_rating_dict = add_new_user(username, fs_u, users_rating_dict) # добавляем данные в словарь
users_rating_dict_json = json.dumps(users_rating_dict)
with open("users_rating_dict.json", "w") as json_file:
    json_file.write(users_rating_dict_json)
    
    
    	#начинаем считать победы за раунд
    if fs_c > fs_u:
        win_user += 1 # плюсик к победам игрока
        print('Итог раунда: победа игрока ', username, '! Поздравляем!')
    if fs_c < fs_u:
        print('Итог раунда: победа компьютера!', username,', не расстраивайтесь! У Вас всё обязательно получится!')
        win_computer += 1 #плюсик к победам компьютера
    if fs_c == fs_u:
        print('Это ничья! Игра становится волнительнее!')
        win_user += 1
        win_сomputer += 1
#начинаем считать кол-во побед всего
if win_user > win_computer:
    print('Победа игрока', username, '! Вы молодец!')
if win_user < win_computer:
    print('Победа компьютера!', username, ', не расстраивайтесь! Всё ещё впереди!')
if win_user == win_computer:
    print('Ничья! Искусственному интеллекту довольно тяжело тягаться с Вами!')


print('А вот табличка с текущими результатами игроков:\n')
users_table = DataFrame(list(users_rating_dict.items()), columns = ['Username', 'Personal best'])
print(users_table)


input('До новых встреч! Нажмите Enter для завершения.')
