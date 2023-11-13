tek_sayilar = []
toplam = 0
for x in range(1,10):
    if x % 2 == 1:
        tek_sayilar.append(x)
        toplam += x
    else:
        pass
print(f'Tek rakamlar: {tek_sayilar}')
print(f'Tek rakamlarin toplami: {toplam}')

cift_sayilar=[]
toplam_c = 0
for i in range(1,11):
    if i % 2 == 0:
        cift_sayilar.append(i)
        toplam_c += i 
    else:
        pass
print(f'Cift rakamlar: {cift_sayilar}')
print(f'Cift rakamlarin toplami: {toplam_c}')
