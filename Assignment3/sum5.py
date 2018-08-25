l=['Grapes','Apple','Mango','Apple','Mango','Apple','Grapes','Mango','Mango']
a=set(l)   #To get the unique for list we used set and stored in a varible
#print(a)
word_list=list(a)  #converting variable a that is a set to list and storing in word_list.
#print(word_list)
word_list.sort()
print("word_list =",word_list)
a=l.count('Apple')
b=l.count('Grapes')
c=l.count('Mango')
print("count_list =",[a,b,c])


