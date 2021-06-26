from time import time

import psycopg2

def get_connecion():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        user="ikal",
        password="password",
        database="postgres")

    return conn

def main() -> None:
    conn = get_connecion()
    cursor = conn.cursor()

    # GET DATA FROM DB
    cursor.execute('select * from users;')    
    data = cursor.fetchall()
    print(len(data), "data selected")

    # INSERT TO users TABLE
    cursor.executemany("INSERT INTO users (name) VALUES (%s)",
                       list(zip([i[1] for i in data])))
    conn.commit()

    # INSERT TO pengguna TABLE
    cursor.executemany("INSERT INTO pengguna (name) VALUES (%s)",
                       list(zip([i[1] for i in data])))
    conn.commit()

    # CLOSE CONNECTION
    conn.close()

awal = time()

main()

print("Waktu Eksekusi program :", time()-awal, "detik")