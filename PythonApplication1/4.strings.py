name = "sadık"
surname ="turan"
age = 36

greeting = "My name is " + name + " "  + surname + " and \nI am " + str(age)+ " years old"
print(greeting )
#\n yazdığın yerden itibaren alt satıra geçiyor

print(greeting[0]) #greeting deki 0. karakter yani ilk karakterin 
#ne olduğunu soruyoruz yani ilk harf olan M dir cevap
print(greeting[2])
#print(len(greeting)) #kaç karakterli olduğunu söyler
length = len(greeting)
print(greeting[length-1]) #son karakterden bir öncekini buluruz
print(greeting[-1]) #o kadar işlem yapmak yerine yalnızca bunu yazsak da aynısı olur

print(greeting[2:5]) # 2. karakterden başla 5. kadar yaz demek, 5. yi yazmaz ama
print(greeting[3:]) # 3. den başla en sona kadar git
print(greeting[:16])
print(greeting[2:40:2]) # 2den 40a kadar git ama her karakteri alma 2 karakterde bir al diyebiliriz
