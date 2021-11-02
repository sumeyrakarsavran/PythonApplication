name ="çınar"
surname = "turan"

print("My name is {}".format(name))
#print("My name is {0} {1}".format(name,surname)) normal hali
print("My name is {1} {0}".format(name,surname)) #soyisim başa gelir
print("My name is {s} {n}".format(n=name,s=surname)) #soyisim başa gelir
print("My name is {} {} and I'm {} years old.".format(name, surname, "36"))

result =200/700
print("the result is {}".format(result))
print("the result is {r:1.3}".format(r=result))
#yukarda yazdığım virgülden sonra kaç basamak istediğim, yuvarlayarak veriyo cevabı
print("the result is {r:7.3}".format(r=result))
#toplam 5 basamaklı olduğu için ben de 7 yazdığım için 2 tane boşluk bırakıyo basamak gibi

print(f"My name is {name} {surname} and I'm {age} years old.")
#bunu yaparsam sona format yazmama gerek kalmaz




