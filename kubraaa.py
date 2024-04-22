tum_karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


parola_uzunlugu = int(input("Parolanın uzunluğunu girin: "))


import random
parola = ''.join(random.choice(tum_karakterler) for i in range(parola_uzunlugu))

print("Oluşturulan parola:", parola)
