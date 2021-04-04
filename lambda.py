#sorting coordinates due to the x axis
coor  = [(4,2) , (5,9) , (1,4)]
sortedcoor = sorted(coor , key= lambda x : x[0])
print(sortedcoor)

#sorting coordinates due to the sum of each coor
coor  = [(4,2) , (5,9) , (1,4)]
sortedcoor = sorted(coor , key= lambda x : x[0]+ x[1])
print(sortedcoor)

#it changes the values of each index in the list according to a specific equation
num= [2,3,7,9,4,6,3,4,15,17]
maping = map(lambda x : x*2,num)
print(list(maping))


#it creates a new list according to the things listed in lambda equation
filtering = filter(lambda x : x %3==0 , num)
print(list(filtering))


#creating a list from a single line loop and else if 
newlist = [ number**2 for number in range(10) if number %2 == 0]
print(newlist)

