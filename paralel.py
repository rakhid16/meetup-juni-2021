from time import  time, sleep
from os import getpid
from multiprocessing import Pool

def cetak(nama : str) -> None:
    sleep(1)
    print(nama, getpid())

awal = time()

p = Pool(processes=4)

# UNLOCKING THE GIL
_ = p.map(
    cetak,
    [nama for nama in ("JoJo", "Henry", "Zaid", "Sanji")])

p.close()

print("Waktu Eksekusi program :", time()-awal, "detik")

"""
Akan terjadi masalah jika operasi pada sebuah function memakan waktu
yang tidak sebentar. solusi'nya adalah optimasi performa.

Kekurangan :
1. RAM (resource) akan lebih banyak terpakai
2. Semakin banyak jumlah worker maka semakin lama program
   mengalokasikan waktunya hanya untuk spawn worker saja.

Kelebihan :
1. Program akan tereksekusi secara cepat (optimal)
"""