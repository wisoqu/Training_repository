# корутина - сопрограмма
# футура - вьючерс
# таска - задачи
# import  time
#
# def func_1(x):
#     print(x**2)
#     time.sleep(3)
#     print(f'work {func_1.__name__} is over')
#
# def func_2(x):
#     print(x**3)
#     time.sleep(3)
#     print(f'work {func_2.__name__} is over')
#
# def main():
#     func_1(2)
#     func_2(2)
#
# print(time.strftime("%X"))
#
# main()
#
# print(time.strftime("%X"))

#asyncio


# import time
# import asyncio
#
# async def func_1(x):
#     print(x**2)
#     await asyncio.sleep(3)
#     print(f"работа {func_1.__name__} завершена!")
#
#
# async def func_2(x):
#     print(x**2)
#     await asyncio.sleep(3)
#     print(f"работа {func_2.__name__} завершена!")
#
#
# async def main():
#     task_1 = asyncio.create_task(func_1(3))
#     task_2 = asyncio.create_task(func_2(4))
#
#     await task_1
#     await task_2
#
# print(time.strftime("%X"))
#
# asyncio.run(main())
#
# print(time.strftime("%X"))




#async functions and coroutines
# получение типов функции
# import time
#
# def func_1(x):
#     print(x**2)
#     time.sleep(3)
#     print(f'work {func_1.__name__} is over')
#
# def func_2(x):
#     print(x**3)
#     time.sleep(3)
#     print(f'work {func_2.__name__} is over')
#
# def main():
#     func_1(2)
#     func_2(2)
#
# print(type(func_1(2)))
# print(type(func_2))
#

# print(time.strftime("%X"))
#
# main()
#
# print(time.strftime("%X"))


# import time
# import asyncio
#
# async def func_1(x):
#     print(x**2)
#     await asyncio.sleep(3)
#     print(f"работа {func_1.__name__} завершена!")
#
#
# async def func_2(x):
#     print(x**2)
#     await asyncio.sleep(3)
#     print(f"работа {func_2.__name__} завершена!")
#
#
# async def main():
#     task_1 = asyncio.create_task(func_1(3))
#     task_2 = asyncio.create_task(func_2(4))
#
#     await task_1
#     await task_2
#
# print(type(func_1))
# print(type(func_2(3)))


# print(time.strftime("%X"))
#
# asyncio.run(main())
#
# print(time.strftime("%X"))


# def count_to_three():
#     yield 1
#     yield 2
#     yield 3

def count_up_to(num): # generator`s function
    count = 1
    while count <= num:
        yield count #приостановка функции
        count += 1

# making a generator`s object
# counter = count_up_to(10) - generator
#
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# f - сама функция
# f() - вызов функции coroutine