message ="Hello there. My name is Sadık Turan "

#bu tarz bir sürü bize yardım eden string methodları var, ihtiyaç halinde listeye bakıp faydalanabiliriz
message = message.upper() #mesajdaki tüm karakterli büyük harfleştirir
message = message.lower() #hepsini küçültür
message = message.title() #her kelimenin baş harfini büyültür
message = message.capitalize() #sadece ilk harfini büyük yapar
message = message.strip() #başa boşluk bıraktıysan onu siler
message = message.split() #her kelime ayrı ayrı gelir, burda her kelimeye ulaşıp üzerinde işlem yapabiliriz
#print(message[0]) #yukardakiyle beraber bunu yazarsam ilk kelimeyi bulurum
message = message.split(".") #nokta olan yerden ayır yani cümle cümle göster
#print(message[0]) bunu da yazarsan ilk cümleyi bulursun
message = " ".join(message) #kelime kelime iken hepsini birleştir ve aralarına bosluuk koy demek
message = "*".join(message) #yukardakini yaparken hepsinin arasına * ekler
index = message.find("Sadık") #Sadık kelimesi cümlede var mı bakar ve kaçıncı indekste yani baş harfi kaçıncı karakter onu söyler
#print(index)
index = message.find("Sadıkk") #yazarsak -1 gelir bu da kelimenin orda olmadığını anlatır
isFound = message.startswith("H") #cümle H ile mi başlıyor diye sorduk #true ya da false gelcek
isFound = message.endswith("n")
message = message.replace("Sadık", "Çınar") #yerlerini değiştirir
message = message.replace(" ", "*") #bütün boşluklara yıldız ekler
message = message.replace("ç", "c").replace("ü", "u").replace("ş", "s")
message = message.center(100) #bizim mesajı 100 karakter yapar daha az olduğu için başına ve sonuna boşluk koyar
message = message.center(50,"*") #50 karakter yapar boşuk yerine * koyar



print(message)
