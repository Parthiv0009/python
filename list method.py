# MOST USEFULL LIST METHODS

num = [1,4,8,5,6,9,15,11,18]  #add any element in last 
num.append(7)
print(num)  

num.sort()   # sort any list in accending order like: 0,1,2,3,4
print(num)



word = ['a','c','b','f','e','d']
word.sort(reverse=True)        #this make list fully reverse like : 5,4,3,2,1,0
print (word)

word = ['a','c','b','f','e','d']
word.reverse()       #this make list in mirror reverse like : before "1,5,8,3,4,"
print (word)                                               #: after  "4,3,8,5,1"


num = [1,3,2,4]
num.insert(1,9)   #this method add value in list on index that user want.
print (num)       # num.insert(1,9) where 1 is index and 9 is value

num = [1,3,2,4]
num.remove(3)    #this method first find value that user want remove in this case 
print (num)      #we want remove 3 so method find first 3 in this list and remove simple 


num = [1,3,2,4]
num.pop(2)     #this method work like remove method but here user enter index
print(num)     # of value that he want remove.


##in python there are  have many more method of list available.









