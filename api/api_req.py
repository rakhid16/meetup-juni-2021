"""
Skenario Async

1. HTTP requests & responses
2. Database operations
"""

import asyncio

from os import getpid
from multiprocessing import Pool
from time import time

import aiohttp
import requests

def get_pokemon(url: str) -> str:
    pokemon = requests.get(url)
    pokemon = pokemon.json()

    print(pokemon['english'], getpid())

    return pokemon['english']

def main_sync() -> None:
    [get_pokemon(
        f'http://0.0.0.0:8080/{number}') for number in range(0, 809)]

def main_multi(worker : int) -> None:
    p = Pool(processes=worker)

    _ = p.map(get_pokemon,
        [f'http://0.0.0.0:8080/{number}' for number in range(0, 809)])

    p.close()

async def get_pokemon_async(
    session : aiohttp.ClientSession,
    url: str) -> str:

    async with session.get(url) as resp:
        pokemon = await resp.json()
        print(
            pokemon['english'],
            asyncio.current_task().get_name())

        return pokemon['english']

async def main_async() -> None:
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(
            get_pokemon_async(
                session,
                 f'http://0.0.0.0:8080/{number}')) for number in range(0, 809)]

        await asyncio.gather(*tasks)

awal = time()

#main_sync()
#main_multi(worker = 30)
asyncio.run(main_async())

print("Waktu Eksekusi program :", time()-awal, "detik")