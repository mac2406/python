name = input("Student name: ")
course = input("Course name: ")
tuition = int(input("Tuition fees: "))
hostel = int(input("Hostel fees: "))
library = int(input("Library fees: "))

total_fees = tuition + hostel + library

print("-------------------------")
print("STUDENT FEE RECEIPT")
print("-------------------------")

print(f"Student name: {name}")
print(f"Course name: {course}")
print(f"Tuition fees: {tuition}")
print(f"Hostel fees: {hostel}")
print(f"Library fees: {library}")

print(f"Total fees: {total_fees}")
print("-------------------------")