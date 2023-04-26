import csv
from Packages import Package
from Graph import graph
from Graph import greedy_path_algorithm
from datetime import timedelta, datetime
import hashtable
import Truck

class Utils:

    @staticmethod
    def add_seconds(time, sec):
        date = datetime(100, 1, 1, time.hour, time.minute, time.second)
        date = date + timedelta(seconds=sec)
        return date.time()

    @staticmethod
    def out_for_delivery(truck_packages):
        for package in truck_packages:
            package.status = "OUT_FOR_DELIVERY"

    @staticmethod
    def see_package_status(trucks,hour, min, sec):
        '''miles_between = graph.edge_weights
        print(hour)
        stop_time = datetime(2023, 1, 1, hour, min, sec)

        # Truck 1 Delivery
        trucks.start_time = datetime(2023, 1, 1, 1, 1, 1)
        trucks.current_time = trucks.start_time
        Utils.out_for_delivery(trucks.truck_packages)
        if ('600 E 900 South', '3595 Main St') in miles_between:
            print("dkjfkd")
        else:
            print("No distance data available for this address pair.")

        for i in range(0, len(trucks.route) - 1):
            if trucks.route[i] == trucks.route[i + 1]:
                continue  # skip this iteration if the same stop is repeated
            if miles_between[trucks.route[i], trucks.route[i + 1]] != '':
                distance = miles_between[trucks.route[i], trucks.route[i + 1]]
                speed = trucks.speed
                minutes_decimal = distance / speed
                seconds_to_add = round(minutes_decimal * 60, 2)
                delivered_time = Utils.add_seconds(trucks.current_time, seconds_to_add)
                if delivered_time < stop_time.time():
                    trucks.current_time = datetime(2023, 1, 1, delivered_time.hour, delivered_time.minute,
                                               delivered_time.second)
                    updated_delivery_status = "DELIVERED AT", str(delivered_time)
                    for package in trucks.truck_packages:
                        if trucks.route[i + 1] == package.destination:
                            package.status = updated_delivery_status
                trucks.finish_time = trucks.current_time'''
        print("Truck " + str(trucks.truck_id) + " Delivery:", *trucks.truck_packages, sep="\n")  # prints using new lines instead of a giant line
    @staticmethod
    def deliver_packages(trucks):
        miles_between = graph.edge_weights
        total_miles_driven = 0.0
        truck_start = trucks.start_time
        trucks.start_time = truck_start
        trucks.current_time = truck_start

        for i in range(0, len(trucks.route) - 1):
            if trucks.route[i] == trucks.route[i + 1]:
                continue
            if miles_between[trucks.route[i], trucks.route[i + 1]] != '':
                distance = miles_between[trucks.route[i], trucks.route[i + 1]]
                speed = trucks.speed
                minutes_decimal = distance / speed
                seconds_to_add = round(minutes_decimal * 60, 2)
                delivered_time = Utils.add_seconds(trucks.current_time, seconds_to_add)
                trucks.current_time = datetime(2023, 1, 1, delivered_time.hour, delivered_time.minute,
                                               delivered_time.second)
                updated_delivery_status = f"DELIVERED AT {str(delivered_time)}"
                if trucks.truck_packages[i].status.startswith("On Truck"):
                    trucks.truck_packages[i].status = updated_delivery_status
                elif trucks.route[i + 1] == trucks.truck_packages[i].destination and trucks.truck_packages[i].status == "DELAYED":
                    continue
                '''for package in trucks.truck_packages:
                    if trucks.route[i] == package.destination and package.status.startswith("On Truck"):
                        package.status = updated_delivery_status
                    elif trucks.route[i + 1] == package.destination and package.status == "DELAYED":
                        continue'''
                trucks.finish_time = trucks.current_time
                # update total miles driven
                #total_miles_driven += sum(float(miles_between[trucks.route[i], trucks.route[i + 1]]))
        trucks.start_time = trucks.finish_time
        print("Deliver Truck " + str(trucks.truck_id) + " Delivery:", *trucks.truck_packages,
                  sep="\n")  # prints using new lines instead of a giant line

    @staticmethod
    def loadPackageData(file):
        print("Loading package data...")
        packageHashTable = hashtable.HashTable()
        with open(file) as packages:
            packageData = csv.reader(packages, delimiter=',')
            #next(packageData)
            for row in packageData:
                package = list(row)
                packageID = int(package[0])
                packageDestination = package[1]
                packageCity = package[2]
                packageState = package[3]
                packageZip = package[4]
                packageDeadline = package[5]
                packageWeight = package[6]
                packageNotes = package[7]
                packageStatus = "Loaded"

                p = Package(packageID, packageDestination, packageCity, packageState,
                            packageZip, packageDeadline, packageWeight, packageNotes, packageStatus)
                packageHashTable.insert(packageID, p)
            return packageHashTable

