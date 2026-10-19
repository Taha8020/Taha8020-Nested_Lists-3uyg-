users = [
    {
        "username": "taha",
        "password": "123",
        "email": "taha@example.com"
    },
    {
        "username": "batur",
        "password": "567",
        "email": "batur@example.com"
    },
    {
        "username": "oz",
        "password": "901",
        "email": "oz@example.com"
    }
]
girilen_username = input("Kullanıcı adınızı giriniz: ")
girilen_password = input("Şifrenizi giriniz: ")
for user in users:
    if user["username"] == girilen_username and user["password"] == girilen_password:
        print("Giriş başarılı!")
        break  
else:
    print("Kullanıcı adı veya şifre hatalı.")

