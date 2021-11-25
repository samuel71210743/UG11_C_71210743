def ambil_dan_sisipkan():
    kata = str(input('Masukkan Kalimat: '))
    index_1 = int(input('Masukkan index 1: ')) - 1 
    index_2 = int(input('Masukkan index 2: ')) - 1
    result = print(kata+kata[index_1]+kata[index_2])
    return result


ambil_dan_sisipkan()