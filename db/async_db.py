import asyncio

from time import time

import asyncpg

async def get_connecion():
    conn = await asyncpg.connect(
        host="localhost",
        port=5432,
        user="ikal",
        password="password",
        database="postgres")

    return conn

async def main() -> None:
    conn = await get_connecion()

    # GET DATA FROM DB
    data = await conn.fetch('select * from users;')
    print(len(data), "data selected")

    # INSERT TO users TABLE
    await conn.executemany("INSERT INTO users(name) VALUES($1);",
                           list(zip([i['name'] for i in data])))
    
    # INSERT TO pengguna TABLE
    await conn.executemany("INSERT INTO pengguna(name) VALUES($1);",
                           list(zip([i['name'] for i in data])))

    # CLOSE CONNECTION
    await conn.close()

awal = time()

asyncio.run(main())

print("Waktu Eksekusi program :", time()-awal, "detik")