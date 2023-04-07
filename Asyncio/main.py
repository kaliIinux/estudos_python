import asyncio, time


async def outrafuncao():
    
    await asyncio.sleep(1)
    print(f"momento outra funcao: {time.strftime('%X')}")
    print("Minha mensagem 1")
    
async def outrafuncao2():
    
    await asyncio.sleep(1)
    print(f"momento outra funcao2: {time.strftime('%X')}")
    print("Minha mensagem 2")

async def funcao():
    print(f"iniciou: {time.strftime('%X')}")
    task = asyncio.create_task(outrafuncao())
    task1 = asyncio.create_task(outrafuncao2())
    print(f"iniciou: {time.strftime('%X')}")
    
    await task
    await task1

asyncio.run(funcao())