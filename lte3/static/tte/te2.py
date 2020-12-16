import asyncio

async def my_coro(arg):  
    "A coroutine."  
    print(arg)

async def main():  
    "The top-level coroutine."
    await my_coro(42)

# Канонической точкой входа в программу asyncio является asyncio.run(main()), 
# где main () — подпрограмма (coroutine) верхнего уровня.

asyncio.run(main())  

