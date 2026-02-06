import time
# Параллелизм делит ресурсы компьютера на несколько потоков, компьютер быстро переключается
"""multiprocessing - независимость выполнения вычислений.
В отличии от потоков threading, процесс имеет собственное ядро"""

# GIL - Global Interpreter Lock.
# Не позвояет работать с несколькими потоками на уровни интерпритатора.

# num = 2
#
# def thread_1():
#     global  num
#     num += 2
#
# def thread_2():
#     global num
#     num *=3
# print(thread_1())
# print(thread_2())

# исследование разных потоков параллельного вычисления python

# import time
#
# def heavy(n):
#     for x in range(1,n):
#         for y in range(1,n):
#             x**y
#
# def sequence(n):
#     for i in range(n):
#         heavy(500)
#     print(f"{n} cycle compleat")
#
# if __name__ == "__main__":
#     start = time.time()
#     sequence(80)
#     end = time.time()
#     print(" All time program work", end - start)



# # Использование потоков
# import time
#
# def heavy(n):
#     for x in range(1,n):
#         for y in range(1,n):
#             x**y
#
# def sequence(n):
#     for i in range(n):
#         heavy(500)
#     print(f"{n} cycle compleat")
#
# if __name__ == "__main__":
#     start = time.time()
#     sequence(80)
#     end = time.time()
#     print(" All time program work", end - start)


# Threads
# import threading
# import time
#
#
# def heavy(n, i, thead):
#     for x in range(1, n):
#         for y in range(1, n):
#             x ** y
#     print(f"Цикл № {i}. Поток {thead}")
#
#
# def sequential(calc, thead):
#     print(f"Запускаем поток № {thead}")
#     for i in range(calc):
#         heavy(500, i, thead)
#     print(f"{calc} циклов вычислений закончены. Поток № {thead}")
#
#
# def threaded(theads, calc):
#     # theads - количество потоков
#     # calc - количество операций на поток
#
#     threads = []
#
#     # делим вычисления на `theads` потоков
#     for thead in range(theads):
#         t = threading.Thread(target=sequential, args=(calc, thead))
#         threads.append(t)
#         t.start()
#
#     # Подождем, пока все потоки
#     # завершат свою работу.
#     for t in threads:
#         t.join()
#
#
# if __name__ == "__main__":
#     start = time.time()
#     # разделим вычисления на 4 потока
#     # в каждом из которых по 20 циклов
#     threaded(4, 20)
#     end = time.time()
#     print("Общее время работы: ", end - start)

# Имитация однопоточного режима работы
#
# import threading
# import time
#
# def heavy():
#     # имитации операций ввода-вывода
#     time.sleep(2)
#
# def threaded(theads):
#     threads = []
#
#     # делим операции на `theads` потоков
#     for thead in range(theads):
#         t = threading.Thread(target=heavy)
#         threads.append(t)
#         t.start()
#
#     # Подождем, пока все потоки
#     # завершат свою работу.
#     for t in threads:
#         t.join()
#     print(f"{theads} циклов имитации операций ввода-вывода закончены")
#
# if __name__ == "__main__":
#     start = time.time()
#     # 80 потоков - это неправильно и показано
#     # чисто в демонстрационных целях
#     threaded(80)
#     end = time.time()
#     print("Общее время работы: ", end - start)
#

# 80 циклов имитации операций ввода-вывода закончены
# Общее время работы:  2.008725881576538
