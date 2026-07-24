import array as arr

b1= {"apple", "banana", "mango", "grape"}
b2={"mango", "kivi", "banana"}

b1.add("orange")
c = b1 & b2

a = arr.array("i",[3,5,2,4,])
a.insert(0, 1)
a.append(6)
print("4 count:", a.count(4))
a.reverse()

print(b1)
print(b2)
print(c)
print(a)