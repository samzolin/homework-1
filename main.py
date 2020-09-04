# Author: Samantha Zolin saz5193@psu.edu 
lettergrade1 = input("Enter your course 1 letter grade: ")
credit1 = input("Enter your course 1 credit: ")
credit1 = float(credit1)
if lettergrade1 == "A":
  gradepoint1 = 4.0
  print("Grade point for course 1 is: 4.0")
elif lettergrade1 == "A-":
  gradepoint1 = 3.67
  print("Grade point for course 1 is: 3.67")
elif lettergrade1 == "B+":
  gradepoint1 = 3.33
  print("Grade point for course 1 is: 3.33")
elif lettergrade1 == "B":
  gradepoint1 = 3.0
  print("Grade point for course 1 is: 3.0")
elif lettergrade1 == "B-":
  gradepoint1 = 2.67
  print("Grade point for course 1 is: 2.67")
elif lettergrade1 == "C+":
  gradepoint1 = 2.33
  print("Grade point for course 1 is: 2.33")
elif lettergrade1 == "C":
  gradepoint1 = 2.0
  print("Grade point for course 1 is: 2.0")
elif lettergrade1 == "D":
  gradepoint1 = 1.0
  print("Grade point for course 1 is: 1.0")
elif lettergrade1 == "F":
  gradepoint1 = 0.0
  print("Grade point for course 1 is: 0.0")
else: 
  gradepoint1 = 0.0
  print("Grade point for course 1 is: 0.0")

lettergrade2 = input("Enter your course 2 letter grade: ")
credit2 = input("Enter your course 2 credit: ")
credit2 = float(credit2)
if lettergrade2 == "A":
  gradepoint2 = 4.0
  print("Grade point for course 2 is: 4.0")
elif lettergrade2 == "A-":
  gradepoint2 = 3.67
  print("Grade point for course 2 is: 3.67")
elif lettergrade2 == "B+":
  gradepoint2 = 3.33
  print("Grade point for course 2 is: 3.33")
elif lettergrade2 == "B":
  gradepoint2 = 3.0
  print("Grade point for course 2 is: 3.0")
elif lettergrade2 == "B-":
  gradepoint2 = 2.67
  print("Grade point for course 2 is: 2.67")
elif lettergrade2 == "C+":
  gradepoint2 = 2.33
  print("Grade point for course 2 is: 2.33")
elif lettergrade2 == "C":
  gradepoint2 = 2.0
  print("Grade point for course 2 is: 2.0")
elif lettergrade2 == "D":
  gradepoint2 = 1.0
  print("Grade point for course 2 is: 1.0")
elif lettergrade2 == "F":
  gradepoint2 = 0.0
  print("Grade point for course 2 is: 0.0")
else: 
  gradepoint2 = 0.0
  print("Grade point for course 2 is: 0.0")

lettergrade3 = input("Enter your course 3 letter grade: ")
credit3 = input("Enter your course 3 credit: ")
credit3 = float(credit3)
if lettergrade3 == "A":
  gradepoint3 = 4.0
  print("Grade point for course 3 is: 4.0")
elif lettergrade3 == "A-":
  gradepoint3 = 3.67
  print("Grade point for course 3 is: 3.67")
elif lettergrade3 == "B+":
  gradepoint3 = 3.33
  print("Grade point for course 3 is: 3.33")
elif lettergrade3 == "B":
  gradepoint3 = 3.0
  print("Grade point for course 3 is: 3.0")
elif lettergrade3 == "B-":
  gradepoint3 = 2.67
  print("Grade point for course 3 is: 2.67")
elif lettergrade3 == "C+":
  gradepoint3 = 2.33
  print("Grade point for course 3 is: 2.33")
elif lettergrade3 == "C":
  gradepoint3 = 2.0
  print("Grade point for course 3 is: 2.0")
elif lettergrade3 == "D":
  gradepoint3 = 1.0
  print("Grade point for course 3 is: 1.0")
elif lettergrade3 == "F":
  gradepoint3 = 0.0
  print("Grade point for course 3 is: 0.0")
else: 
  gradepoint3 = 0.0
  print("Grade point for course 3 is: 0.0")


GPA = (gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3) 

print(f"Your GPA is: {GPA}")

 