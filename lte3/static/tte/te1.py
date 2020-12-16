import aiohttp
import asyncio

async def print_preview(url):
    # connect to the server
    async with aiohttp.ClientSession() as session:
        # create get request
        async with session.get(url) as response:
            # wait for response
            response = await response.text()

            # print first 3 not empty lines
            count = 0
            lines = list(filter(lambda x: len(x) > 0, response.split('\n')))
            print('-'*80)
            for line in lines[:3]:
                print(line)
            print()

def print_all_pages():
    pages = [
        'http://textfiles.com/adventure/amforever.txt',
        'http://textfiles.com/adventure/ballyhoo.txt',
        'http://textfiles.com/adventure/bardstale.txt',
    ]

    tasks =  []
    loop = asyncio.new_event_loop()
    for page in pages:
        tasks.append(loop.create_task(print_preview(page)))

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

print_all_pages()
