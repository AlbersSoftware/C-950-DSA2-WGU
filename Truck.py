from typing import List, Any

from Graph import graph, Graph
from Graph import greedy_path_algorithm
from datetime import timedelta, datetime
from hashtable import HashTable
import csv
from Packages import Package

# The Truck Class assists in creating truck objects which will be loaded with packages

class Truck:


# Constructor to initialize packages on the truck, route, delivery start time, and mileage
    def __init__(self, truck_id, capacity, startTime): # , type, value
        self.truck_packages = []
        self.route = ["4001 South 700 East"]
        self.completedroute = []
        self.start_time = startTime
        self.current_time = None
        self.finish_time = None
        self.speed = 0.3  # 18mph is equivalent to 0.3 miles / minute
        self.truck_id = truck_id
        self.capacity = capacity
        #self.prioritytype = type
        #self.priorityvalue = value


    # Put package on truck
    def insert(self, package):
        self.truck_packages.append(package)  # puts the package onto the truck
        self.route.append(package.destination)

    def putPackageInDeliveryDict(self, package_list):
        graph.put_packages_in_delivery_dict(package_list)
    def load_packages(self, package_list, priority):
        for package in package_list:
            if (priority == 1 and package.deadline == "EOD") or package.status.startswith("DELIVERED AT")\
                    or package.status.startswith("On Truck"):
                continue
            if self.truck_id == 1 and (package.ID == 19 or package.ID == 13 or package.ID == 14
                                       or package.ID == 16 or package.ID == 20 or package.ID == 11 or package.ID == 12
                                       or package.ID == 5 or package.ID == 7 or package.ID == 8 or package.ID == 37
                                       or package.ID == 10 or package.ID == 30 or package.ID == 34):
                self.insert(package)
                package.load_to_truck(self.truck_id)
                # After loading packages onto the truck, put them in the delivery dictionary in the graph instance
                print(f"Package {package.ID} loaded onto Truck {self.truck_id}")
            elif self.truck_id == 2 and (package.ID == 1 or package.ID == 3 or package.ID == 18 or package.ID == 36
                                         or package.ID == 2  or package.ID == 17 or package.ID == 21
                                         or package.ID == 22 or package.ID == 23 or package.ID == 24 or package.ID == 26
                                         or package.ID == 27 or package.ID == 28 or package.ID == 29 or package.ID == 15 ):
                self.insert(package)
                package.load_to_truck(self.truck_id)
                # After loading packages onto the truck, put them in the delivery dictionary in the graph instance
                #graph.put_packages_in_delivery_dict(package_list)
                print(f"Package {package.ID} loaded onto Truck {self.truck_id}")
            elif self.truck_id == 3 and (package.ID == 6 or package.ID == 25 or package.ID == 28 or package.ID == 32
                                         or package.ID == 35 or package.ID == 38 or package.ID == 39
                                         or package.ID == 40 or package.ID == 33 or package.ID == 31 or package.ID == 9):
                self.insert(package)
                package.load_to_truck(self.truck_id)
                # After loading packages onto the truck, put them in the delivery dictionary in the graph instance
                #graph.put_packages_in_delivery_dict(package_list)
                print(f"Package {package.ID} loaded onto Truck {self.truck_id}")
                #elif self.truck_id == 3 and self.truck3_priority and (package.ID == 6)



    def remove(self, package):
        self.truck_packages.remove(package)  # takes the package off the truck
        self.route.remove(package[1])  # removes the address from the route


# Leave the hub and start the delivery route
    def start_delivery(self, time):
        self.start_time = time


# This is updated as deliveries are made
    def current_time(self, time):
        self.current_time = time
        return time



    # Time that the truck finished their deliveries and is back at the hub
    # This will tell truck 3 when to leave (as there are only 2 drivers)
    def returned_to_hub(self, time):
        self.finish_time = time
        return time

    # Gets the miles traveled for an individual truck
    # O(N)
    def miles_traveled(self):
        edge_weight_list = graph.edge_weights
        miles = 0
        for i in range(0, len(self.completedroute) - 1):
            if self.completedroute[i] == self.completedroute[i + 1]:
                continue  # Skip this iteration if the same location appears twice in a row
            miles = miles + edge_weight_list[self.completedroute[i], self.completedroute[i + 1]]
        return miles


# Create truck objects

'''def load_trucks_and_get_best_route():
        all_addresses = []
        delivery_dict = graph.delivery_dict
        # Populates the unvisited_addresses list with the locations from the graph.
        for location in delivery_dict:
            all_addresses.append(location)

    # Priority 1 (see description above)
        for address in all_addresses:
            for package in delivery_dict[address]:
                if package.deadline == "9:00":
                    truck1.insert(package)

    # Priority 2 (see description above)
        for address in all_addresses:
            for package in delivery_dict[address]:
                if package.deadline == "10:30" and package.notes != "" and package.notes != "2" and package.notes != "W" and package.notes != "9:05":
                    truck1.insert(package)
                elif package.deadline == "10:30" and package.notes == "9:05":
                    truck2.insert(package)

    # Priority 3 (see description above)
        for address in all_addresses:
            for package in delivery_dict[address]:
                if package.deadline == "10:30" and package.notes == "":
                    truck1.insert(package)

    # Priority 4 (see description above)
        for address in all_addresses:
            for package in delivery_dict[address]:
                if package.deadline == "17:00" and package.notes == "9:05":
                    truck2.insert(package)
                if package.deadline == "17:00" and package.notes == "W":
                    truck2.insert(package)
                if package.deadline == "17:00" and package.notes == "2":
                    truck2.insert(package)

    # Priority 5 (see description above)
        for address in all_addresses:
            for package in delivery_dict[address]:
                if package.deadline == "17:00" and package.notes == "":
                    if len(truck1.truck_packages) < 16:
                        truck1.insert(package)
                    elif len(truck2.truck_packages) < 16:
                        truck2.insert(package)
                    elif len(truck3.truck_packages) < 16:
                        truck3.insert(package)
                    else:
                        print("package could not be loaded")


# Change the route to make it more efficient
for truck in [truck1, truck2, truck3]:
    truck.route = greedy_path_algorithm(truck.route)

    # Route the trucks back to the hub
    #truck1.route.append("4001 South 700 East")
    #truck2.route.append("4001 South 700 East")
    #truck3.route.append("4001 South 700 East")

    # Results
    print("All truck & package data after loading: ")
    print("Truck 1 has", len(truck1.truck_packages), "packages")
    print("Truck 1 packages:", *truck1.truck_packages, sep="\n")
    print("Truck 2 has", len(truck2.truck_packages), "packages")
    print("Truck 2 packages:", *truck2.truck_packages, sep="\n")
    print("Truck 3 has", len(truck3.truck_packages), "packages")
    print("Truck 3 packages:", *truck3.truck_packages, sep="\n")'''





# Gets the total miles traveled by all trucks
# O(N)


# Assists with stating the time of the package delivery
# O(1)



# This function delivers all the packages to the correct address
# O(N^2)

    # Changes the delivery status to "out for delivery"
# O(N)



    # Allows the user in main.py to view packages' delivery status at certain times
    # O(N^2)
