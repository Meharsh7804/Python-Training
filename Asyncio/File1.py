import asyncio

async def main():
    print("Hello, World!")
    asyncio.sleep(2)
    print("Goodbye, World!")

# async def main():
#     print("Start of main coroutine")

print(type(main())) # coroutine object
# main() returns a coroutine object, which is then run by asyncio.run()

# run the main coroutine
asyncio.run(main())

# RuntimeWarning: coroutine 'sleep' was never awaited