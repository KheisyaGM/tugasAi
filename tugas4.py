def hitung_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

p = 5
l = 3
luas, keliling = hitung_persegi_panjang(p, l)

print("Luas persegi panjang:", luas)
print("Keliling persegi panjang:", keliling)