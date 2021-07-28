#operating system module
import os
import csv


dir_path = os.path.dirname(os.path.realpath(__file__))#original path
path = os.path.join(dir_path, "Directory")
try:
    os.mkdir(path)  #create a new directory in the current path
except :
    pass

#-------------------------------------------------------------------------

os.chdir(path) #change directory to the empty directory
dir_list = os.listdir(path) # list of current files in the directory as a list
if "Cust.csv" not in dir_list:# if it is not already created in the directory
    with open('Cust.csv', 'w') as fp:
        pass
if "Orders.csv" not in dir_list: #if it is not already created in the directory
    with open('Orders.csv', 'w') as fp:
        pass

#--------------------------------------------------------------------------

def getID(name):
    csv_file = csv.reader(open('Cust.csv', "r"), delimiter=",")

    # loop through the csv list
    for row in csv_file:

        if(row[1] == name):# if the name was found in the sec index of the list

            return row[0]# return the first index which is the id.


#---------------------------------------------------------------------------


def getList_of_orders(id):
    id = str(id)# convert int to string
    list = []
    csv_file = csv.reader(open('Orders.csv', "r"), delimiter=",")
    # loop through the csv list
    for row in csv_file:


        if (row[1] == id):  # if the id was found in the sec index of the list


            string = row[0]+" "+ row[2]+" "+row[3]
            list.append(string)

    return list

#----------------------------------------------------------------------------
def  getSum_of_orders(list:list):

    sum =0

    for i in range(len(list)):
        word = str(list[i])
        word = word[::-1]
        word = word.split().pop(0)
        word = word[::-1]
        sum = sum + int(word)

    return sum

#------------------------------------------------------------------------------

print("Test-1- : " , getID("dani"))
print("Test-2- : " ,getList_of_orders(10))
print("Test-3- : " ,getSum_of_orders(getList_of_orders(10)))




