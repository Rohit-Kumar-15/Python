mylist = ["banana", "cherry", "apple"]
print (mylist)

item = mylist[2]
print (item)

for x in mylist:
    print(x)


if "banana" in mylist:
    print ("yes")


mylist.append("lemon")
mylist.insert(1,"Orange")
mylist.remove("apple")
mylist.pop()
mylist.reverse()
mylist.clear()

print(mylist)

mylist2 = [2,4,6,7,3,4,8]
mylist2.sort()
newlist = sorted(mylist2)

fivelist = [0] * 5

listnew = mylist2 + fivelist

a= mylist[1:3]

origlist = ["Banana", "Cherry", "Lemon"]
copylist = origlist.copy()
copylist = list(origlist)
copylist = origlist[:]

square = [i*i for i in mylist2]
print(square)