import csv

def file():
    with open("pythonSQL./orders.csv", "r") as file:
        reader = csv.DictReader(file)
        counts ={}
        for row in reader:
            department = row["department"]
            if department in counts:
                counts[department] += 1
            else:
                counts[department] = 1
            
    for department in sorted(counts, key=counts.get,  reverse=True): 
        print(F"{department}: {counts[department]}")    

        
file()