import aiohttp
import asyncio
import time

async def fetch_page(session, url):
    page_start = time.time()
    async with session.get(url) as response:
        #print(response.status)
        print('fetch took {}'.format(time.time() - page_start))
        return response.status
async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session,url))
        grouped_task = asyncio.gather(*tasks)
        return await grouped_task


loop = asyncio.get_event_loop()
start = time.time()
urls = ['http://google.com' for i in range(50)]
loop.run_until_complete(get_multiple_pages(loop, *urls))
print("total time:" , time.time()-start)