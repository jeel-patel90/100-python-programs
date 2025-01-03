##### here i created a list called students marks...

student_mark = [98, 95, 90, 92, 95, 97]

### here i use append method to add another value...

print(student_mark)
student_mark.append(100)
print("updated list : ",student_mark)

### here i use remove method to remove added value...
print(student_mark)
student_mark.remove(100)
print("updated list : ",student_mark)

### here i use len method to print the lenght of list...

lenght = len(student_mark)
print("This is the total lenght of list, which is : ",lenght)

### here i use sort method to sort as ascending order of added value...
print(student_mark)
student_mark.sort()
print("sorted list : ",student_mark)

### here i use count method to print how many time 100 is stored in list...
count = student_mark.count(100)
print(count)

### here i use count method to print how many time 100 is stored in list...
print(student_mark)
student_mark.insert(5, 100)
print("updated list : ",student_mark)

### here i use count method to print how many time 100 is stored in list...
print(student_mark)
student_mark.pop(3)
print("updated list : ",student_mark)