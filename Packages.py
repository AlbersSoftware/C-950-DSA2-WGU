import csv
from datetime import datetime
from typing import List
import hashtable




class Package:
    def __init__(self, ID, destination, city, state, Zip, deadline, weight, notes, status="Loaded"):
        super().__init__()
        self.ID = ID
        self.destination = destination
        self.city = city
        self.state = state
        self.Zip = Zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status

        # Add delivery time

    def __str__(self):
        return f"{self.ID}, {self.destination}, {self.city}, {self.state}, {self.Zip}, {self.deadline}, {self.weight}, {self.notes}, {self.status}"

    def load_to_truck(self, truck_id):
        self.status = f"On Truck {truck_id}"
def loadPackageData(file):
    print("Loading package data...")
    packageHashTable = hashtable.HashTable()
    with open(file) as packages:
        packageData = csv.reader(packages, delimiter=',')
        #next(packageData)
        for row in packageData:
            package = list(row)
            packageID = int(package[0])
            packageDestination = package[1]
            packageCity = package[2]
            packageState = package[3]
            packageZip = package[4]
            packageDeadline = package[5]
            packageWeight = package[6]
            packageNotes = package[7]
            packageStatus = "Loaded"

            p = Package(packageID, packageDestination, packageCity, packageState,
                        packageZip, packageDeadline, packageWeight, packageNotes, packageStatus)

            packageHashTable.insert(packageID, p)


        return packageHashTable


