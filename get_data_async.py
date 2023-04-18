import asyncio
import time
from aiohttp import ClientSession, ClientResponseError


async def fetch_url_data(session, url):
    try:
        async with session.get(url, timeout=60) as response:
            response = await response.read()
    except Exception as e:
        print(e)
    else:
        return response
    return


async def fetch_async(loop, range_num):
    url = "https://www.google.com/"
    tasks = []
    async with ClientSession() as session:
        for i in range(range_num):
            task = asyncio.ensure_future(fetch_url_data(session, url))
            tasks.append(task)
        fetch_responses = await asyncio.gather(*tasks)
    return fetch_responses


if __name__ == '__main__':
    for amount in [1, 10, 50, 100, 500]:
        start_time = time.time()
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(fetch_async(loop, amount))
        # until to the end or error
        loop.run_until_complete(future)
        responses = future.result()
        print('Collected ', amount, ' results for ', time.time() - start_time, ' seconds')
