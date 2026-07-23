

student_marks = [85, 92, 78, 90, 64]
sample_values = [10.5, 20.3, 15.8]


num_students = len(student_marks)
print(f"Number of students: {num_students}")

first_mark = student_marks[0]   
last_mark = student_marks[-1]   
print(f"First mark: {first_mark}, Last mark: {last_mark}")


top_three = student_marks[0:3]  
print(f"Top three marks: {top_three}")

total_score = 0
for mark in student_marks:
    total_score += mark         

average_score = total_score / num_students
print(f"Total score: {total_score}")
print(f"Average score: {average_score:.2f}")
