marks = int(input("enter the marks: "))

if 91 <= marks <= 100:
    grade = "s"
elif 81 <= marks < 91:
    grade = "A"
elif 71 <= marks < 81:
    grade = "b"
elif 61 <= marks < 71:
    grade = "c"
elif 51 <= marks < 61:
    grade = "d"
elif 41 <= marks < 51:
    grade = "fail"
else:
    grade = "Invalid marks entered"

print("grade:", grade)