import csv
employees = [["Name", "Age", "Job"],
             ["Kartik", 22, "Student"],
             ["Kanchika", 23, "Engineer"],
             ["Ashmit", 24, "Student"],
             ["Maahi", 22, "Designer"]]
file_path = "output.csv"
try:
    with open(file=file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(
            f"File has been updated and text has been addded in {file_path}")
except FileExistsError:
    print(f"csv file : {file_path} already exists")
