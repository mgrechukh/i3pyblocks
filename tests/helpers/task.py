import asyncio


async def runner(coros, timeout=0.1):
    "Run a list of coroutines as tasks, including timeout"
    tasks = [asyncio.ensure_future(coro) for coro in coros]

    await asyncio.wait(tasks, timeout=timeout)

    for task in tasks:
        task.cancel()
