print("1: Mathematical Operations")
print("2: Simple Bio")

option=int(input("Choose your choice : \n"))
if(option ==1):
    FirstNum = int(input("please write your first number : \n"))
    SecNum = int(input("please write your second number : \n"))
    print("choose one of the following mathematical operations by (its number): ")
    print("1. + \n2. - \n3. / \n4. * \n")
    operation = int(input())
    i=0
    while(i!=-1):

        if (operation == 1):
            answer = FirstNum + SecNum
            print("the answer is :" , answer)
            i =-1
            break
        if (operation == 2):
            answer = FirstNum - SecNum
            print("the answer is :", answer)
            break
        if (operation == 3):
            answer = FirstNum / SecNum
            print("the answer is :", answer)
            break
        if (operation == 4):
            answer = FirstNum * SecNum
            print("the answer is :", answer)
            break
        else:
            print("please enter a enter a number in range of 1-4 : ")
            operation = int(input())


if(option == 2):
    name = input("Hello , what's your name? \n ")
    city =input("From which city do you come from ? \n")
    fatherName= input("What's your father's name ? \n")
    motherName = input("What's your mother's name ? \n" )
    dictionary ={ "Name" : name , "City" : city ,"FatherName": fatherName ,"MotherName": motherName}
    print("Hello " , dictionary.get("Name"),",")
    print("We have received your order and it will be delivered to:  ", dictionary.get("City") ,)
    print("If there are any problems with the order , we will contact your father :", dictionary.get("FatherName") , " or your mother: ", dictionary.get("MotherName"))
    print("Thank you so much ! ")













