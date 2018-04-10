import csv

with open("employees.csv", "r") as file:
    print("Id,Manager,LastName,FirstName")
    reader = csv.DictReader(file)
    i = 1
    for row in reader:
        print(i, row["Manager"], row["LastName"], row["FirstName"], sep=",")
        i = i + 1
