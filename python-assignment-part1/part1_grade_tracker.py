# part1_grade_tracker.py

def task_1():
    print("=== Task 1: Data Parsing & Profile Cleaning ===\n")
    raw_students = [
        {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
        {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
        {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
        {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
        {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
    ]

    cleaned_students = []

    for student in raw_students:
        # Loop through raw_students and for each student, produce a cleaned version where:
        # name has leading/trailing whitespace removed and is converted to Title Case.
        clean_name = student["name"].strip().title()
        
        # roll is converted from a string to an integer.
        clean_roll = int(student["roll"])
        
        # marks_str is split on ", " and each element is converted to an integer, producing a marks list.
        clean_marks = [int(m) for m in student["marks_str"].split(", ")]
        
        cleaned_students.append({
            "name": clean_name,
            "roll": clean_roll,
            "marks": clean_marks
        })
        
        # Verify the name is valid: check that every word in the name contains only alphabetic characters. 
        # Print "✓ Valid name" or "✗ Invalid name" next to each student.
        is_valid = all(word.isalpha() for word in clean_name.split())
        validity_str = "✓ Valid name" if is_valid else "✗ Invalid name"
        print(f"{clean_name}: {validity_str}")
        
        # Print a formatted profile card for each cleaned student using f-strings
        print("================================")
        print(f"Student : {clean_name}")
        print(f"Roll No : {clean_roll}")
        print(f"Marks   : {clean_marks}")
        print("================================")
        print()

    # After processing all students, print the name in ALL CAPS and lowercase for the student with roll number 103.
    for student in cleaned_students:
        if student["roll"] == 103:
            print(f"Student 103 Name (UPPER): {str(student['name']).upper()}")
            print(f"Student 103 Name (lower): {str(student['name']).lower()}")
            break
    print("\n" + "="*50 + "\n")


def task_2():
    print("=== Task 2: Marks Analysis Using Loops & Conditionals ===\n")
    student_name = "Ayesha Sharma"
    subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
    marks        = [88, 72, 95, 60, 78]

    # Helper function for grade calculation
    def get_grade(m):
        if m >= 90: return "A+"
        elif m >= 80: return "A"
        elif m >= 70: return "B"
        elif m >= 60: return "C"
        else: return "F"

    print(f"Marks for {student_name}:")
    # Using a for loop, print each subject alongside its marks and a grade label
    for i in range(len(subjects)):
        subj = subjects[i]
        m = marks[i]
        grade = get_grade(m)
        print(f"{subj}: {m} ({grade})")

    total_marks = sum(marks)
    average_marks = round(float(total_marks) / len(marks), 2)  # type: ignore
    max_mark = max(marks)
    max_idx = marks.index(max_mark)
    min_mark = min(marks)
    min_idx = marks.index(min_mark)

    # Calculate and print total, average, highest, lowest
    print(f"\nTotal marks: {total_marks}")
    print(f"Average marks: {average_marks}")
    print(f"Highest scoring subject: {subjects[max_idx]} ({max_mark})")
    print(f"Lowest scoring subject: {subjects[min_idx]} ({min_mark})\n")

    # Using a while loop, simulate a marks-entry system
    print("Enter new subjects and marks (type 'done' to stop):")
    new_subjects_count: int = 0
    while True:
        subj = input("Subject name: ")
        if subj.lower() == 'done':
            break
        m_input = input(f"Marks for {subj} (0-100): ")
        try:
            m = int(m_input)
            if 0 <= m <= 100:
                subjects.append(subj)
                marks.append(m)
                new_subjects_count += 1  # type: ignore
                print(f"Added {subj} with marks {m}.")
            else:
                print("Warning: Marks must be between 0 and 100.")
        except ValueError:
            print("Warning: Please enter a valid number.")

    print(f"\nNew subjects added: {new_subjects_count}")
    new_average = round(float(sum(marks)) / len(marks), 2)  # type: ignore
    print(f"Updated average marks: {new_average}")
    print("\n" + "="*50 + "\n")


def task_3():
    print("=== Task 3: Class Performance Summary ===\n")
    class_data = [
        ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
        ("Rohit Verma",    [55, 68, 49, 72, 61]),
        ("Priya Nair",     [91, 85, 88, 94, 79]),
        ("Karan Mehta",    [40, 55, 38, 62, 50]),
        ("Sneha Pillai",   [75, 80, 70, 68, 85]),
    ]

    print(f"{'Name':<18}| {'Average':<8}| {'Status'}")
    print("-" * 40)

    passed_count: int = 0
    failed_count: int = 0
    highest_avg = 0
    topper_name = ""
    sum_of_averages = 0

    for name, m_list in class_data:
        # Compute average rounded to 2 decimal places
        avg = round(float(sum(m_list)) / len(m_list), 2)  # type: ignore
        # Assign result status: Pass if average >= 60, else Fail
        status = "Pass" if avg >= 60 else "Fail"
        
        # Track counts for later summary
        if status == "Pass":
            passed_count += 1  # type: ignore
        else:
            failed_count += 1  # type: ignore
            
        # Track the top student
        if avg > highest_avg:
            highest_avg = avg
            topper_name = name
            
        # Sum for the class average
        sum_of_averages += avg
        
        # Print a formatted class report using exactly 2 decimal places for visual alignment
        print(f"{name:<18}|  {avg:<6.2f} | {status}")

    # After the table, print summary statistics
    print("\nSummary:")
    print(f"Number of students who passed: {passed_count}")
    print(f"Number of students who failed: {failed_count}")
    print(f"Class topper: {topper_name} ({highest_avg:.2f})")
    
    class_average = round(float(sum_of_averages) / len(class_data), 2)  # type: ignore
    print(f"Class average: {class_average:.2f}")
    print("\n" + "="*50 + "\n")


def task_4():
    print("=== Task 4: String Manipulation Utility ===\n")
    essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

    # Step 1: Strip leading and trailing whitespace. Store as clean_essay.
    clean_essay = essay.strip()
    print("1. Clean Essay:")
    print(clean_essay)
    print()

    # Step 2: Convert clean_essay to Title Case and print it.
    print("2. Title Case:")
    print(clean_essay.title())
    print()

    # Step 3: Count how many times the word "python" appears in clean_essay.
    print("3. Count of 'python':")
    print(clean_essay.count("python"))
    print()

    # Step 4: Replace every occurrence of "python" in clean_essay with "Python 🐍".
    print("4. Replaced 'python':")
    print(clean_essay.replace("python", "Python 🐍"))
    print()

    # Step 5: Split clean_essay into individual sentences by splitting on ". ".
    sentences = clean_essay.split(". ")
    print("5. Sentences list:")
    print(sentences)
    print()

    # Step 6: Print each sentence on a new line, numbered starting from 1. 
    # Add a "." at the end of each sentence if it does not already end with one.
    print("6. Numbered sentences:")
    for idx, sentence in enumerate(sentences, 1):
        sentence = sentence.strip()
        # Add a dot at the end if there isn't one
        if sentence and not sentence.endswith("."):
            sentence += "."
        print(f"{idx}. {sentence}")
    print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    task_1()
    task_2()
    task_3()
    task_4()
