#dictionarries = object
band = {
  'lang': 'eng',
  'name': 'himxa'
}
#another way of creating dic
band2 = dict(lang='eng',name='himxa')
print(band)
print(band2)
# to get value from dic
print(band['lang'])
print(band.get('name'))

#to get the keys or values
print(band.keys())
print(band.values())

#to change values or to resign value
band['lang'] = 'usa'
print(band)
# can also add
band['newme'] = 'am good'
# another way for adding and updating
band.update({'lang': 'broken', 'name': 'bradoo'})
print(band)

#to remove an item
# put the elemt to be remove inside the pop
print(band.pop('lang'))
print(band)



#to delete
del band['name']
print(band)

# delte a doctionalry
del band2
print(band)
# use thsi to create refresnce
#ban2 = band 
#to create copy
band2 = band.copy()
band2['song'] = 'sprinter'
print(band2)
print(band)
#or use the dict function constructor function
band3 = dict(band2)
print(band3)


#Nested dictionalry
number1 = {
  'name' : 'plant',
  'like': 'water'

 }
number2 = {
  'name' : 'page',
  'like': 'sand'

 }
band4 = {
  'member1' : number1,
  'member': number2

}
print(band4['member1']['name'])

#Sets
nums = {1,2,3,4}
#or
nums1 = set((1,2,3))
print(nums,nums1)

#no duplicate are allowed in set
numis = {1,2,3,8}
print(numis, '','here')
# true is 1 and false is 0
numm = {1,True,2,False,35,0}
print(numm)
# to get a value out it use the same thing with list
# to get value 
numm.add(8)
print(numm)

#you can use update method with list,tuples and dictionaries, tto

#merge two sets to create a nw set
one = {1,2,3}
two = {5,6,7}
mynewset = one.union(two)
print(mynewset)

# to keep only duplicate
one1 = {1,2,3}
two2 = {2,3,4}
one1.intersection_update(two2)
print(one1)

 #to keep everything except thr duplicate
one1 = {1,2,3}
two2 = {2,3,4}
one1.symmetric_difference_update(two2)
print(one1)