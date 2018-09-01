s=input("Enter a string")
a=s.split()
Excluded_word=['and','is','are','to']
print(a)
count=0
for each in a:
    if(each=='and' or each=='is' or each=='are' or each=='to'):
        count+=1
print("Number of exculded word are:")
print(count)
    
