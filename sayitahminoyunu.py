import random
rndSayi = random.randint(1, 20)
i = 0
bildinMi = False
devamMi = True
while devamMi == True:
    while bildinMi == False:
        i += 1
        tahmin = input("1 ile 20 arasında bir sayı tahmin ediniz: ".title())
        if tahmin.isdigit():
            tahmin = int(tahmin)
            if tahmin < rndSayi:
                print("-------lütfen büyük sayı giriniz!-------".title())
            elif tahmin > rndSayi:
                print("-------lütfen küçük sayı giriniz!-------".title())
            else:
                bildinMi = True
        else:
            print("Hatalı Giriş!")
    print("Tebrikler! {} Denemede Buldunuz!".format(i))
    cevap = input("Çıkmak İster Misiniz?..e/h: ")
    if cevap.lower() == "e":
        devamMi = False
    elif cevap.lower() == "h":
        rndSayi = random.randint(1, 20)
        bildinMi = False
        devamMi = True
        i = 0

