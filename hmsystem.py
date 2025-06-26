import os

def add_Patient():
    Name=input("Enter Patient's Name: ")
    Age=input("Enter Age: ")
    Gender=input("Enter Gender: ")
    Disease=input("Enter disease: ")
    with open("patients.txt","a") as f:
        f.write(f"{Name},{Age},{Gender},{Disease}\n")
    print("Patient Added")

def view_Patients():
    if not os.path.exists("patients.txt"):
        print("No patient records found.")
        return
    with open("patients.txt","r") as p:
        for line in p:
            Name,Age,Gender,Disease=line.strip().split(",")
            print(f"Name: {Name}, Age: {Age}, Gender: {Gender}, Condition: {Disease}")

def find_Patient():
    user=input("Enter patient name to search: ").lower()
    found=False
    with open("patients.txt","r") as p:
        for line in p:
            Name,Age,Gender,Disease=line.strip().split(",")
            if(Name.lower()==user):
                print(f"Name: {Name}, Age: {Age}, Gender: {Gender}, Condition: {Disease}")
                found=True
                break
    if not found:
        print("Patient not found. Invalid name!!")

while True:
    print("__Hospital Management System__")
    print("1. Add Patient")
    print("2. View All Patients")
    print("3. Search Patient by Name")
    print("4. Exit")
    user=int(input("Enter your choice(1-4): "))
    if(user==1):
        add_Patient()
    elif(user==2):
        view_Patients()
    elif(user==3):
        find_Patient()
    elif(user==4):
        print("Exiting")
        break
    else:
        print("Invalid number!! Try again\n")
        