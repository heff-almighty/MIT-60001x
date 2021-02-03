#Write a program that counts up the number of vowels contained in the string
#Assume 's' is a string of lower case chars

#set variables for vowels and set variable 's' 
vowels = ['a', 'e', 'i', 'o', 'u']
s = "abcde"

# set variable to count whatever i want to count
count = 0

#write for loop to count vowels and disregard consonants
for char in s:
    if char in vowels:
        count +=1
print ('Number of vowels: ' + str(count))
