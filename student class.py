class student:
    def __init__(x, name,roll_no,email, marks):
        x.name = name
        x.roll_no = roll_no
        x.email = email
        x.marks = marks

    def viewMarks(x):
        a = int(input('Enter the semester--> '))
        print('Marks of Semester',a,'are: ',x.marks[a-1])
    
    def changeMarks(x):
        a = int(input('Enter the semester--> '))
        x.marks[a-1] = int(input('Enter the marks: '))
        print('Updated marks are: ',x.marks[a-1])

    



stud1 = student('Suraj',1402121059,'rockdrago@abc.com',[67,57,32,60,78])


print(stud1.marks)
stud1.viewMarks()
stud1.changeMarks()

print(stud1.marks)
