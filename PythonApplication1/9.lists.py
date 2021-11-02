my_list = [1,2,3]
my_list = ["bir",2,True,5.6]
print(my_list)

list1 = ["one","two","there"]
list2 = ["four","five","six"]

numbers = list1 +list2
print(numbers)
print(len(numbers))

userA = ["Sadık", 36]
userB = ["Çınar", 2]

users = userA + userB #böyle liste yapıyorum
users = [userA, userB] #liste içinde liste yaparım böyle de

print(userA)
print(userB)
print(users)

#print(users[1]) #çınar ve yaşı gelir
a= users[1] #yalnızca çınarın adına ulaşmak için bu ikisini yaparız
print(a[0])

print(users[1][0]) #ikisi yerine bunu yazsak da aynı şey

