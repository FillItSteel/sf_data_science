import numpy as np

number = np.random.randint(1, 101) # загадываем число
count = 0

while True:
    count += 1
    print("Угадай число от 1 до 100")
    predict_number = int(input())

    if predict_number > number:
        print("Число должно быть меньше!")

    elif predict_number < number:
        print("Число должно быть больше!")

    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break # конец игры, выход из цикла