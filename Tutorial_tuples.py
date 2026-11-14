mytuple = ("Max", 28, "Boston")
mytuple = tuple(["Max", 28, "Boston"])
mytuple = "Max", 28, "Boston"
mytuple = ("Max",)        #tuple
mytuple = ("Max")       #stirng


items = mytuple[-1]

#Immutable
#iteration, in operation, len(mytuple), slicing

print(mytuple.count("Max"))
print(mytuple.index("Max"))

mylist = list(mytuple)

#unpacking
name, age, city = mytuple

tuple2 = (0, 1, 2, 3, 4)
i1, *i2, i3 = tuple2   #i2 is list