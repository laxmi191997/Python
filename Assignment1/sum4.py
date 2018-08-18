mrp = int(input("Enter the value for MRP"))
offerno = int(input("Enter the value for offer no"))
if(offerno == 1):
    discount = mrp * 0.25
    print(" For offer no {} Final value after discount is {}".format(offerno,discount))
elif(offerno == 2):
    discount = mrp * 0.4
    print("For offer no {} Final value after discount is {}".format(offerno,discount))
elif(offerno == 3):
    discount = mrp * 0.6
    print("For offer no {} Final value after discount is {}".format(offerno,discount))
elif(offerno == 4):
    discount = mrp * 0
    print("For offer no {} Final value after discount is {}".format(offerno,discount))
else:
    print("No such discount")

    
