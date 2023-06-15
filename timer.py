import time

def timer(seconds):
    print("Таймер запущен на", seconds, "секунд.")

    while seconds > 0:
        print("Осталось времени:", seconds, "секунд.")
        time.sleep(1)
        seconds -= 1

    print("Таймер завершен.")

# Пример использования программы
seconds = int(input("Введите количество секунд для таймера: "))
timer(seconds)
