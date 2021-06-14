import os
import sys

class mahasiswa:
    nim = ''
    nama = ''

pilih = 0
datamahasiswa = []

def menu():
    os.system('cls')
    print("_______________________________________-")
    print("PILIH MENU")
    print("1. Input Data Mahasiswa")
    print("2. Cari NIM Mahasiswa")
    print("3. Cari Nama Mahasiswa")
    print("4. Keluar Menu")
    pilih = int(input("Masukan Pilihan Anda : "))
    if pilih == 1:
        inputdata()
        menu()
    if pilih == 2:
        carinim()
        menu()
    if pilih == 3:
        carinama()
        menu
    if pilih == 4:
        print("terima kasih")
        sys.exit()
    if pilih > 4 :
        print("pilihan anda tidak ada pada menu")
        input("silahkan pilih menu kembali")
        menu()

def tampil():
    print("Data Mahasiswa")
    for data in datamahasiswa:
        print("__________________________________________")
        print("NIM Mahasiswa : " ,str(data.nim))
        print("Nama Mahasiswa : " ,data.nama)
    print("_______________________________________")


def inputdata():
    ulang = 'Y'
    while ulang in ('y','Y'):
        os.system('cls')
        mhs = mahasiswa()
        print('Input data mahasiswa')
        print("__________________________________________")
        mhs.nim = (input("input nim mahasiswa : "))
        mhs.nama = (input("input nama mahasiswa : "))
        print("__________________________________________")
        datamahasiswa.append(mhs)
        ulang = input('apakah anda ingin mengulang input ? (y/t)= ')
    menu()

def carinim():
    os.system('cls')
    tampil()
    ulang = 'Y'
    while ulang in ('y','Y'):
        cari = (input("Masukan Nim yang dicari : "))
        for n in range(0,len(datamahasiswa)):
            if cari == datamahasiswa[n].nim :
                isfounded = True
                id = n
                break
            else :
                isfounded = False
        if isfounded:
            print("__________________________________________")
            print("Nim Mahasiswa : ",datamahasiswa[id].nim)
            print("Nama Mahasiswa : ",datamahasiswa[id].nama)
            print("__________________________________________")
        else:
            print("Nim yang anda cari tidak ditemukan")
        ulang = input('apakah anda ingin mengulang input ? (y/t)= ')
    menu()

def carinama():
    os.system('cls')
    tampil()
    ulang = 'Y'
    while ulang in ('y','Y'):
        cari = (input("Masukan Nama yang dicari : "))
        for b in range(0,len(datamahasiswa)):
            if cari == datamahasiswa[b].nama :
                isfounded = True
                id = b
                break
            else :
                isfounded = False
        if isfounded:
            print("__________________________________________")
            print("Nim Mahasiswa : ",datamahasiswa[b].nim)
            print("Nama Mahasiswa : ",datamahasiswa[b].nama)
            print("__________________________________________")
        else:
            print("Nama yang anda cari tidak ditemukan")
        ulang = input('apakah anda ingin mengulang input ? (y/t)= ')
menu()