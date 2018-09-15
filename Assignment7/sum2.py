def emical():
    p=int(input('Enter amount'))
    r=int(input("Enter rate of interest"))
    n=int(input('Enter number of years'))
    r=r/(12*100)
    n=n*12
    emi=(p*r*pow((1+r),n)/pow((1+r),(n-1)))
    print(emi)
emical()
