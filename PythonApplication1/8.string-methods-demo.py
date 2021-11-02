website= "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#1- " Hello World " karakter dizisinin baş ve sondaki boşluk karakterlerini silin
result = "Hello World".strip()
result = "Hello World".lstrip() #sadece soldaki
result = "Hello World".rstrip()
result = website.lstrip("/:pth")


#2- "http://www.sadikturan.com" içindeki sadikturan bilgisi haricindeki her karakteri silin
result = "www.sadikturan.com".strip("w.moc")

#3-
#4- "website" içinde kaç tane a karakteri vardır
result = website.count("a")
result = website.count("www")
result = website.count("www",0,10) #0 ile 10. karakterler arasında www den kaç tane var


#5- "website" www ile başlayıp com ile bitiyor mu
result = website.startswith("www")
result = website.startswith("http")
result = website.endswith("com")

#6- "website" içinde ".com" ifadesi var mı
#count ile de sorabilirsin, false ya da true der
result = website.find("com") #varsa kaçıncı karakterde onu söylüyor
result = website.find("com",0,10)
result = website.rfind("com",0,10) #sağdan say


result = website.index("com")
result = website.rindex("com")
#result = website.rindex("comm") #exception

#7- "course" içindeki krkterlerin hepsi alfabetik mi
result = course.isalpha() #false çünkü sayısal karakterler de var
result = "Hello".isalpha()
result = course.isdigit()
result = "123".isdigit()

#8- "Contents" ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz
result = "Contents".center(50, "*") #cevap bu
result = "Contents".ljust(50, "*")
result = "Contents".rjust(50, "*")

print(result)