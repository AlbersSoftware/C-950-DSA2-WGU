import csv

from Truck import truck1

distances = list(csv.reader(open('Data/distance.csv')))
addresses = list(csv.reader(open('Data/address_file.csv')))





# Function that takes a list of packages and returns the corresponding destinations addresses

def getTruckDestinations(truckPackages, truck):
    truckDestinations = []
    for package in range(len(truckPackages)):
        truckDestinations.append(truck.packages[package].destination)
    return truckDestinations


# List of all addresses
allAddresses = []
for address in range(len(addresses)):
    allAddresses.append(addresses[address][1])


# Function that takes a matrix and list of indexes(i) and returns corresponding columns.
def getColumn(matrix, i):
    return [row[i] for row in matrix]

# Returns list of column indexes given a list  of packages


def getDistanceCols(truckPackages, truck):
    destinations = getTruckDestinations(truckPackages, truck)
    destinationIndexes = []
    for destination in destinations:
        if destination in allAddresses:
            destinationIndexes.append(allAddresses.index(destination))
    return destinationIndexes


# Function that takes in a list of packages and returns the corresponding distance data.


def getPackageDistances(truckPackages, truck):
    destinationIndexes = getDistanceCols(truckPackages, truck)
    truckDistances = []
    for i in destinationIndexes:
        truckDistances.append(getColumn(distances, i))
    return truckDistances


truckDistances = getPackageDistances(truck1.packages, truck1)
# print(truckDistances)


def getNextDestination(currentLocation):
    currentLocation = 0
    indexes = getDistanceCols(truck1.packages, truck1)
    for i in indexes:
        currentCol = getColumn(distances, 0)
        print(currentCol[i])
        m = float(min(n for n in currentCol if n != '0'))
    print(m)


getNextDestination(getTruckDestinations(truck1.packages, truck1))