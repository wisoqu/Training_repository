# дз 0
# Условие: Напиши функцию-генератор even_fibonacci(limit),
# которая генерирует числа Фибоначчи, но выдает только четные из них и только до тех пор,
# пока число меньше limit.
# Подсказка: Используй цикл while внутри генератора и оператор yield.
#дз 1
# Условие: Напиши асинхронную функцию fetch_data(id, delay),
# которая имитирует загрузку данных: «спит» delay секунд, а затем возвращает строку:
# f"Данные из источника {id} получены".
# Задание: Запусти три таких задачи параллельно (например, с задержками 1, 2 и 3 секунды) с помощью asyncio.gather() и выведи результаты в консоль.
# Инструмент: Тебе понадобится await asyncio.sleep(delay).

# Футуры и задачи
import asyncio
import time

async def even_fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        if a % 2 == 0:
            yield a
        a, b = b, a + b
fibonacci = even_fibonacci(6)

async def fetch_data(id, delay):
    await asyncio.sleep(delay)
    print(f"Данные из источника {id} получены")

async def main():
    result = await asyncio.gather(
        fetch_data(1, 1),
        fetch_data(2, 2),
        fetch_data(3, 3)
    )
    print(result)