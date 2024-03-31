ad = input("Adınız : ")  # input ile girilen veriler string olarak kabul edilir
print("Hoş Geldin", ad)
yas = int(input("Yaşınız : "))  # yaş değişkenini int türüne dönüştürdük
print(ad, yas, "yaşında..")

print("b", "a", "k", "i")
print("b", "a", "k", "i", sep="__")  # sep ile boşluklar arasına str bir ifade girilebilir

print("Yaşınız: ")
yas2 = input()
print(yas2, "yaşındasın..")

print("Yaşınız: ", end="")  # sona eklenen end ile cursorun alt satıra inmesi engellendi (giriş işlemi aynı satırda)
yas3 = input()
print(yas3, "yaşındasın..")

print("Baki\nDönmez")  # \n ile alt satıra geçilir
print("BakiDönmez")
print("Baki\tDönmez")  # \t ile arada bit tab boşluk oluşturulur

sinav1 = int(input("1.Sınav Notunuz = "))
sinav2 = int(input("2.Sınav Notunuz = "))
sinav3 = int(input("3.Sınav Notunuz = "))
ort = (sinav1+sinav2+sinav3)/3
print(f"Ortalamanız = {ort}")

dogum = int(input("Doğum Yılınızı Giriniz : "))
yas = 2024 - dogum
print(yas, "yaşındasınız..")

print("baki")
print("baki"*4)  # hata vermez str ifadeyi yanyana yazdırır(kaç defa isteniyorsa)
# print("baki"+4)  hata verir str ifade ile int toplanamaz
