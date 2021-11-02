#

#her hangi bir şeyi atamak,yani sayı vs. girmek için input kullanılır
#inputtan gelen değer string olarak algılanır, mat işlemi yapmaz

x= input("1.sayı:")
y= input("2.sayı:")

#toplam =x+y
#print(toplam)

print(type(x))
print(type(y)) #tiplerini görmek için yaptık sadece

toplam =int(x)+int(y)
print(toplam)

x=5              #int
y=2.5            #float
name="çınar"     #string
isOnline = True  #bool


#print(type(x))
#print(type(y))      #hepsini seçip ctrl +k+c ye basarsan hepsi ayrı ayrı yorum satırı oluyor
#print(type(name))   #ctrl +k+u yaparsan yorumluktan çıkar
#print(type(isOnline)) #bu printli olanlar """ veya ''' ile topluca yorum satırı olmuyor nedense


#Type Conversion

#int to float
x= float(x)
print(x)
print(type(x))

#float to int
y= int(y)
print(y)
print(type(y))

# float and int to str
result = str(x) +str(y)
print(result)
print(type(result))

#bool to str
isOnline= str(isOnline)
print(isOnline)
print(type(isOnline))

#bool to int
isOnline = int(isOnline)
print(isOnline)
print(type(isOnline))
