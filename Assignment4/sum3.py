s=str(input("Enter a string"))
vowel_list=['a','e','i','o','u','A','E','I','O','U']
for each in s:
    if each in vowel_list:
        print("Buzz")
    else:
        print(each)
