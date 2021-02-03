s = 'azcbobobegghakl'

#Write a program that prints the number of times the string 'bob' occurs in s
#Assume 's' is a string of lower case chars

#set variable 'bob' counter to zero 
countbob = 0

#set iteration counter to zero 
i = 0

#for loop that takes the range of s and iterates over it
for i in range(len(s)):
    #identify bob in s by checking current and next 2 charachters
    if (s[i:i+3] == 'bob'):
        #add bobs counted to countbob total
        countbob +=1

#return bobs counted        
print("Number of bobs in s is: " + str(countbob))
