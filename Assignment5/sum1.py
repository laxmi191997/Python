s=str(input("Enter a string"))
a=s.split()
#b=max(a,key=len)
#print(b)
#print(a)
longest_word =[]
for each in a:
    if each not in longest_word:
        longest_word.append(each)
        
#print(longest_word)
for each in longest_word:
    if len(each)>len(longest_word):
        longest_word =each

print(longest_word)
