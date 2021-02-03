s = "asgafbsdgbchdabcdefbcdefgjed"

#Write a program that prints the longest substring of s in which the letters 
#occur in alphabetical order.

#define 2 variables
longest = s[0]
current = s[0]

# scan the string and iterate over it
for i in s[0:]:
    if i >= current[-1]:
        #concatenate string if above if statement is satisfied
        current += i
        #compare lengths of variables counted and replace longest with 
        #current if true
        if len(current) > len(longest):
            longest = current
    else:
        current = i
print ("Longest substring in alphabetical order is:", longest)
