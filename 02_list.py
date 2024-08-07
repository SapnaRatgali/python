#list

'''
mylist = ["banana","apple","mango"]

print(mylist)

'''
'''

#INTEGER TYPE LIST


a=22
b=5
c=81
d=26

ages=[22,5,81,26]

print(ages)

#access the 3rd value

print(ages[2])      #print(ages[index])
                    #so 3rd value is 81 but index is 2

print("The ages on 4th and 2nd position is :")
print(ages[3],ages[1])


#float type list


print("the username are :")
username=['Sapna','amaya','mhadvi']
print(username)

print("the height in foot are :")
height_in_foot=[5.5,6.8,4.2]
print(height_in_foot)

'''

#NESTED LIST - LIST WITHIN LIST

'''
print("NESTEDL IS AS FOLLOWED:")
nestedl=[[12,35],[54,44,8],[9]]
print(nestedl)

print(nestedl[0])
print(nestedl[0][1])

print(nestedl[2])
print(nestedl[2][-1])

print(nestedl[1])
print(nestedl[1][2])

'''

#MIXED LIST

nestedList = [["pen","book","laptop"],[200,500,25000],[2,3,0]]

print("The entire list contains stationary,price,quantity:")
print(nestedList)

print("The price are :")
print(nestedList[1])

print("The stationary are :")
print(nestedList[0])
print("The stationary at 3rd position is :")
print(nestedList[0][2])

print()


person=["sapna",55.788,60]
print()
print(person)


#add email in person
person[-1]="sapna@gmail.com"

print(person)
print(person*2)
print(person*3)
print()

#add 2 list together
print("the combined list contains nestedList and person list")
combinedlist=nestedList+person
print(combinedlist)


#FUNCTIONS/METHODS

#add element without overriding - append(val)
print()

listing = [12,35,46,58,25,64]
print(listing)
listing.append(100)
print(listing)

#insert element at a specific index position- index(indexNo,val)
print()
listing.insert(0,500)
print("after inserting 500 in the list")
print(listing)


#remove an elemnt from list
print()
print(listing)
listing.remove(500)
print("after removing 500 from list")
print(listing)


#clear entire list --clear()
print()
print("This is list which after clearing will be empty")
print(listing)
#print("this is an empty list")
#listing.clear()
#print(listing)
print()
'''
id=[1,2,3,1]
print(id)
id.remove(3)
print(id)

'''

#index position remove element -- .pop(indexno)

print(listing)
listing.pop(2)
print(listing)

#slicing -it ask for range for print list element

print("This is the list")
print(listing)

print(listing[0:2])
print(listing[2:])  #till end
print(listing[:-1]) #starting till end

print(listing[:2]) 



#length
num = [8, 2, 1, 4, 5]
print("The length is:")
print(len(num))

print()

num_len=len(num)
print("The length of list is :",num_len)
print()

#sort

li = sorted(num)
print("The sorted list is :",li)
print()


#reverse
myl = [1, 2, 3, 4, 5]
myl.reverse()
print(myl) 

print(myl.reverse())
