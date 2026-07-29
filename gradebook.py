students={
   "ashveer":85,
    "divit":75,
    "samar":90,
    "vedant":86
}

total=0
for score in student.values():
    total+= score
print("average:", total/len(students))

top= max(students,key=students.gets)