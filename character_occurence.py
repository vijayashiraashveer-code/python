word = input("enter a word")
char = input("Enter a character")
count = 0
for i in word:
    if i == char:
       count += 1
print("total occurrences:", count)