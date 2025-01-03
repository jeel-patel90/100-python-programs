a = int(input("Enter your 1st number : "))
b = int(input("Enter your 2nd number : "))
#this is third variable for swapp the a and b variable
c = 0

#first we add c = a so a's value and c's value become similar 
c = a
#than we add a = b so a's and b's value become similar
#so now b's value is a
a = b
# as we above made a and c simialar so whatever c's value is now b's value too
b = c

print(a,"value after swap")
print(b,"value after swap")