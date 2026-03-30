#------------------------------------------------Task 1---------------------------------------------

raw_students = [
    {"name": "  ayesha123 SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]
processed_students = []

# Loop through raw student list
for students in raw_students:

    #Q1.1 Strip and Capitalize
    name = students["name"].strip().title()

    #Q2 check if name string is alphanumeric. Sprint string into two parts, iterate and check via valid flag
    valid = True
    for name_alp in name.split():
        if not name_alp.isalpha():
            valid = False
            break

    if valid: print("✓ Valid name")
    else: print("✗ Invalid name")

    #Q1.2 Change string Roll no. into Integer
    roll_no = int(students["roll"])

    int_marks = []
    #Q1.3 Split marks string into List. Then Iterate list and change each value to Integer
    for marks in students["marks_str"].split(','):
        int_marks.append(int(marks))

    #Q3 Print as per required Template
    print("==================")
    print(f"Student :{name}")
    print(f"Roll No :{roll_no}")
    print(f"Marks :{int_marks}")
    print("==================")

    #Store processes students in another list for Q4
    processed_students.append({"name": name, "roll": roll_no, "marks": int_marks})


for pro_student in processed_students:
    # Q4 Fetch Roll value from processes students list, If Roll no. is 103, print in All Caps and Lowercase

    if pro_student["roll"] == 103:
        print(f"Student :{pro_student["name"].upper()}")
        print(f"Student :{pro_student["name"].lower()}")



#------------------------------------------------Task 2---------------------------------------------
student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]


#Q1 Loop subject as per length & fetch parallel index in marks. Compare and assign Grades

for sub in range(len(subjects)):
    mark = marks[sub]
    if mark >= 90: grade = "A+"
    elif mark >= 80: grade = "A"
    elif mark >= 70: grade = "B"
    elif mark >= 60: grade = "C"
    else: grade = "F"
    print(f"Subject: {subjects[sub]}, Marks: {mark}, Grade: {grade}")

total_marks = sum(marks)

#Q2.1 Print Total from sum of marks
print(f"\n\nTotal Marks = {total_marks}")
#Q2.2 total Sum divided by length of marks array will be average
print(f"Average: {round(total_marks/len(marks),2)}")

#Q2.3 Get max from Marks list, then get index. Use same index to fetch subject
max_marks = max(marks)

print(f"Highest scoring subject: {subjects[marks.index(max_marks)]} Marks Scored: {max_marks}")
#Q2.4 Get min from Marks list, then get index. Use same index to fetch subject
min_marks = min(marks)
print(f"Lowest scoring subject: {subjects[marks.index(min_marks)]} Marks Scored: {min_marks}")


#Q3
done = "false"

new_subject = []

# Keep loop running until user provides done as an input
while True:
    subject = input("\n\nPlease Enter Subject Name (Enter 'Done' at anytime to Stop) ")
    if subject.lower() != "done":

        marks_input = input("\nEnter Marks (0-100) for ")
        #check is marks input is a digit
        if marks_input.isdigit():
            marks_int = int(marks_input)

            #Marks enter must be between 0 & 100
            if 0 <= marks_int <= 100:
                # Add input to Subject List & marks List once all validations are satisfied
                new_subject.append(subject)
                marks.append(int(marks_input))
            else: print("do not crash, and do not add invalid entries to the list.")
        else: print("do not crash, and do not add invalid entries to the list.")
    else: break

print(f"New Subjects Added: {new_subject}")

print(f"Marks updated List: {marks}")
print(f"Updated Average: {sum(marks)/len(marks)}")




#------------------------------------------------Task 3---------------------------------------------
from xml.dom.minidom import ProcessingInstruction

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print("Name                     | Average | Status")
print("---------------------------------------------------")

pass_count = 0
fail_count = 0
topper_avg = 0
total_avg = 0

topper_name = ""

#For loop with dynamic length for the list
for index in range(len(class_data)):
    students = class_data[index]
    for stu_index in range(len(students)):
        name = students[stu_index]
        #incrementing index to get marks list
        stu_index+=1
        average = round(sum(students[stu_index])/len(students[stu_index]),2)


        #calculate status
        status = ""
        if average >= 60:
            status = "Pass"
            pass_count += 1
        else:
            status = "Fail"
            fail_count += 1

        #Print Results
        print(f"{name:<25}| {average:<7} | {status}")

        #Calculating total Average sum of Class
        total_avg += average

        #Topper calculation & average
        if average > topper_avg:
            topper_avg = average
            topper_name = name
        break

#Summary
print(f"\n\nSummary\nNo. of Students Passes: {pass_count} \nNo. of Students Failed: {fail_count}")
print(f"\nClass Topper: {topper_name} {topper_avg}")
print(f"\nClass Average: {round(total_avg/len(class_data),2)}")




#------------------------------------------------Task 4---------------------------------------------
essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

#4.1 Strip Essay
clean_essay = essay.strip()
print(f"Clean Essay \n{clean_essay}")

#4.2 Title case
clean_essay_title = clean_essay.title()
print(f"\nTitle Case \n{clean_essay_title}")

#4.3 Count python
count_python = clean_essay.count("python")
print(f"\nCount of python \n{count_python}")

#4.4 Replace python with Python 🐍
new_clean_essay = clean_essay.replace("python", "Python 🐍")
print(f"\nReplaced Clean Essay \n{new_clean_essay}")

#4.5 Replace python with Python 🐍
clean_essay_list = clean_essay.split(". ")
print(f"\nClean Essage List \n{clean_essay_list}")

#4.6: Print numbered sentences
print("\nNumbered Sentences:")

for essay_val in range(len(clean_essay_list)):
    val = clean_essay_list[essay_val]

    # Add period if missing
    if not val.endswith("."):
        val = val + "."

    print(f"{essay_val + 1}. {val}")