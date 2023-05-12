from typing import List, Any

from Graph import graph, Graph


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
        self.hub_location = "4001 South 700 East"
        self.isInHub = True



    # Put package on truck
    def insert(self, package):
        self.truck_packages.append(package)  # puts the package onto the truck
        self.route.append(package.destination)

    def putPackageInDeliveryDict(self, package_list):
        graph.put_packages_in_delivery_dict(package_list)
    def load_packages(self, package_list, priority):
        for package in package_list:
            if priority == -1 and self.truck_id == 1 and (package.ID == 15 or package.ID == 16):
                self.insert(package)
                package.load_to_truck(self.truck_id)
                break
            elif priority == -1 and (self.truck_id == 2 and package.ID == 25 ):
                self.insert(package)
                package.load_to_truck(self.truck_id)
                break
            elif (priority == 1 and package.deadline == "EOD") or package.status.startswith("DELIVERED AT")\
                    or package.status.startswith("On Truck"):
                continue
            elif priority == -1:
                continue
            if self.truck_id == 1 and (package.ID == 19 or package.ID == 13 or package.ID == 14
                                        or package.ID == 20    or package.ID == 39
                                         or package.ID == 34 or package.ID == 31 or package.ID == 40
                                        or package.ID == 4 or package.ID == 21 or package.ID == 29  ):
                self.insert(package)
                package.load_to_truck(self.truck_id)
                # After loading packages onto the truck, put them in the delivery dictionary in the graph instance
                #print(f"Package {package.ID} loaded onto Truck {self.truck_id}")
            elif self.truck_id == 2 and (package.ID == 1 or package.ID == 3 or package.ID == 18 or package.ID == 17
                                          or package.ID == 38
                                         or package.ID == 25    or package.ID == 30
                                         or package.ID == 8 or package.ID == 37 or package.ID == 36  or package.ID == 6):
                self.insert(package)
                package.load_to_truck(self.truck_id)
                # After loading packages onto the truck, put them in the delivery dictionary in the graph instance

                #print(f"Package {package.ID} loaded onto Truck {self.truck_id}")
            elif self.truck_id == 3 and (package.ID == 23 or package.ID == 28 or package.ID == 32 or package.ID == 27
                                         or package.ID == 35  or package.ID == 24 or package.ID == 9
                                         or package.ID == 33  or package.ID == 28 or package.ID == 5   or package.ID == 11 or package.ID == 12 or package.ID == 22 or package.ID == 26 or package.ID == 10 or package.ID == 7  or package.ID == 2):
                self.insert(package)
                package.load_to_truck(self.truck_id)
                # After loading packages onto the truck, put them in the delivery dictionary in the graph instance
                #graph.put_packages_in_delivery_dict(package_list)
                #print(f"Package {package.ID} loaded onto Truck {self.truck_id}")
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


