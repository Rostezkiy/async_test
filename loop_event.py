import asyncio

# Дальше создаются три задачи, которые добавляются в список.
# Они выполняются асинхронно с помощью get_event_loop, create_task и await библиотеки asyncio.

async def async_function(task_no):
    print(f'{task_no}: Start ...')
    await asyncio.sleep(1)
    print(f'{task_no}: ... Done!')


async def main():
    taskA = loop.create_task(async_function('task A'))
    taskB = loop.create_task(async_function('task B'))
    taskC = loop.create_task(async_function('task C'))
    await asyncio.wait([taskA, taskB, taskC])


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except:
        pass

asyncio.run(main())
