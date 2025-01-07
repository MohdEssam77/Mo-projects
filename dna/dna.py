import csv
import sys


def main():
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    Database = []
    with open(sys.argv[1], "r") as file:
        lines = csv.DictReader(file)
        for i in lines:
            Database.append(i)

    f = open(sys.argv[2], "r")
    dna = f.readline().strip()

    subsequences = list(Database[0].keys())[1:]
    results = {}
    for j in subsequences:
        results[j] = longest_match(dna, j)

    for k in Database:
        match = 0
        for j in subsequences:
            if int(k[j]) == results[j]:
                match += 1
        if match == len(subsequences):
            print(k["name"])
            return
    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    for i in range(sequence_length):

        count = 0

        
        while True:

            
            start = i + count * subsequence_length
            end = start + subsequence_length

            if sequence[start:end] == subsequence:
                count += 1

            else:
                break

        longest_run = max(longest_run, count)

    return longest_run


main()
