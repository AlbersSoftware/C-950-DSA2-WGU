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
        if package:
            print("Package ID: {}, Destination: {}, Status {}".format(package.ID, package.destination, package.status))

            #call for get packages and to search packages

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
                      "[1] Load the trucks with packages \n"
                      "[2] Lookup individual package status \n"
                      "(enter anything else to exit) \n")

    # exit the program on bad input
    if main_menu != "1" and main_menu != "2":
        print("You didn't enter a valid menu option! Press [1] to load trucks and [2] to look up packages. Please try again.")
        SystemExit



    # [1] load the trucks, and start the simulation
    # load the packages onto the trucks, call to graph starting point and greedy path, deliver packages and clear packages that have been delivered from the route.
    if main_menu == "1":
        print("The time is now 8:00")
        print("Packages were inserted into the hashtable and loaded onto the trucks.")
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
        truck1.load_packages(all_packages,1)
        truck2.load_packages(all_packages, 1)

        status_1 = input("\nYou can now see package status #1 \n"
                         "[1] To see package status of packages delivered between 8:35 a.m. and 9:25 a.m \n"
                         "(Enter anything else to exit) \n")

        # exit the program on bad input
        if status_1 != "1":
            print("You didn't enter a valid menu option or chose to exit the program. Please try again.")
            SystemExit

        # [1] view package status #1
        if status_1 == "1":
            # see package status 1 between times specified, call to greedy path for each truck if packages are in route, clear route for trucks if delievered.
            truck1.route = Graph.greedy_path_algorithm(truck1.route, truck1.route[0])
            #truck3.route = Graph.greedy_path_algorithm(truck3.route, "3060 Lester St")
            truck2.route = Graph.greedy_path_algorithm(truck2.route, truck2.route[0])
            truck3.route = Graph.greedy_path_algorithm(truck3.route, "4001 South 700 East")

            Utils.deliver_packages(truck1,9, 25, 0,8, 0,0)
            Utils.clearDeliveredRoute(truck1)
            truck1.route = Graph.greedy_path_algorithm(truck1.route, truck1.route[0])
            Utils.deliver_packages(truck2, 9, 25, 0,9, 5,0)
            Utils.clearDeliveredRoute(truck2)
            truck2.load_packages(all_packages, 1)
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
                Utils.deliver_packages(truck3, 12, 25, 0,9, 5,0)
                Utils.clearDeliveredRoute(truck3)
                truck3.route = Graph.greedy_path_algorithm(truck3.route, truck3.route[0])


            Utils.see_package_status(truck1, 9, 25, 0,8,35,0)
            Utils.see_package_status(truck2, 9, 25, 0,8,35,0)
            Utils.see_package_status(truck3, 9, 25, 0,8,35,0)

            truck1.load_packages(all_packages, 2)

            # Fix package #9's address
            print("\nUpdate: The time is now 10:20AM. Package #9 has an address change and must be updated.")
            fix_pkg = input("Would you like to fix this address? Enter 1 for 'YES' or anything else to exit: ")

            # exit the program on bad input
            if fix_pkg != "1":
                print("You didn't enter a valid menu option, or chose to exit the program. Please try again.")
                SystemExit

            # [1] yes, fix the address for package #9. The package is on truck 2 and we will loop until the package is updated.
            # Then call to greedy path for each truck and clear delivered route. If truck 1 has returned truck 3 can start. Print sucessful update of package #9 address.
            if fix_pkg == "1":
                print("Changing package #9 address to 410 S State St., Salt Lake City, UT 84111")
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
                truck3.route = Graph.greedy_path_algorithm(truck3.route,truck3.route[0])
                Utils.deliver_packages(truck1, 10, 30, 0, 8, 0,0)
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

                print("The address has been fixed for package #9")


                # view package status 2
                status_2 = input("\nYou can now see package status #2\n"
                                 "[1] To see package status of packages delivered between 9:35 a.m. and 10:25 a.m \n"
                                 "(Enter anything else to exit)\n")

                # Exit program on bad input
                if status_2 != "1":
                    print("You didn't enter a valid menu option, or chose to exit the program. Please try again.")
                    SystemExit

                if status_2 == "1":
                    # set at hub to false,see package status 2 between times specified, call to greedy path for each truck if packages are in route, clear route for trucks.
                    if truck1.isInHub == False:
                        Utils.deliver_packages(truck1, 13, 12, 0,8, 0,0)
                        Utils.clearDeliveredRoute(truck1)
                        truck1.route = Graph.greedy_path_algorithm(truck1.route, truck1.route[0])

                    if truck2.isInHub == False:
                        Utils.deliver_packages(truck2, 14, 12, 0,9,5,1)
                        Utils.clearDeliveredRoute(truck2)
                        truck2.route = Graph.greedy_path_algorithm(truck2.route, truck2.route[0])
                    #  conditional to check if truck 1 is back to hub to determine truck 3 start time.
                    if truck1.isInHub:
                        truck1_current_time = truck1.finish_time
                        truck3.start_time = datetime(2023, 1, 1, truck1_current_time.hour, truck1_current_time.minute,
                                                     truck1_current_time.second)
                        truck3.putPackageInDeliveryDict(all_packages)
                        truck3.load_packages(all_packages, -1)
                        truck3.route = Graph.greedy_path_algorithm(truck3.route, "4001 South 700 East")
                        Utils.deliver_packages(truck3, 13, 12, 0, 9, 50, 0)
                        Utils.clearDeliveredRoute(truck3)
                        truck3.putPackageInDeliveryDict(all_packages)
                        truck3.load_packages(all_packages, 1)

                        truck3.route = Graph.greedy_path_algorithm(truck3.route, truck3.route[0])
                        Utils.deliver_packages(truck3, 13, 12, 0, 9, 5, 0)
                        Utils.clearDeliveredRoute(truck3)
                        truck3.route = Graph.greedy_path_algorithm(truck3.route, truck3.route[0])


                    Utils.see_package_status(truck1, 10, 25, 0,9,35,1)
                    Utils.see_package_status(truck2, 10, 25, 0,9,35,1)
                    Utils.see_package_status(truck3, 10, 25, 0,9,35,1)

                    # view package status #3
                    status_3 = input("\nYou can now see package status #3\n"
                                     "[1] To see the status of packages delivered between 12:03 p.m. and 1:12 p.m  \n"
                                     "(Enter anything else to exit)\n")

                    # Exit system on bad input
                    if status_3 != "1":
                        print("You didn't enter a valid menu option, or chose to exit the program. Please try again.")
                        SystemExit

                    # [1] See package status 3 between times specified, call to greedy path for trucks if packages are in route, clear route for trucks
                    if status_3 == "1":
                        if len(truck1.route) > 0:
                            Utils.deliver_packages(truck1, 17, 25, 0,8, 0,0)
                            Utils.clearDeliveredRoute(truck1)
                            if len(truck1.route) > 0:
                                truck1.route = Graph.greedy_path_algorithm(truck1.route, truck1.route[0])

                        if len(truck2.route) > 0:
                            Utils.deliver_packages(truck2, 18, 25, 0,9,5,0)
                            Utils.clearDeliveredRoute(truck2)
                            if len(truck2.route) > 0:
                                truck2.route = Graph.greedy_path_algorithm(truck2.route, truck2.route[0])

                        if len(truck3.route) > 0:
                            Utils.deliver_packages(truck3, 17, 25, 0, truck3.start_time.hour, truck3.start_time.minute,
                                           truck3.start_time.second)
                            Utils.clearDeliveredRoute(truck3)
                            if len(truck3.route) > 0:
                                truck3.route = Graph.greedy_path_algorithm(truck3.route, truck3.route[0])

                        Utils.see_package_status(truck1, 13, 12, 0,12,3,1)
                        Utils.see_package_status(truck2, 13, 12, 0,12,3,1)
                        Utils.see_package_status(truck3, 13, 12, 0,12,3,1)


                        # view the final results
                        final = input("\nView final result of the delivery?\n"
                                      "[1] Yes, see all package delivery details including finish time and total mileage.\n"
                                      "(Enter anything else to exit)\n")

                        # Exit system on bad input
                        if final != "1":
                            print("You didn't enter a valid menu option, or chose to exit the program. Please try again.")
                            SystemExit

                        # [1] Final output for the program
                        if final == "1":
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

                            Utils.see_package_status(truck1, 13, 12, 0,8,0,0)
                            Utils.see_package_status(truck2, 13, 12, 0,8,0,0)
                            Utils.see_package_status(truck3, 17, 12, 0,8,0,0)
                            truck1_miles = truck1.traveled_miles()
                            truck2_miles = truck2.traveled_miles()
                            truck3_miles = truck3.traveled_miles()
                            total = truck1_miles + truck2_miles + truck3_miles
                            print("Truck 1: ", round(truck1_miles, 2), "+ Truck 2: ", round(truck2_miles, 2),
                                  "+ Truck 3: ", round(truck3_miles, 2), " TOTAL =", round(total, 2), "miles")
                            print("All trucks have returned to the hub by", truck2.finish_time.time())
                            SystemExit

    # Menu option #2 lookup packages by ID
    if main_menu == "2":
        print("Update: The time is 7:59AM. All packages are waiting at the hub or delayed.")

        checker = "1"
        while checker == "1":

            user_search_string = input("Enter the package ID# you want to search: ")
            try:
                user_search_int = int(user_search_string)
                print_search_result(packageHashTable, user_search_int)
            except ValueError:
                print("You didn't enter a valid number for the ID")
            try_again = input("Enter 1 to re-search or anything else to exit: ")
            checker = try_again
        userinterface()


# program entry
print("WGU Delivery System: The time is 7:59AM")
userinterface()




