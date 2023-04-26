import csv
from typing import List
from Packages import Package



class HashTable:
    # Constructor to initialize the hash table
    # O(m) complexity, where m is the number of buckets in the hash table
    def __init__(self, table_size=10):
        self.table_size = table_size
        self.hash_table = [None] * table_size
        self.table = []
        for i in range(table_size):
            self.table.append([])

    def addnewelement(self):
        self.table_size += 1
        self.table.append([])

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

    def get_all_values(self) -> List[Package]:
        all_values = []
        for bucket in self.table:
            for package in bucket:
                all_values.append(package)
        return all_values
    def search(self, key):
            hash_index = key % (self.table_size+1)-1
            while self.hash_table[hash_index] is not None:
                if self.hash_table[hash_index].ID == key:  # access the ID attribute of the Package object
                    return self.hash_table[hash_index]
                hash_index = (hash_index + 1) % self.table_size
            return None

    def remove(self, key):
        # Get the bucket list where this key/ID should be found
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Look inside the bucket and remove package for the matching key/ID, if found.
        for package in bucket_list:
            if package[0] == key:
                bucket_list.remove(key)

def get_packages(filename):
     hash_pkgs = HashTable()
     with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                print(row)
                package = Package(*row, "Loaded")
                hash_pkgs.insert(package.ID, package)
            return hash_pkgs




def print_search_result(package_hashtable, id):
    print(package_hashtable.search(id))




