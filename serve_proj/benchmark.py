import asyncio
import aiohttp
import time

async def fetch_page(session, url):
    async with session.get(url) as response:
        assert response.status == 200
        return await response.read()

async def run_benchmark(url):
    start = time.time()
    count = 0
    async with aiohttp.ClientSession(loop=loop) as session:
        while time.time() - start < 30: # Run test for one minute.
            count += 1
            print(await fetch_page(session, url))
        return count / (time.time() - start) # Compute queries per second.

async def main():
    num_connections = 5 # Use as many connections as replicas.
    url = "http://127.0.0.1:8080/generate?query=Hello%20friend%2C%20how"
    results = await asyncio.gather(*[run_benchmark(url) for _ in range(num_connections)])
    print("Queries per second:", sum(results)) # Sum qps over all replicas.

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())