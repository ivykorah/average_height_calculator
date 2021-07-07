
student_heights = input("Input a list of student heights separated by spaces ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum_height = 0
for heights in student_heights:
  sum_height += heights

count = 0
for items in student_heights:
  count += 1

average_height = sum_height / count
print(f"The average heights of the students in this class is: {round(average_height)}")
