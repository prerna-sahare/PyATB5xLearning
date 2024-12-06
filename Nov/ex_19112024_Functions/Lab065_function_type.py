# user define
# 1.they cannt return(non return)
# 2. they can return something
# 3. they have paramenter
# 4. they dont have parameter


# 1.
def greet():
    print("hello")

greet()

# 2.
def greet_by_name(name):
   print("hello, ", name)

greet_by_name("Prerna")

# 3.

def greet_default_agr(name="Prerna"):
    print("Hello", name)

greet_default_agr("Sahare")
greet_default_agr()

# 4.multiple argument

def multiple_argument(name1="a", name2="b"):
     print("mutliple", name1,name2)

multiple_argument(name1="prerna")
multiple_argument(name2="sahare")
multiple_argument()
multiple_argument("Lucky")

# 4. argument+return type

def sum_of_two(a,b):
    return a+b

result=sum_of_two(4,5)
print(result)