import csv
from typing import List
from Packages import Package

# the HashTable class provides efficient key/value storage and retrieval and satisfies section: D.
class HashTable:
    # initialize the hash table and its size

    def __init__(self, table_size=10):
        self.table_size = table_size
        self.hash_table = [None] * table_size
        self.table = []
        for i in range(table_size):
            self.table.append([])
# add new element to table and append it making it partly self adjusting
    def addnewelement(self):
        self.table_size += 1
        self.table.append([])
    #checks if current table size is smaller than ID and if it is it calls add new element to increase size.
    # converts string to int for package ID, calculates the bucket index for the given key using the modulo operator to determine where the package is being stored.
    # update the bucket and assign status based on deadline, uses linear probing for collision handling with the % operator.
    #O(n) space where n is the number of packages and constant time O(1) for each insertion.
    def insert(self, key, package):
        if self.table_size < package.ID:
            self.addnewelement()
        package.ID = int(package.ID)
        bucket = key % (len(self.table)+1)-1
        self.table[bucket].append(package)
        if bucket >= len(self.hash_table):
            self.hash_table.append(package)
        else:
            self.hash_table[bucket] = package
        if package.deadline != "9:05":
            package.status = "AT_HUB"  # Adds delivery status for all packages that are not late to the hub
        if package.deadline == "9:05":
            package.status = "DELAYED_ON_FLIGHT"  # Packages that are late to the hub get this delivery status
# retrieve all packages stored, O(n) space and time,where n is the number of packages
    def get_all_values(self) -> List[Package]:
        all_values = []
        for bucket in self.table:
            for package in bucket:
                all_values.append(package)
        return all_values
    # find package based on given key. O(1) space and O(1) to O(n) time depending on collisions.
    # Increments index by 1 if collision occurs until it finds an empty slot(linear probing).
    def search(self, key):
            hash_index = key % (self.table_size+1)-1
            while self.hash_table[hash_index] is not None:
                if self.hash_table[hash_index].ID == key:  # access the ID attribute of the Package object
                    return self.hash_table[hash_index]
                hash_index = (hash_index + 1) % self.table_size
            return None
# directly accesses the specific bucket and performs a linear search within that bucket to find and remove the package.
    # It is predetermined making space O(1) and due to bucket size being small its probably closer to O(1) as well.
    def remove(self, key):
        # Get the bucket list where this key/ID should be found
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Look inside the bucket and remove package for the matching key/ID, if found.
        for package in bucket_list:
            if package[0] == key:
                bucket_list.remove(key)
# reads data from csv file and populates package objects, O(n) space and time, n being packages in the csv file and packages read from the csv file.
def get_packages(filename):
     hash_pkgs = HashTable()
     with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                print(row)
                package = Package(*row, "Loaded")
                hash_pkgs.insert(package.ID, package)
            return hash_pkgs



# prints the search result based on ID. O(1) space and time.
def print_search_result(package_hashtable, id):
    print(package_hashtable.search(id))




