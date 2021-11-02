website= "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#1- "course" karakter dizisinde kaç karakter bulunmaktadır?
result = len(course)

#2- "website" içinden www karakterini alın
result = website[7:10]

#3- "website" içinden com karakterini alın
result = website[22:25]
lenght = len(website)
result = website[lenght-3: lenght]

#4- "course" içinden ilk 15 ve son 15 krk al
result =course[0:15]
result =course[:15] #ilk
result =course[-15:] #son

#5- "course" ifadesindeki karakterleri tersten yazdırın
result = course[::]  
#kurs ifadesindeki bütün elemanları almak 
#için iki tane iki nokta ekliyoruz
#sayının sol tarafına iki nokta eklersek sol tarafı işin içine katmış oluyoruz
#sayının sağ tarafına iki nokta eklersek bitiş karakterlerini yani sağ tarafı işin içine katmış oluyoruz
result = course[::2] #yazarsak bir karakter alır bir karakter almaz
result = course[::1] #tek tek her karakteri al
result = course[::-1] #her şey tersten yazılır

#s= "12345" *5 #bu ifadeyi 5 kere yan yana yaz dedim
#print(s)
#print(s[::5]) #5karakterde bir yaz dedim yani cevap şimdi 11111 olacak


name, surname, age, job = "Bora", "Yılmaz", 32, "mühendis"
#6- Yukarıda verilen değişkenler ile ekrana aşağıdaki fadeyi yazdırın
#  "Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis."

result = "Benim adım " + name + " " + surname + ", Yaşım " + str(age)+ " ve mesleğim " +job
result = "Benim adım {} {}, Yaşım {} ve mesleğim {}.".format(name,surname, age,job)
#ilk yaptığımız biraz uğraştırıcı o yüzden tamamını kopyl ypştr gerekli yerleri parantezle ve format ekle
result = f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}."


#7- "Hello world" ifadesindeki w yu W ile değiştir
s = "Hello world" #w 6. dır
s= s[0:6] + "W"+ s[-4:]
s.replace("w","W") #kolay yolu bu
print(s)

#8- "abc" ifadesini yan yana 3 defa yazdırın
result = "abc" *3


print(result)
