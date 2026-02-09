import csv
from packageClass import Package
from hashTable import HashTable

#path to the CSV file holding package information
csv_package_file = "wgupsPackageFile.csv"


def load_packages(csv_package_file):
    """
    Loads the package info from a csv file into our custom hash table.

    :param csv_package_file: Filepath to the csv package file.

    First we create an empty hash table and store packages by the package id.
    We then open the CSV file and create a CSV reader making sure to skip the
    first row. After that we build a package object from the row fields. Insert the
    package data into the hash table using the package id ad the key. Once all package
    data is inserted in the hash table we return it.
    :return: We return a hashtable where each key is a package id and each value is a
    package object.
    """
    #Initilaizes an empty hash table to store all package objects
    package_table = HashTable()

    #Opens the CSV file for reading, the encoding handles leading char causing issues.
    with open (csv_package_file, mode='r', newline='', encoding='utf-8-sig') as csvfile:
        csv_package_reader = csv.reader(csvfile, delimiter=',')

        #This will skip the header row
        next(csv_package_reader)
        #Each row in the CSV reps a single package
        for row in csv_package_reader:
            #Creates a Package object using the CSV columns
            package_data = Package(
                package_id=int(row[0]),
                address=row[1],
                city=row[2],
                state=row[3],
                zip_code=row[4],
                delivery_deadline=row[5],
                weight=row[6],
                #Handles for cases when the package has no note data to it
                note=row[7] if len(row) > 7 else "",
            )

            #Inserts the package info into the hash table using its ID as the key
            package_table.insert(package_data.package_id, package_data)

    return package_table





