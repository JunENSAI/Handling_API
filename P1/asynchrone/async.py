import time
import httpx
import asyncio

URLS = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1"
]

# --- STRATEGY 1: SYNCHRONOUS  ---
def fetch_sync():
    print("\n--- Starting Synchronous Fetch ---")
    start_time = time.perf_counter()
    
    with httpx.Client() as client:
        for i, url in enumerate(URLS):
            print(f"Requesting {i+1}...")
            client.get(url) 
            
    end_time = time.perf_counter()
    print(f"Synchronous finished in: {end_time - start_time:.2f} seconds")

# --- STRATEGY 2: ASYNCHRONOUS ---

async def fetch_async():
    print("\n--- Starting Asynchronous Fetch ---")
    start_time = time.perf_counter()
    
    async with httpx.AsyncClient() as client:
        tasks = []
        for i, url in enumerate(URLS):
            print(f"Queueing request {i+1}...")
            tasks.append(client.get(url))
        
        # asyncio.gather fires them all at once and waits for all to finish
        print("Waiting for all responses...")
        responses = await asyncio.gather(*tasks)
            
    end_time = time.perf_counter()
    print(f"Asynchronous finished in: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    #fetch_sync() -- the synchronous version take some time to run, so possibly you saw the exception ReadTimeout
    asyncio.run(fetch_async())
    
    print("\nObservation: Async should be 3x faster because the 1s delays happened in parallel!")