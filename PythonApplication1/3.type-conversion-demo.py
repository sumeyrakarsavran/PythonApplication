
#yarıçap verilen bir dairenin alan ve çevresini hesapla 
# pi :3.14

pi = 3.14
r = float(input("yari çap:")) #input str bir bilgi verir o yüzden sayıya çevirmem lazım
alan = pi * (r ** 2)
print(type(alan))

cevre = 2 * pi * r
print(type(cevre))

print("alan:", alan)   #str birleştirme kullanılırken + kullanılır
print("cevre:", cevre) #float int vs. varsa (str olabir de olmayabilir de) birleştirme yaparken , kullanılır

print("alan: "+ str(alan)+ ","+ "cevre: " + str(cevre))
