import csv
from tabulate import tabulate

data_to_write = [
    ["Name", "Age", "Country"],
    ["Alice", "25", "USA"],
    ["Bob", "30", "Canada"],
    ["Amine", "16", "Tunisia"],
    ["Jeffrey", "24", "USA"],
]

data_to_write_dict = [
    {"Name": "Alice", "Age": "25", "Country": "USA"},
    {"Name": "Bob", "Age": "30", "Country": "Canada"},
]
fieldnames = ["Name", "Age", "Country"]


def write(data):
    with open("output.csv", "w") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)


def read(path, delimeter=","):
    with open(path, "r") as file:
        csv_reader = csv.reader(file, delimiter=delimeter)
        print(tabulate(csv_reader, headers="firstrow", tablefmt="grid"))


def read_dict(path, delimeter=","):
    with open(path, "r") as file:
        csv_dict_reader = csv.DictReader(file, delimiter=delimeter)
        # for row in csv_dict_reader:
        #     print(row['Name'], row['Age'], row['Country'])
        print(tabulate(csv_dict_reader, tablefmt="grid"))


def write_dict(path, data, fieldnames, delimeter=","):
    with open(path, "w") as file:
        csv_dict_writer = csv.DictWriter(
            file, fieldnames=fieldnames, delimiter=delimeter
        )
        csv_dict_writer.writeheader()
        csv_dict_writer.writerows(data)
