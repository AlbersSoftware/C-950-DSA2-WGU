import csv
from datetime import timedelta, datetime

import Graph
from Truck import Truck
from utils import Utils

from hashtable import print_search_result, get_packages
from hashtable import HashTable
packageHashTable = Utils.loadPackageData('Data/package_file.csv')


def ui():
    pass


    print("Packages from package hash table:")
    for i in range(len(packageHashTable.table)):
        package = packageHashTable.search(i + 1)
        if package:
            print("Package ID: {}, Destination: {}, Status {}".format(package.ID, package.destination, package.status))

            #call for get packages and to search packages
            #package_hashtable = get_packages("Data/package_file.csv")
            #print_search_result(package_hashtable, "1")

    truck1 = Truck(truck_id=1, capacity=16, startTime=datetime(2023, 1, 1, 8, 0, 0))
    truck2 = Truck(truck_id=2, capacity=16, startTime=datetime(2023, 1, 1, 8, 0, 0))
    truck3 = Truck(truck_id=3, capacity=10, startTime=datetime(2023, 1, 1, 9, 5, 0))

    # create a list of all packages
    all_packages = packageHashTable.get_all_values()





    # print the packages on each truck
    print("Truck 1 packages:")
    for package in truck1.truck_packages:
        print(package)

    print("\nTruck 2 packages:")
    for package in truck2.truck_packages:
        print(package)

    print("\nTruck 3 packages:")
    for package in truck3.truck_packages:
        print(package)


    main_menu = input("What would you like to do? \n"
                      "[1] Load Trucks (Insert Packages) \n"
                      "[2] Lookup Individual Package \n"
                      "ENTER 0 TO EXIT \n")

    # [0] Exit the program
    if main_menu == "0":
        print("You entered 0 or did not enter a valid menu option.")
        print("Goodbye!")
        SystemExit

    # [1] Load Trucks
    if main_menu == "1":
        print("The time is now 8:00")
        print("Packages were inserted into hash table and packages were loaded onto trucks.")
        # load the packages onto the trucks
        truck1.putPackageInDeliveryDict(all_packages)
        truck1.load_packages(all_packages)
        truck2.putPackageInDeliveryDict(all_packages)
        truck2.load_packages(all_packages)
        truck3.putPackageInDeliveryDict(all_packages)
        truck3.load_packages(all_packages)

        #truck1.load_trucks_and_get_best_route()
        #truck2.load_trucks_and_get_best_route()
        #truck3.load_trucks_and_get_best_route()


        status_1 = input("\nEnter 1 to go package status #1 \n"
                         "[1] See package status of all packages between 8:35 a.m. and 9:25 a.m \n"
                         "ENTER 0 TO EXIT \n")

        # [0] Exit the program
        if status_1 == "0":
            print("You entered 0 or did not enter a valid menu option.")
            SystemExit

        # [1] Package status #1
        if status_1 == "1":
            # the graph call might need to be elsewhere
            truck1.route = Graph.greedy_path_algorithm(truck1.route)
            truck2.route = Graph.greedy_path_algorithm(truck2.route)
            #truck3.route = Graph.greedy_path_algorithm(truck3.route)

            Utils.deliver_packages(truck1)
            Utils.deliver_packages(truck2)

            Utils.see_package_status(truck1, 9, 25, 0,8, 0,0)
            Utils.see_package_status(truck2, 9, 25, 0,8,0,0)
            Utils.see_package_status(truck3, 9, 25, 0,8,0,0)

            # Next: Fix the package #9 address
            print("\nURGENT! IT IS 10:20AM. YOU NEED TO FIX THE ADDRESS FOR PACKAGE #9")
            fix_pkg = input("Fix address package #9? Enter 1 for YES or 0 TO EXIT: ")

            # [0] Exit the program
            if fix_pkg == "0":
                print("You entered 0 or did not enter a valid menu option.")
                SystemExit

            # [1] YES, fix the package
            if fix_pkg == "1":
                print("Fixing package #9 address to 410 S State St., Salt Lake City, UT 84111 ... ")
                for package in truck3.truck_packages:
                    if package.ID == "9":
                        package.destination = "410 S State St"
                        package.city = "Salt Lake City"
                        package.state = "UT"
                        package.zip = "84111"
                        break  # stop looping once you've updated the package
               # truck3.route = Graph.greedy_path_algorithm(truck3.route)
                Utils.deliver_packages(truck3)
                Utils.see_package_status(truck3, 9, 23, 0,8,0,0)
                #truck1.route = Graph.greedy_path_algorithm(truck1.route)  # updates route with the best route
                #truck1.route.append("4001 South 700 East")  # bring the truck back to the hubs
                print("You fixed the address!")

                # Next: See package status 2
                status_2 = input("\nNow, you can view package status #2\n"
                                 "[1] See package status of all packages between 9:35 a.m. and 10:25 a.m \n"
                                 "ENTER 0 TO EXIT\n")

                # [0] Exit the program
                if status_2 == "0":
                    print("You entered 0 or did not enter a valid menu option.")
                    SystemExit

                if status_2 == "1":
                    Utils.see_package_status(truck1, 10, 23, 0,9,25,1)
                    Utils.see_package_status(truck2, 10, 23, 0,9,25,1)
                    Utils.see_package_status(truck3, 10, 23, 0,9,25,1)

                    # Next: See package status 3
                    status_3 = input("\nNow, you can view package status #3\n"
                                     "[1] See package status of all packages between 12:03 p.m. and 1:12 p.m (13:12) \n"
                                     "ENTER 0 TO EXIT\n")

                    # [0] Exit the program
                    if status_3 == "0":
                        print("You entered 0 or did not enter a valid menu option.")
                        SystemExit

                    # [1] See package status 3
                    if status_3 == "1":
                        Utils.see_package_status(truck1, 13, 12, 0,10,23,1)
                        Utils.see_package_status(truck2, 13, 12, 0,10,23,1)
                        Utils.see_package_status(truck3, 13, 12, 0,10,23,1)
                        #Utils.see_package_status(13, 12, 0)

                        # Last, the user can view the final results
                        final = input("\nSEE FINAL RESULTS OF THE TRUCK DELIVERY SIMULATION?\n"
                                      "[1] YES, see all package delivery details, total mileage, and time finished\n"
                                      "ENTER 0 TO EXIT\n")

                        # [0] Exit the program
                        if final == "0" or final != "1":
                            print("You entered 0 or did not enter a valid menu option.")
                            SystemExit

                        # [1] See final results and exit the program!
                        if final == "1":
                            Utils.see_package_status(truck1, 13, 12, 0,8,0,0)
                            Utils.see_package_status(truck2, 13, 12, 0,8,0,0)
                            Utils.see_package_status(truck3, 13, 12, 0,8,0,0)
                            t1_miles = truck1.miles_traveled()
                            t2_miles = truck2.miles_traveled()
                            t3_miles = truck3.miles_traveled()
                            total = t1_miles + t2_miles + t3_miles
                            print("Truck 1: ", round(t1_miles, 2), "+ Truck 2: ", round(t2_miles, 2),
                                  "+ Truck 3: ", round(t3_miles, 2), " TOTAL =", round(total, 2), "miles")
                            print("All trucks are back at hub by", truck3.finish_time.time())
                            SystemExit

    # Lookup Individual Package
    if main_menu == "2":
        print("Reminder: The time is 7:59AM. All packages are either AT_HUB or DELAYED_ON_FLIGHT")

        checker = "1"
        while checker == "1":
            # Prompt the user to get package ID to search for.
            user_search_string = input("Enter the ID of the package you would like to search for: ")
            try:
                user_search_int = int(user_search_string)
                print_search_result(packageHashTable, user_search_int)
            except ValueError:
                print("You did not enter an integer for the ID")
            try_again = input("Enter 1 to search again. Enter anything else to exit: ")
            checker = try_again
        ui()


# Program starts here
print("Welcome to WGUPS! The time is 7:59AM")
ui()




