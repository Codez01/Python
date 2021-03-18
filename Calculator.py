import math

def VolumeOfSphere():
    i=0
    error = True

    while(error== True):
        try:

            r = int(input("write the radius of the sphere : "))
            answer = lambda x: (4 / 3) * math.pi * x

            print("The Volume Of The Sphere Is: ", answer(r))
            break


        except:

           print("Please write the radius  of the sphere in numbers !")

           error = True









def MathmaticalOperations():
    x=int(input("please write the value of x: \n"))
    y = int(input("please write the value of y: \n"))
    i =1
    while(i!=-1):
        z = input("please choose one of the following operations only : + , - , / , * \n")
        if (z == "+"):
            answer = lambda x, y: x + y
            print("The Answer is : ", answer(x, y))
            break
        elif (z == "-"):
            answer = lambda x, y: x - y
            print("The Answer is : ", answer(x, y))
            break
        elif (z == "*"):
            answer = lambda x, y: x * y
            print("The Answer is : ", answer(x, y))
            break
        elif (z == "/"):
            answer = lambda x, y: x / y
            print("The Answer is : ", answer(x, y))
            break

        else:

            print("please choose one of the following operations only : + , - , / , *")












