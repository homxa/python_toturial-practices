
# def hello(hamza= 'himxa'):
#   print('hello world ' + hamza )
def hello(i,o):
  #check if it not number
  if(type(i) is not int or type(o) is not int):
    return
  return i + o

total = hello(2,2)
print(total)   

if 1 not in ['1','2',4]:
   print('working')

   #to modified global value 
#using a nested function value use nonlocal insted of global
 #Here  using  global
user = 'himxa'
def text():
  global user
  user = 'Branded'
  print(user)
text()  

me = None

print(me)