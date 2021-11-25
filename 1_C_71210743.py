daftar_nilai1 = [10,40,30,53,50]
daftar_nilai2 = [99,78,89,85,46]
daftar_nilai3 = [57,90,76,85,78]

def nilai(x): 
    print("Nilai Tertinggi adalah: ", max(x)) 
    print("Nilai Terendah adalah: ", min(x))
    rata2 = (sum(x)/len(x))
    fix_hasil_rata2 = "{:.2f}".format(rata2)
    print('Rata-ratanya adalah: ', fix_hasil_rata2) 
    x.sort()
    print('', x)


nilai(daftar_nilai1)