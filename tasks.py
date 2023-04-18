import asyncio


# Задачи используются для планирования параллельного выполнения сопрограмм.
# При передаче сопрограммы в цикл событий для обработки можно получить объект Task,
# который предоставляет способ управления поведением сопрограммы извне цикла событий.


async def async_function():
    print('> start async func')
    await asyncio.sleep(1)
    print('> end async func')


async def main():
    print('main create task')
    task = asyncio.create_task(async_function())
    print('main before await task')
    await task
    print('main after await task')


asyncio.run(main())
