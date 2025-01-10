import sys
import csv
array = []
newArray = []
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-4:] != ".csv":
    sys.exit("Not a CSV file")
else:
    try:
        with open(sys.argv[1]) as f:
            reader = csv.DictReader(f)
            for row in reader:
                array.append({"name": row["name"], "house": row["house"]})
    except:
        sys.exit("File does not exist")
    else:
        for i in range(len(array)):
            last, first = array[i]["name"].split(',')
            first = first.strip()
            house = array[i]["house"]
            newArray.append({"first": first, "last": last, "house": house})
        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writerow({"first": "first", "last": "last", "house": "house"})
            for j in range (len(newArray)):
                writer.writerow({"first": newArray[j]["first"], "last": newArray[j]["last"], "house": newArray[j]["house"]})
