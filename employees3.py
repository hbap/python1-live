import csv

from pprint import pprint

with open("employees.csv", "r") as file:
    employees = {}
    reader = csv.DictReader(file)
    i = 1
    for row in reader:
        employee = row
        employee["Id"] = i
        Name = employee["FirstName"] + " " + employee["LastName"]
        employees[Name] = employee
        i = i + 1

    print("Id,ManagerId,LastName,FirstName")
    for name, employee in employees.items():
        Manager = employee["Manager"]
        if Manager:
            ManagerId = employees[Manager]["Id"]
        else:
            ManagerId = ""
        print(employee["Id"], ManagerId, employee["LastName"], employee["FirstName"], sep=",")
