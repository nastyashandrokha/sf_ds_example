"""Игра "Угадай число"
Компьютер загадывает число и угадывает его меньше, чем за 20 попыток 
"""

import numpy as np

def random_predict(number: int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0  
    first_number = 0
    last_number = 101
    mean_number = 50
    predict_number = np.random.randint(1, 101) #Предполагаемое число
    
    while mean_number != predict_number:
        count += 1
        mean_number = (first_number+last_number)//2
        if predict_number > mean_number:
            first_number = mean_number
        else:
            last_number = mean_number
    return(count)

print(f"Программа угадала число за {random_predict()} попыток")


def score_game(random_predict) -> int:
    """Проверка - за какое количество попыток программа угадает число за 1000 подходов

    Args:
        random_predict (_type_): Функция угадывания числа

    Returns:
        int: Среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) #Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) #Загываем список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает в среднем за {score} попыток')
    return score

if __name__ == '__main__':
#RUN
    score_game(random_predict)