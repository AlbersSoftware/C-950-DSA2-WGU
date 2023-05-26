from typing import List, Any

from Graph import graph, Graph


# The truck class handles the truck objects. Specific package order to load onto the trucks, add/remove from route, time and miles traveled.

class Truck:


# initialize packages on the truck, route, empty list for completed route, delivery start and end time and start and location, capacity, mileage, speed, and if the truck is back to the hub.
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



    # Put package on truck and append the destination to the route.
    def insert(self, package):
        self.truck_packages.append(package)
        self.route.append(package.destination)
    # Put package in delivery dictionary
    def putPackageInDeliveryDict(self, package_list):
        graph.put_packages_in_delivery_dict(package_list)
    # specify the order in which the packages go onto the trucks and set priority for packages 15,16,25,26,6,34,5, and 37.
    def load_packages(self, package_list, priority):
        for package in package_list:
            if priority == -1 and self.truck_id == 1 and (package.ID == 15 or package.ID == 16):
                self.insert(package)
                package.load_to_truck(self.truck_id)
            elif priority == -1 and self.truck_id == 2 and (package.ID == 25 or package.ID == 26):
                self.insert(package)
                package.load_to_truck(self.truck_id)
            elif (priority == 1 and package.deadline == "EOD" and self.truck_id == 1) or package.status.startswith("DELIVERED AT")\
                    or package.status.startswith("On Truck"):
                continue
            elif priority == -2 and self.truck_id == 2 and (package.ID == 6 or package.ID == 34):
                self.insert(package)
                package.load_to_truck(self.truck_id)
            elif priority == -1 and self.truck_id == 3 and (package.ID == 5 or package.ID == 37):
                self.insert(package)
                package.load_to_truck(self.truck_id)
            if priority == -1 or priority == -2:
                continue
            if self.truck_id == 1 and (package.ID == 1 or package.ID == 13 or package.ID == 14
                                        or package.ID == 20 or package.ID == 29 or package.ID == 19
                                          or package.ID == 31 or package.ID == 30  or package.ID == 40
                                        ):
                self.insert(package)
                package.load_to_truck(self.truck_id)


            elif self.truck_id == 2 and ( package.ID == 9 or package.ID == 3 or package.ID == 18 or package.ID == 25
                                          or package.ID == 27 or package.ID == 28 or package.ID == 32
                                          or package.ID == 35 or package.ID == 38  or package.ID == 36  or package.ID == 39 ):
                self.insert(package)
                package.load_to_truck(self.truck_id)



            elif self.truck_id == 3 and (package.ID == 2 or package.ID == 4 or package.ID == 12
                                         or package.ID == 7  or package.ID == 8 or package.ID == 10 or package.ID == 11
                                         or package.ID == 17   or package.ID == 21 or package.ID == 22
                                         or package.ID == 24 or package.ID == 23 or package.ID == 33):
                self.insert(package)
                package.load_to_truck(self.truck_id)
                #insert package and load to truck based on ID
                # When packages are on the trucks, insert in delivery dictionary's graph instance



        # remove package from the truck via subscript
    def remove(self, package):
        self.truck_packages.remove(package)
        self.route.remove(package[1])


# initialize the start time
    def start_delivery(self, time):
        self.start_time = time


# update as deliveries are handled, return the current time.
    def current_time(self, time):
        self.current_time = time
        return time





    # Gets the traveled miles for each truck using the edge weight's in the graph
    def traveled_miles(self):
        edge_weight_list = graph.edge_weights
        miles = 0
        for i in range(0, len(self.completedroute) - 1):
            if self.completedroute[i] == self.completedroute[i + 1]:
                continue  # skip this iteration if the same location appears twice in a row
            miles = miles + edge_weight_list[self.completedroute[i], self.completedroute[i + 1]]
        return miles


