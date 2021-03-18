print("welcome to our hotel , please choose room type : ")
print("1.single (150 nis)")
print("2.double (250 nis)")
print("3.suite (600 nis)")
room = int(input())
if(room== 1 or room ==2 or room == 3):
    print("how many nights? ")
    nights = int(input())
    if (nights > 0):
        print("do you want a breakfast (50 nis) press y or n ")
        breakfast = input()
        if (breakfast != "y" and breakfast != "n"):
            print("illegal input !")

        if (room == 1):
            if breakfast == "y":
                reser = 150 * nights + 50
                print("your reservation for a single room for ", nights, " nights with breakfast is done ")
                print("you'll pay ", reser, "nis")

            else:
                reser = 150 * nights
                print("your reservation for a single room for ", nights, " nights without breakfast is done ")
                print("you'll pay ", reser, "nis")

        if (room == 2):
            if breakfast == "y":
                reser = 250 * nights + 50
                print("your reservation for a double room for ", nights, " nights with breakfast is done ")
                print("you'll pay ", reser, "nis")

            else:
                reser = 250 * nights
                print("your reservation for a single room for ", nights, " nights without breakfast is done ")
                print("you'll pay ", reser, "nis")

        if (room == 3):
            if breakfast == "y":
                reser = 600 * nights + 50
                print("your reservation for a suite room for ", nights, " nights with breakfast is done ")
                print("you'll pay ", reser, "nis")

            else:
                reser = 600 * nights
                print("your reservation for a single room for ", nights, " nights without breakfast is done ")
                print("you'll pay ", reser, "nis")


    else:

      print("illegal input")
else:
    print("illegal input ")