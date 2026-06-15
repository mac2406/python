name = input("Enter Student name: ")
marks = int(input("Enter marks: "))

if marks <= 100 and marks >= 0:
    if marks >= 90:
        Grade = "A+"
        Result = "Pass"
    elif marks >= 80 and marks <= 89:
        Grade = "A"
        Result = "Pass"
    elif marks >= 70 and marks <= 79:
        Grade = "B"
        Result = "Pass"
    elif marks >= 60 and marks <= 69:
        Grade = "C"
        Result = "Pass"
    elif marks >= 50 and marks <= 59:
        Grade = "D"
        Result = "Pass"
    else:
        Grade = "Fail"
        Result = "Fail"


    print("------------------------")
    print("STUDENT REPORT")
    print("------------------------")
    print(f"Student: {name}")
    print(f"Marks: {marks}")
    print(f"Grade: {Grade}")
    print(f"Result: {Result}")
    print("------------------------")

else:
    print("Invalid marks")