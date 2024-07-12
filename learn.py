import time
#1 data types in python
#1 sting
name = 'hamza'
#print(type(name))

#2 inst = numbers interger
age = 15
#print(type(age))
#for joing num and string use this
print(name +  ' ' + str(age))

#3 float= an numeber data contain numeric value
#height = 12.4
#age = 20
#print('yuor heght is'+ '' + str(height))
#print(age + height)

#4 boolean = true or false

#converting from one datatype to another 
#str('12')
#float(2)
#int('67')

#2 accepting userInput in python
#default input come in string so you have to convert it
# name = input('what is your name')
# age = input('How old ae you :')
# print('hello '+ name)

#3 if and elsif statement
#this is the way to write it in python
# name = int(input('enter a number'))

# if name > 1:
#  print('good')
# elif name == 1:
#  print('Not bad')

#4 logical operatore = and, or and not
#same logic with javascripte just replace the && with and same with the rest
# but for not  have to put the conditions inside parantaces eg
#name = int(input(''))
#if not(name < 6):
 #print('changed')

#5i while loop 
#len = lengnth
#none = null
# print(len('rtt'))
#name = [1,2,3,4,5]
#print(len(name), '' + 'working...')

# while len(name) == 0:
#  name = input('Enter your NAme') 

# print('you name is '+ name)
#name = None
#while not name:
 # name = input('Enter your NAme') 

#print('you name is '+ name)

#5ii for loop 
# for let must have a ending point  must define index or i range accept start and or ending point
for i in range(2,12 + 1,):
 print(i)
 #time.sleep(1)

print('Happy new year')


me = ['hmza','suleiman','brad']
print(len(me), 'the length of me')
for i in (me):
   print(i)

# ternary operator in python
name = 30

print('greate') if name > 40  else print('under age')



