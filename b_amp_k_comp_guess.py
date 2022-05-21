def bk(number_2_guess, guess_try):
    b = 0 # количество быков
    k = 0 # количество коров
    common = set(number_2_guess) & set(guess_try) # находим пересечение множества цифр загадонного числа и введенного
    if len(common) != 0:
        for el in list(common):
            if number_2_guess.index(el) == guess_try.index(el):
                b += 1
            else:
                k += 1
    return((b,k))

combinations = [] #все допустимые последовательности
for i in range(123, 9877):
    if i < 1000:
        a = ['0']
    else:
        a = []
    for j in str(i):
        a.append(j)
    if len(a) == len(set(a)):
            combinations.append(tuple(a))
        
def comp_guess():
    turn = 0
    print('Загадайте число из четырёх разных цифр')
    answer = combinations
    while True:
        turn += 1
        new_answer = []
        guess = answer[0]
        print('Предположим', ''.join(guess))
        by = int(input('Сколько быков? '))
        cow = int(input('Сколько коров? '))
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
    
