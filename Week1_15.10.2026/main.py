import subprocess

import numpy as np

# === Exercise 1.1 ===

# names = np.array([
#     "John Stevenson",
#     "Jane Smith",
#     "Tim Wilson",
#     "Kate Stevenson",
#     "Kate Palmer",
#     "Tom Eastman",
#     "Laura Green",
#     "Mike Watson",
#     "Sally Black",
#     "Mark Ramsey"
#     ])

# print(*names[[1, 7]])

names = [
    "John Stevenson",
    "Jane Smith",
    "Tim Wilson",
    "Kate Stevenson",
    "Kate Palmer",
    "Tom Eastman",
    "Laura Green",
    "Mike Watson",
    "Sally Black",
    "Mark Ramsey"
    ]

subprocess.run(["cls"], shell=True)

def add_employee():
    employee_name = input("=== Add new employee ===\n\nEmployee Name: ")
    names.append(employee_name)
    subprocess.run(["cls"], shell=True)

def display_employees():
    for i in names:
        print(i)
    input("\nPress ENTER to return to menu")
    subprocess.run(["cls"], shell=True)


while True:

    print("\n === Menu === ")
    print("\n1. Add an employee\n2. Display all employees\n3. Quit\n")

    try:
        menu_choice = int(input("Please enter number choice: "))
    except ValueError:
        subprocess.run(["cls"], shell=True)
        print("Please enter a valid choice (number)")
        continue

    if menu_choice == 1:
        subprocess.run(["cls"], shell=True)
        add_employee()
    elif menu_choice == 2:
        subprocess.run(["cls"], shell=True)
        display_employees()
    elif menu_choice == 3:
        subprocess.run(["cls"], shell=True)
        print("You've quit, loser")
        quit()
    else:
        subprocess.run(["cls"], shell=True)
        print("Please enter a valid choice")