import os

import csv

file_to_load = os.path.join("election_results.csv")
file_to_save = os.path.join("Analysis" , "election_results.txt")


with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)

    