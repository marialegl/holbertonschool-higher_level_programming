#!/usr/bin/python3
"""Reading data from one format (CSV) and
converting it into another format (JSON) using serialization techniques.
"""

import csv
import json


def convert_csv_to_json(csv_file):
    data = []

    try:
        with open(csv_file, encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)

            for rows in csvReader:
                data.append(rows)

        with open("data.json", 'w', encoding="utf-8") as jsonFile:
            json.dump(data, jsonFile, indent=4)
        return (True)

    except FileNotFoundError:
        print(f"Error: The file {csv_file} was not found.")
        return (False)
