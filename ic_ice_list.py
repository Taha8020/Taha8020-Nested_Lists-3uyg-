#kullanıcıya toplam bütce sorucaz ve ürünler diye bir sözlük oluşturucaz ve fiyat ve ürün ismi olucak kulanıcı bütçesine uygun ürünleri göstersin
bütce = float(input("Toplam bütçenizi giriniz: "))
ürünler = {
    "laptop": 5000,
    "mouse": 150,
    "klavye": 300,
    "monitor": 1200,
    "kulaklık": 250,
    "tablet": 2000}
uygun_ürünler=[]
for ürün, fiyat in ürünler.items():
    if fiyat <= bütce:
        uygun_ürünler.append(ürün)
        print(f"Ürün: {ürün}, Fiyat: {fiyat}")