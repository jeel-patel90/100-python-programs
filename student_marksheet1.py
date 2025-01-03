# this is the program of pythob for student's marksheet...
name = input("Enter Your Name: ")
roll_no = int(input("Enter Your Roll No: "))
sub1=int(input("Enter Your Marks Sub1: "))
sub2=int(input("Enter Your Marks Sub2: "))
sub3=int(input("Enter Your Marks Sub3: "))
sub4=int(input("Enter Your Marks Sub4: "))
sub5=int(input("Enter Your Marks Sub5: "))

total=sub1+sub2+sub3+sub4+sub5
percentage=total/5

print("Name: ",name)
print("Roll No: ",roll_no)
print("  ")
print("Sub 1: ",sub1)
print("Sub 2: ",sub2)
print("Sub 3: ",sub3)
print("Sub 4: ",sub4)
print("Sub 5: ",sub5)
print(" ")
print("Total: ",total)
print("Percentage: ",percentage,"%")
print("  ")
