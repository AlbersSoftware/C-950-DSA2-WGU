# Chris Albers, ID:(009877757), C-950 DSA2- C1 requirement
from datetime import timedelta, datetime

import Graph
from Truck import Truck
from utils import Utils

from hashtable import print_search_result, get_packages
from hashtable import HashTable
packageHashTable = Utils.loadPackageData('Data/package_file.csv')


# C2 requirement- Process and flow of the program is determined here in the main. Each section is labled as you go through the CMI as to whats happening.
# time and space complexity of the program is O(n^2)
# time and space complexity of the program is O(n^2)
def userinterface():
    pass






            # set the initial datetime for each truck.
    truck1 = Truck(truck_id=1, capacity=16, startTime=datetime(2023, 1, 1, 8, 0, 0))
    truck2 = Truck(truck_id=2, capacity=16, startTime=datetime(2023, 1, 1, 9, 5, 0))
    truck3 = Truck(truck_id=3, capacity=16, startTime=datetime(2023, 1, 1, 10, 0, 0))

    # create a list of all packages from hashtable
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

    # main menu with options to either view final results and give a specific time to see if packages are at hub, en route or delievered and second option is to look up an individual package by ID# after a given time.
    main_menu = input("----MAIN MENU----\n"
                      "[1] View final results and give a specific time to see if packages are at hub, en route or delievered \n"
                      "[2] Lookup individual package status by entering a time and a package ID # \n"
                      
                      "(enter anything else to exit) \n")

    # exit the program on bad input
    if main_menu != "1" and main_menu != "2":
        print("You didn't enter a valid menu option! Press [1] View final results and give a specific time to see if packages are at hub, en route or delievered and [2] to look up packages by time and ID. (Program Closing) Please try again.")
        SystemExit

    if main_menu == "1":
        # load trucks and their priorities, Set the greedy path, deliver packages on truck 1 to 925, truck 2 to 1025, and then 1130 as priority is set. Clear route as they get delivered.
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
        # fix address for package #9 as this is part of the final output, call to greedy path, deliver packages, and clear the route as before.

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
        # check if truck1 is back at hub and if so then update truck 3 start time to truck1 return time. load truck 3 priority and packages, deliver and clear route.
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

        # final output, check what hasn't been delivered yet for each truck and deliver them. Time is set high so all packages have been delivered clear the route and call to greedy path.
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
        # see package status of packages starting at 8am- finish for all trucks, tally the total miles traveled and display the total time traveled by all trucks and package delivery time by truck #.
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



       # look up package status by time, enter a valid time and see where packages are. Either 'at hub' 'en-route' or 'Delivered At- (specified time)'

        user_time = input(
            "Please enter a time to check the status of package(s). Use the following format, HH:MM:SS: ")
        user_time_arr = user_time.split(":") # reads the time split, you still need to enter the ':'s. If the user misses a digit or if its not a digit print the bad input statement and close program.
        if len(user_time_arr) != 3 or not all(segment.isdigit() for segment in user_time_arr):
            print(
                "You must enter The hours, minutes and seconds seprated by :, Here is 3 examples of accepted input: 10:45:00, 9:15:11, 13:09:00. (Program Closing) Please try again!")
            raise SystemExit
        hours = int(user_time_arr[0]) # create local variables to check if the hour, minute, and second arrays are valid.
        minutes = int(user_time_arr[1])
        seconds = int(user_time_arr[2])

        if not (0 <= hours <= 23) or not (0 <= minutes <= 59) or not (0 <= seconds <= 59):
            print(
                "You entered an unrealistic time, It must be less than 24 hours, less than 59 minutes and less than 59 seconds.(Program Closing) Please try again!")
            raise SystemExit
        convert_time = datetime(2023, 1, 1, int(user_time_arr[0]), int(user_time_arr[1]), int(user_time_arr[2]),
                                tzinfo=None)
        for package in truck2.truck_packages: # if user enters a time less than 10:20AM make sure the address is still not fixed yet.
            if package.ID == 9 and int(user_time_arr[0]) < 10 or (int(user_time_arr[0]) == 10 and int(user_time_arr[1]) < 20):

                package.destination = "300 State St"
                package.city = "Salt Lake City"
                package.state = "UT"
                package.zip = "84103"
                package.notes = "Wrong address listed"
                truck2.route.append(package.destination)
                break
        # converted time becomes the user input in see package status finish times.
        Utils.see_package_status(truck1, convert_time.hour, convert_time.minute, convert_time.second, 8, 0, 0)
        Utils.see_package_status(truck2, convert_time.hour, convert_time.minute, convert_time.second, 8, 0, 0)
        Utils.see_package_status(truck3, convert_time.hour, convert_time.minute, convert_time.second, 8, 0, 0)
        print("\n*****IN ORDER BY ID*****\n") # loop through packages and print them by user ID to make it easier for the evaluators. The updated info travels with the ordered print as well not just when its ordered by truck.
        for i in range(len(packageHashTable.table)):
            package = packageHashTable.search(i + 1)

            hour = int(user_time_arr[0])
            minute = int(user_time_arr[1])
            second = int(user_time_arr[2])



            if package:

                print("Package ID: {}, Destination: {}, Status {}".format(package.ID, package.destination,package.status))


        # end of program for menu option one
        SystemExit







    # Menu option #2 lookup packages by giving a time and an ID
    if main_menu == "2":


        checker = "1"
        while checker == "1":
            # user inputs a time and like above must be in the correct format
            user_time = input(
                "Please enter a time to check the status of packages. Use the following format, HH:MM:SS: ")
            user_time_arr = user_time.split(":")
            if len(user_time_arr) != 3 or not all(segment.isdigit() for segment in user_time_arr):
                print(" You must enter The hours, minutes and seconds seprated by :, Here is  3 examples of accepted input: 10:45:00, 9:15:11, 13:09:00. (Program Closing) Please try again!")
                raise SystemExit
            hours = int(user_time_arr[0])
            minutes = int(user_time_arr[1])
            seconds = int(user_time_arr[2])

            if not (0 <= hours <= 23) or not (0 <= minutes <= 59) or not (0 <= seconds <= 59):
                print("You entered an unrealistic time, It must be less than 24 hours, less than 59 minutes and less than 59 seconds. (Program Closing) Please try again!")
                raise SystemExit

            convert_time = datetime(2023, 1, 1, int(user_time_arr[0]), int(user_time_arr[1]), int(user_time_arr[2]), tzinfo=None)
            #load trucks, start delivery, call to greedy path and clear route in the same fashion as menu option 1.
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
            # fix address only this time the logic > is the opposite as menu option 1.
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
            # check if truck1 is back at hub and if so then update truck 3 start time to truck1 return time. load truck 3 priority and packages, deliver and clear route.
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
            # final delivery process which is the same as before in menu option 1.
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

            # converted time becomes the user input in see package status finish times.
            Utils.see_package_status(truck1, convert_time.hour, convert_time.minute, convert_time.second, 8, 0,0)
            Utils.see_package_status(truck2, convert_time.hour, convert_time.minute, convert_time.second, 8, 0,0)
            Utils.see_package_status(truck3, convert_time.hour, convert_time.minute, convert_time.second, 8, 0,0)








            # Search for package by ID from the hashtable, validate input is correct, end of program.

            user_search_string = input("\n ***Enter the package ID# you want to search: \n")
            try:
                user_search_int = int(user_search_string)
                print_search_result(packageHashTable, user_search_int)
                print("The search is completed!(Program Closing) Good Bye!")
                raise SystemExit

            except ValueError:
                print("You didn't enter a valid number for the ID. You can enter a number 1 through 40. (Program Closing) Please try again!")
                raise SystemExit

        userinterface()


# program entry
print("WGU Delivery System: Pick a Menu Option below")
userinterface()




