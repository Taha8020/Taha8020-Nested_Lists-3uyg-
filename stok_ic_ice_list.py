
# stoklar adına sözlük içinde (laptop, mouse ,tablet, klavye ) laptop value değeri 5 mouse value değeri 10 tablet value değeri 7 klavye value değeri 3 olacak şekilde bir sözlük oluşturun.
stoklar={"laptop":5,"mouse":0,"klavye":12,"monitor":3,"kulaklık":8,"tablet":2}
istek=input("Hangi bilgiyi almak istiyorsun 1:Stokta olan ürünler- 2: Stokta olmayan ürünler- 3: Stok tükenmek üzere olan ürünler: ")
if istek=="1":
    for stok in stoklar:
        if stoklar[stok]>0:
            print(f"Stokta olan ürünler {stok}, adet sayısı {stoklar[stok]}")
elif istek=="2":
    for stok in stoklar:
        if stoklar[stok]==0:
            print(f"Stokta olmayan ürünler {stok}, adet sayısı {stoklar[stok]}")
elif istek=="3":
    for stok in stoklar:
        if stoklar[stok]<=3 and stoklar[stok]>0:
            print(f"Stok tükenmek üzere olan ürünler {stok}, adet sayısı {stoklar[stok]}")
else:
    print("Hatalı giriş yaptınız. Lütfen 1, 2 veya 3 giriniz.")

    #3. seçenek olarak stok tükenmek üzere buraya 3 ve 3ün altındaki ürünleri listeleyecek bir seçenek ekleyin.
    # Yapıldı
