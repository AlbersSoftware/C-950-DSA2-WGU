import csv
from datetime import timedelta, datetime

import Graph
from Truck import Truck
from utils import Utils

from hashtable import print_search_result, get_packages
from hashtable import HashTable
packageHashTable = Utils.loadPackageData('Data/package_file.csv')
# Chris Albers, ID:(009877757), C-950 DSA2- C1 requirement

# C2 requirement- Process and flow of the program is determined here in the main. Each section is labled as you go through the CMI as to whats happening.

def userinterface():
    pass

# prints packages from the hashtable and with their ID, destination and status.
    print("Packages from the hashtable:")
    for i in range(len(packageHashTable.table)):
        package = packageHashTable.search(i + 1)
        if package.deadline != "9:05":
            package.status = "AT_HUB"
        if package.deadline == "9:05":
            package.status = "DELAYED_ON_FLIGHT"
        if package:
            print("Package ID: {}, Destination: {}, Status {}".format(package.ID, package.destination, package.status))




            # set the initial datetime for each truck.
    truck1 = Truck(truck_id=1, capacity=16, startTime=datetime(2023, 1, 1, 8, 0, 0))
    truck2 = Truck(truck_id=2, capacity=16, startTime=datetime(2023, 1, 1, 9, 5, 0))
    truck3 = Truck(truck_id=3, capacity=16, startTime=datetime(2023, 1, 1, 10, 0, 0))

    # create a list of all packages
    all_packages = packageHashTable.get_all_values()





    #while truck1.finish_time is None:
        #truck3.start_time = truck1.finish_time


    # print the packages on each truck indicating they start unloaded.
    print("Truck 1 packages: Not loaded yet")
    for package in truck1.truck_packages:
        print(package)

    print("\nTruck 2 packages: Not loaded yet")
    for package in truck2.truck_packages:
        print(package)

    print("\nTruck 3 packages: Not loaded yet")
    for package in truck3.truck_packages:
        print(package)

    # main menu with options to either load packages from the hashtable or to look up individual packages.
    main_menu = input("----MAIN MENU----\n"
                      "[1] View final results and give a specific time to see if packages are at hub, en route or delievered \n"
                      "[2] Lookup individual package status \n"
                      
                      "(enter anything else to exit) \n")

    # exit the program on bad input
    if main_menu != "1" and main_menu != "2":
        print("You didn't enter a valid menu option! Press [1] to load trucks and [2] to look up packages. Please try again.")
        SystemExit

    if main_menu == "1":
        # load trucks
        truck1.putPackageInDeliveryDict(all_packages)
        truck1.load_packages(all_packages, -1)
        truck1.route = Graph.greedy_path_algorithm(truck1.route, "4001 South 700 East")
        Utils.deliver_packages(truck1, 9, 25, 0, 8, 0, 0)
        Utils.clearDeliveredRoute(truck1)
        truck2.putPackageInDeliveryDict(all_packages)
        truck2.load_packages(all_packages, -1)
        truck2.route = Graph.greedy_path_algorithm(truck2.route, "4001 South 700 East")
        Utils.deliver_packages(truck2, 10, 25, 0, 8, 0, 0)
        Utils.clearDeliveredRoute(truck2)
        truck2.load_packages(all_packages, -2)
        truck2.route = Graph.greedy_path_algorithm(truck2.route, "4001 South 700 East")
        Utils.deliver_packages(truck2, 11, 30, 0, 8, 0, 0)
        Utils.clearDeliveredRoute(truck2)
        truck1.load_packages(all_packages, 1)
        truck1.load_packages(all_packages, 2)
        truck2.load_packages(all_packages, 1)
        # fix address

        for package in truck2.truck_packages:
            if package.ID == 9:
                truck2.route.remove(package.destination)
                package.destination = "410 S State St"
                package.city = "Salt Lake City"
                package.state = "UT"
                package.zip = "84111"
                package.notes = "Fixed the address"
                truck2.route.append(package.destination)
                break

        truck1.route = Graph.greedy_path_algorithm(truck1.route, truck1.route[0])
        truck2.route = Graph.greedy_path_algorithm(truck2.route, truck2.route[0])
        truck3.route = Graph.greedy_path_algorithm(truck3.route, truck3.route[0])
        Utils.deliver_packages(truck1, 10, 30, 0, 8, 0, 0)
        Utils.clearDeliveredRoute(truck1)
        truck1.route = Graph.greedy_path_algorithm(truck1.route, truck1.route[0])
        Utils.deliver_packages(truck2, 12, 30, 0, 9, 5, 0)
        Utils.clearDeliveredRoute(truck2)
        truck2.route = Graph.greedy_path_algorithm(truck2.route, truck2.route[0])

        if truck1.isInHub:
            truck1_current_time = truck1.finish_time
            truck3.start_time = datetime(2023, 1, 1, truck1_current_time.hour, truck1_current_time.minute,
                                         truck1_current_time.second)
            truck3.putPackageInDeliveryDict(all_packages)
            truck3.load_packages(all_packages, -1)
            truck3.route = Graph.greedy_path_algorithm(truck3.route, "4001 South 700 East")
            Utils.deliver_packages(truck3, 11, 30, 0, 9, 50, 0)
            Utils.clearDeliveredRoute(truck3)
            truck3.putPackageInDeliveryDict(all_packages)
            truck3.load_packages(all_packages, 1)

            truck3.route = Graph.greedy_path_algorithm(truck3.route, truck3.route[0])
            Utils.deliver_packages(truck3, 12, 25, 0, 9, 5, 0)
            Utils.clearDeliveredRoute(truck3)
            truck3.route = Graph.greedy_path_algorithm(truck3.route, truck3.route[0])

        # final output
        if len(truck1.route) > 0:
            Utils.deliver_packages(truck1, 17, 25, 0, 8, 0, 0)
            Utils.clearDeliveredRoute(truck1)
            if len(truck1.route) > 0:
                truck1.route = Graph.greedy_path_algorithm(truck1.route, truck1.route[0])

        if len(truck2.route) > 0:
            Utils.deliver_packages(truck2, 17, 25, 0, 8, 0, 0)
            Utils.clearDeliveredRoute(truck2)
            if len(truck2.route) > 0:
                truck2.route = Graph.greedy_path_algorithm(truck2.route, truck2.route[0])

        if len(truck3.route) > 0:
            Utils.deliver_packages(truck3, 17, 25, 0, truck3.start_time.hour, truck3.start_time.minute,
                                   truck3.start_time.second)
            Utils.clearDeliveredRoute(truck3)
            if len(truck3.route) > 0:
                truck3.route = Graph.greedy_path_algorithm(truck3.route, truck3.route[0])

        Utils.see_package_status(truck1, 13, 12, 0, 8, 0, 0)
        Utils.see_package_status(truck2, 13, 12, 0, 8, 0, 0)
        Utils.see_package_status(truck3, 17, 12, 0, 8, 0, 0)
        truck1_miles = truck1.traveled_miles()
        truck2_miles = truck2.traveled_miles()
        truck3_miles = truck3.traveled_miles()
        total = truck1_miles + truck2_miles + truck3_miles
        print("Truck 1: ", round(truck1_miles, 2), "+ Truck 2: ", round(truck2_miles, 2),
              "+ Truck 3: ", round(truck3_miles, 2), " TOTAL =", round(total, 2), "miles")
        print("All trucks have returned to the hub by", truck2.finish_time.time())
       # look up package by ID and time
        user_time = input(
            "Please enter a time to check the status of package(s). Use the following format, HH:MM:SS: ")
        user_time_arr = user_time.split(":")
        convert_time = datetime(2023, 1, 1, int(user_time_arr[0]), int(user_time_arr[1]), int(user_time_arr[2]),
                                tzinfo=None)
        for package in truck2.truck_packages:
            if package.ID == 9 and int(user_time_arr[0]) < 10 or (int(user_time_arr[0]) == 10 and int(user_time_arr[1]) < 20):
                #truck2.route.insert(package.destination)
                package.destination = "300 State St"
                package.city = "Salt Lake City"
                package.state = "UT"
                package.zip = "84103"
                package.notes = "Wrong address listed"
                truck2.route.append(package.destination)
                break

        Utils.see_package_status(truck1, convert_time.hour, convert_time.minute, convert_time.second, 8, 0, 0)
        Utils.see_package_status(truck2, convert_time.hour, convert_time.minute, convert_time.second, 8, 0, 0)
        Utils.see_package_status(truck3, convert_time.hour, convert_time.minute, convert_time.second, 8, 0, 0)
        print("\n*****IN ORDER BY ID*****\n")
        for i in range(len(packageHashTable.table)):
            package = packageHashTable.search(i + 1)

            hour = int(user_time_arr[0])
            minute = int(user_time_arr[1])
            second = int(user_time_arr[2])



            if package:

                print("Package ID: {}, Destination: {}, Status {}".format(package.ID, package.destination,package.status))

        SystemExit

    # [1] load the trucks, and start the simulation
    # load the packages onto the trucks, call to graph starting point and greedy path, deliver packages and clear packages that have been delivered from the route.





    # Menu option #2 lookup packages by giving a time and an ID
    if main_menu == "2":


        checker = "1"
        while checker == "1":

            user_time = input(
                "Please enter a time to check the status of package(s). Use the following format, HH:MM:SS: ")
            user_time_arr = user_time.split(":")
            convert_time = datetime(2023, 1, 1, int(user_time_arr[0]), int(user_time_arr[1]), int(user_time_arr[2]), tzinfo=None)
            #load trucks
            truck1.putPackageInDeliveryDict(all_packages)
            truck1.load_packages(all_packages, -1)
            truck1.route = Graph.greedy_path_algorithm(truck1.route, "4001 South 700 East")
            Utils.deliver_packages(truck1, 9, 25, 0, 8, 0, 0)
            Utils.clearDeliveredRoute(truck1)
            truck2.putPackageInDeliveryDict(all_packages)
            truck2.load_packages(all_packages, -1)
            truck2.route = Graph.greedy_path_algorithm(truck2.route, "4001 South 700 East")
            Utils.deliver_packages(truck2, 10, 25, 0, 8, 0, 0)
            Utils.clearDeliveredRoute(truck2)
            truck2.load_packages(all_packages, -2)
            truck2.route = Graph.greedy_path_algorithm(truck2.route, "4001 South 700 East")
            Utils.deliver_packages(truck2, 11, 30, 0, 8, 0, 0)
            Utils.clearDeliveredRoute(truck2)
            truck1.load_packages(all_packages, 1)
            truck1.load_packages(all_packages, 2)
            truck2.load_packages(all_packages, 1)
            # fix address
            for package in truck2.truck_packages:
                if package.ID == 9 and (int(user_time_arr[0]) > 10 or (int(user_time_arr[0]) == 10 and int(user_time_arr[1]) >= 20)):
                    truck2.route.remove(package.destination)
                    package.destination = "410 S State St"
                    package.city = "Salt Lake City"
                    package.state = "UT"
                    package.zip = "84111"
                    package.notes = "Fixed the address"
                    truck2.route.append(package.destination)
                    break

            truck1.route = Graph.greedy_path_algorithm(truck1.route, truck1.route[0])
            truck2.route = Graph.greedy_path_algorithm(truck2.route, truck2.route[0])
            truck3.route = Graph.greedy_path_algorithm(truck3.route, truck3.route[0])
            Utils.deliver_packages(truck1, 10, 30, 0, 8, 0, 0)
            Utils.clearDeliveredRoute(truck1)
            truck1.route = Graph.greedy_path_algorithm(truck1.route, truck1.route[0])
            Utils.deliver_packages(truck2, 12, 30, 0, 9, 5, 0)
            Utils.clearDeliveredRoute(truck2)
            truck2.route = Graph.greedy_path_algorithm(truck2.route, truck2.route[0])

            if truck1.isInHub:
                truck1_current_time = truck1.finish_time
                truck3.start_time = datetime(2023, 1, 1, truck1_current_time.hour, truck1_current_time.minute,
                                             truck1_current_time.second)
                truck3.putPackageInDeliveryDict(all_packages)
                truck3.load_packages(all_packages, -1)
                truck3.route = Graph.greedy_path_algorithm(truck3.route, "4001 South 700 East")
                Utils.deliver_packages(truck3, 11, 30, 0, 9, 50, 0)
                Utils.clearDeliveredRoute(truck3)
                truck3.putPackageInDeliveryDict(all_packages)
                truck3.load_packages(all_packages, 1)

                truck3.route = Graph.greedy_path_algorithm(truck3.route, truck3.route[0])
                Utils.deliver_packages(truck3, 12, 25, 0, 9, 5, 0)
                Utils.clearDeliveredRoute(truck3)
                truck3.route = Graph.greedy_path_algorithm(truck3.route, truck3.route[0])

            if len(truck1.route) > 0:
                Utils.deliver_packages(truck1, 17, 25, 0, 8, 0, 0)
                Utils.clearDeliveredRoute(truck1)
                if len(truck1.route) > 0:
                    truck1.route = Graph.greedy_path_algorithm(truck1.route, truck1.route[0])

            if len(truck2.route) > 0:
                Utils.deliver_packages(truck2, 17, 25, 0, 8, 0, 0)
                Utils.clearDeliveredRoute(truck2)
                if len(truck2.route) > 0:
                    truck2.route = Graph.greedy_path_algorithm(truck2.route, truck2.route[0])

            if len(truck3.route) > 0:
                Utils.deliver_packages(truck3, 17, 25, 0, truck3.start_time.hour, truck3.start_time.minute,
                                       truck3.start_time.second)
                Utils.clearDeliveredRoute(truck3)
                if len(truck3.route) > 0:
                    truck3.route = Graph.greedy_path_algorithm(truck3.route, truck3.route[0])



            Utils.see_package_status(truck1, convert_time.hour, convert_time.minute, convert_time.second, 8, 0,0)
            Utils.see_package_status(truck2, convert_time.hour, convert_time.minute, convert_time.second, 8, 0,0)
            Utils.see_package_status(truck3, convert_time.hour, convert_time.minute, convert_time.second, 8, 0,0)





            if len(user_time_arr)!= 3:
                print("bad input")
                if user_time_arr != int:
                    print("bad input 2")




            user_search_string = input("Enter the package ID# you want to search: ")
            try:
                user_search_int = int(user_search_string)
                print_search_result(packageHashTable, user_search_int)
                print("The search is over and the system is closing, Good Bye!")
                raise SystemExit
            except ValueError:
                print("You didn't enter a valid number for the ID")


        userinterface()


# program entry
print("WGU Delivery System: The time is 7:59AM")
userinterface()




