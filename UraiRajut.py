# Membuat def function untuk urai
def urai(kata):
    # Membuat variabel a untuk looping 1 (ascending)
    a = ''
    # Membuat variabel b untuk looping 2 (descending)
    b = ''
    
    # Membuat looping ascending 
    for i in range(len(kata)):
        for j in range(0,i+1):
            a += kata[j]
            
    # Membuat looping ascending yang di reverse
    for k in range(len(kata)):
        # dari 0 sampai k karena yang paling akhir tidak di print lagi
        for l in range(0,k):    
            b += kata[l]
    
    # Print Hasil dari Looping ascending dan descending
    return a + b

# Print Hasil 'Code'
print(urai('Code'))
# Print hasil 'Python'
print(urai('Python'))

# Pembatas
print('')
print('')


# Membuat def function untuk Rajut
def rajut(kata):
    b = ''
    c = ''
    awal = 2
    tambah = 1
    k = int((len(kata)/2) - 1)
    #Aritmatika = 1,3,6,10,15,21,15,10,6,3,1

    while tambah <= len(kata):
        b += kata[tambah-1]
        tambah += awal
        awal += 1
        c = b[:-2]
        
    return c
    
print(rajut('CCoCodCodeCodCoC'))
print(rajut('PPyPytPythPythoPythonPythoPythPytPyP'))