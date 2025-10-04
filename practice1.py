# Input marks of 5 subjects
marks = []
print("Enter marks obtained in 5 subjects:")

for i in range(5):
    mark = float(input(f"Subject {i+1}: "))
    marks.append(mark)

# Calculate the average
average = sum(marks) / 5

# Grade assignment based on average
if 91 <= average <= 100:
    grade = "A1"
elif 81 <= average < 91:
    grade = "A2"
elif 71 <= average < 81:
    grade = "B1"
elif 61 <= average < 71:
    grade = "B2"
elif 51 <= average < 61:
    grade = "C1"
elif 41 <= average < 51:
    grade = "C2"
elif 33 <= average < 41:
    grade = "D"
elif 21 <= average < 33:
    grade = "E1"
elif 0 <= average < 21:
    grade = "E2"
else:
    grade = "Invalid marks entered"

# Display the grade
print(f"Average Marks: {average}")
print(f"Grade: {grade}")
