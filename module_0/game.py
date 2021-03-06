import numpy as np


def get_mean(num_1, num_2):
    """Функция возвращает медианное число типа int из двух заданных"""
    mean = int(np.mean(range(num_1, num_2 + 1)))  # поиск медианного числа
    return mean  # возвращает медианное число


def game_core_v3(number):
    """Угадывает путем называния медианного числа среди ряда возможных"""
    count = 1  # счетчик попыток
    min_num = 1  # минимальное число в ряде возможных чисел
    max_num = 100  # максимальное число в ряде возможных чисел
    predict = get_mean(min_num, max_num)  # предполагаемое число
    while number != predict:  # цикл пока не угадали число
        count += 1  # +1 к счетчику попыток
        if number > predict:  # если загаданное число больше предполагаемого
            min_num = predict + 1  # меняет минимальное число ряда возможных
        elif number < predict:  # если загаданное число меньше предполагаемого
            max_num = predict - 1  # меняет максимальное число ряда возможных
        predict = get_mean(min_num, max_num)  # вычисляет предполагаемое число
    return count  # возвращает кол-во попыток


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []  # список с количеством попыток, за которые удалось угадать число
    np.random.seed(1)  # фиксирует RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)  # список из 1000 чисел от 1 до 100
    for number in random_array:  # цикл для каждого числа из списка
        count_ls.append(game_core(number))  # запускает игру и добавляет к списку попыток за сколько удалось угадать
    score = int(round(np.mean(count_ls)))  # определение среднего числа попыток
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")  # вывод на экран среднего количества попыток
    return score  # возвращает среднее количество попыток


score_game(game_core_v3)
