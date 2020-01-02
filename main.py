import csv

path = "/Users/poquito/Desktop/python-csv/"

with open(f"{path}names.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open(f"{path}new_names.csv", "w") as new_file:
        fd = ["first_name", "last_name", "email"]
        de = "\t"
        csv_writer = csv.DictWriter(new_file, fieldnames=fd, delimiter=de)

        # This writes our header (first_name, last_name, email)
        csv_writer.writeheader()

        for line in csv_reader:
            # this would delete a column
            # del line["email"]
            csv_writer.writerow(line)
