'''
x, y, z = "Orange", "Banana", "Apple"

print(x)
print(y)
print(z)
#============================================
x = y = z = "Orange"

print(x)
print(y)
print(z)

#============================================
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)

#============================================

x = "Python "
y = "is "
z = "awesome"

print(x + y + z)
#============================================
x = 5
y = 10

print(x +y)

#=======Global Variables=====================

x = "awesome"

def myfunc():
           print("Python is " + x + " with Global Variables")

myfunc()
    #============================================
    # #Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)
        
myfunc()

print("Python is " + x)
'''
#============================================
#==================global keyword==========================
#def myfunc():
#    global x
#    x = "fantastic"
#
#myfunc()
#
#print("Python is " + x)

#============================================
#============ use the global keyword if you want to change a global variable inside a function.
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)