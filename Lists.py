a=[1,2,"apple","banana",3.15,True,False]
print(a)
print(len(a))
print(type(a))
print(a[0])#indexing should always be in []
print(a[-1])
a.append("Kiwi")
print(a)
a.insert(3,"grapes")
print(a)
a.remove("grapes")
print(a)
a.pop(4)
print(a)
a.clear()
print(a)

del a
#print(a)

b=[1,5,7,3,2,9]
b.sort()
print(b)
b.sort(reverse=True)
print(b)


