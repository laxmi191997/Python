def student_details():
    name=input('Enter name')
    roll_no=int(input("Enter a roll_no"))

    l=[]
    n=int(input('Enter number of subjects'))
    print('Enter the values')
    for i in range(n):
        l.append(int(input()))
    sum=0
    for each in l:
        sum=sum+each
    x=(sum/(n*100))*100
    print("Percentage of student",name,"is",x)
    if(x>=60):
        print("Grade is first class")
    elif(x>=40):
        print("Grade is second class")
    else:
        print("Fail")
def percent():
    student_details()
def display():
    percent()
display()
