import asyncio


# Сопрограммы (coroutine) — это обобщенные формы подпрограмм. Они используются для кооперативных задач и ведут себя как генераторы Python.
# Для определения сопрограммы асинхронная функция использует ключевое слово await. При его использовании сопрограмма передает поток управления обратно в цикл событий (также известный как event loop).
# Для запуска сопрограммы нужно запланировать его в цикле событий. После этого такие сопрограммы оборачиваются в задачи (Tasks) как объекты Future.

async def async_function():
    print('> start async func')
    await asyncio.sleep(1)
    print('> end async func')


async def main():
    print('main before await')
    await async_function()
    print('main after await')


asyncio.run(main())
