# list = array
users = ["himxa", "jhon", "sare"]
data = ["dave", 45, True]
emptyList = []
# use this to check if a value is inside a list
print("dave" in emptyList)
# for accing perticular value in an array
print(users[1])
print(users[-1])

# py methods
# index methode is use for getting the position of the element
print(users.index("himxa"))

# getting two or more ement from a list
# if u put only one value with out providing the second one
# it will get from that elemnt upword
print(users[0:])
# note if u put two value in it , it will only get the elemnt before the last elemt u put
print(users[0:2])
# for getting the length of a list
print(len(users))
# to add new element to ourList
 #i
users.append('Divel',)
print(users)
#ii
users += ['jason','loser']
print(users)
#iii
users.extend(['Robert','Jimmy'])
print(users)

# to add element to a perticular location in a list 
users.insert(0,'brad')
print(users)
# to add more than one elemnt in a perticuler index
# need to specified to aviod replacement
users[2:2] = ['yusuf','maryam']
print(users)

#to replace value
users[0:3] = ['devil','moder','father']
print(users)

#to remove
users.remove('devil')
print(users)

#to delete a list 
del data
#print(data)

#to clear a list
#users.clear()
#print(users)

# to aggarnge elemt
# it put capital letter first this way
users.sort()
print(users)
# now it arrange it properly
users.sort(key=str.lower)
print(users)

# to copy a list 
newUsers = users.copy()
newcopy = list(users);
mycopy = users[:]

#tuple are just like list but can not be changed or remodified
#to create tuple 
#i
myTuple = tuple(('dave',45,True))
#ii
anotherTuple = (1,2,3,4,5)
print(myTuple)