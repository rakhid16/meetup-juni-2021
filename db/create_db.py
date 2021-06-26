import asyncio
import asyncpg

async def get_connecion():
    conn = await asyncpg.connect(
        host="localhost",
        port=5432,
        user="ikal",
        password="password",
        database="postgres")

    return conn

async def main():
    conn = await get_connecion()

    await conn.execute('''
        CREATE TABLE pengguna(
            id serial PRIMARY KEY,
            name text)
    ''')

    await conn.execute('''
        CREATE TABLE users(
            id serial PRIMARY KEY,
            name text)
    ''')

    await conn.close()

asyncio.run(main())