'''
                # Truck 2 Delivery
                truck2_start = datetime(2020, 1, 1, 9, 5, 0)
                truck2.start_time = truck2_start
                truck2.current_time = truck2_start
                for i in range(0, len(truck2.route) - 1):
                    if truck2.route[i] == truck2.route[i + 1]:
                        continue
                    distance = miles_between[truck2.route[i], truck2.route[i + 1]]
                    speed = truck2.speed
                    minutes_decimal = distance / speed
                    seconds_to_add = round(minutes_decimal * 60, 2)
                    delivered_time = add_seconds(truck2.current_time, seconds_to_add)
                    truck2.current_time = datetime(2020, 1, 1, delivered_time.hour, delivered_time.minute,
                                                   delivered_time.second)
                    updated_delivery_status = "DELIVERED AT", str(delivered_time)
                    for package in truck2.truck_packages:
                        if truck2.route[i + 1] == package.destination and package.status == "AT HUB":
                            package.status = updated_delivery_status
                        elif truck2.route[i + 1] == package.destination and package.status == "DELAYED":
                            continue
                    truck2.finish_time = truck2.current_time
                    print("Truck 2 Delivery:", *truck2.truck_packages,
                          sep="\n")  # prints using new lines instead of a giant line
                  
                # Truck 3 Delivery
                truck3_start = truck1.finish_time
                truck3.start_time = truck3_start
                truck3.current_time = truck3_start
                for i in range(0, len(truck3.route) - 1):
                    if truck3.route[i] == truck3.route[i + 1]:
                        continue
                    distance = miles_between[truck3.route[i], truck3.route[i + 1]]
                    speed = truck3.speed
                    minutes_decimal = distance / speed
                    seconds_to_add = round(minutes_decimal * 60, 2)
                    delivered_time = add_seconds(truck3.current_time, seconds_to_add)
                    truck3.current_time = datetime(2020, 1, 1, delivered_time.hour, delivered_time.minute,
                                                   delivered_time.second)
                    updated_delivery_status = "DELIVERED AT", str(delivered_time)
                    for package in truck3.truck_packages:
                        if truck3.route[i + 1] == package.destination:
                            package.status = updated_delivery_status
                    truck3.finish_time = truck3.current_time
                    print("Truck 3 Delivery:", *truck3.truck_packages,
                          sep="\n")  # prints using new lines instead of a giant line
                    ''''''
                   
                

        ''
# Truck 2 Delivery
        truck2_start = datetime(2020, 1, 1, 9, 5, 0)
        truck2.start_time = truck2_start
        truck2.current_time = truck2_start
        truck2.out_for_delivery()
        for i in range(0, len(truck2.route) - 1):
            if truck2.route[i] == truck2.route[i + 1]:
                continue  # skip this iteration if the same stop is repeated
            print(truck2.route[i], truck2.route[i + 1])
            distance = miles_between[truck2.route[i], truck2.route[i + 1]]
            speed = truck2.speed
            minutes_decimal = distance / speed
            seconds_to_add = round(minutes_decimal * 60, 2)
            delivered_time = Utils.add_seconds(truck2.current_time, seconds_to_add)
            if delivered_time < stop_time.time():
                truck2.current_time = datetime(2020, 1, 1, delivered_time.hour, delivered_time.minute,
                                               delivered_time.second)
                updated_delivery_status = "DELIVERED AT", str(delivered_time)
                for package in truck2.truck_packages:
                    if truck2.route[i + 1] == package.destination:
                        package.status = updated_delivery_status
            truck2.finish_time = truck2.current_time
            print("Truck 2 Delivery:", *truck2.truck_packages, sep="\ n")  # prints using new lines instead of a giant line

        # Truck 3 Delivery
        truck3_start = truck1.finish_time
        truck3.start_time = truck3_start
        truck3.current_time = truck3_start
        truck3.out_for_delivery()
        for i in range(0, len(truck3.route) - 1):
            if truck3.route[i] == truck3.route[i + 1]:
                continue  # skip this iteration if the same stop is repeated
            distance = miles_between[truck3.route[i], truck3.route[i + 1]]
            speed = truck3.speed
            minutes_decimal = distance / speed
            seconds_to_add = round(minutes_decimal * 60, 2)
            delivered_time = Utils.add_seconds(truck3.current_time, seconds_to_add)
            if delivered_time < stop_time.time():
                truck3.current_time = datetime(2020, 1, 1, delivered_time.hour, delivered_time.minute,
                                               delivered_time.second)
                updated_delivery_status = "DELIVERED AT", str(delivered_time)
                for package in truck3.truck_packages:
                    if truck3.route[i + 1] == package.destination:
                        package.status = updated_delivery_status
            truck3.finish_time = truck3.current_time
            #print("Truck 3 Delivery:", *truck3.truck_packages, sep="\ n")
           '''



'''' # update total miles driven
        print(miles_between)
        total_miles_driven += sum(miles_between[truck2.route[i], truck2.route[i + 1]]
        for i in range(len(truck2.route) - 1) if truck2.route[i])
        
                # print total miles driven
                print("Total miles driven:", total_miles_driven)

        # update total miles driven
        total_miles_driven += sum(miles_between[truck3.route[i], truck3.route[i + 1]])
         for i in range(len(truck3.route) - 1))'''


def isfloat(distances):
    return None