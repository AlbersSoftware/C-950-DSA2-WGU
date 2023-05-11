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
    def see_package_status(trucks,hour, min, sec, startHr, startMin,startSec):

        print("Delivered Package on Truck " + str(trucks.truck_id))  # prints using new lines instead of a giant line
        for pkg in trucks.truck_packages:
            if (pkg.status.startswith("DELIVERED AT")):
                timeStr = pkg.status.replace("DELIVERED AT", "")
                timeArr = timeStr.split(":")
                timeForDelivery = datetime(2023, 1, 1, int(timeArr[0]), int(timeArr[1]),
                                                   int(timeArr[2]),tzinfo=None)
                timeForEndStatus = datetime(2023, 1, 1, hour, min,sec,tzinfo=None)
                timeForStartStatus = datetime(2023, 1, 1, startHr, startMin, startSec, tzinfo=None)
                if (str( timeForDelivery - timeForEndStatus)).startswith("-1 day") and (str( timeForStartStatus - timeForDelivery)).startswith("-1 day"):
                    print(pkg)

    '''
        Update all the package on the same address are updated as delivered
    '''
    @staticmethod
    def updatePackageStatus(packages, route, status):
        for inlinePackage in packages:
            if inlinePackage.destination == route and inlinePackage.status.startswith("On Truck"):
                inlinePackage.status = status
            elif route == inlinePackage.destination and inlinePackage.status == "DELAYED":
                continue

    @staticmethod
    def isreadytodeliver(truckspackage, hour, min, sec, startHr, startMin,startSec, timeForDelivery):
        for inlinePackage in truckspackage:
            if (inlinePackage.notes != 'Wrong address listed'):
                timeForEndStatus = datetime(2023, 1, 1, hour, min, sec, tzinfo=None)
                timeForStartStatus = datetime(2023, 1, 1, startHr, startMin, startSec, tzinfo=None)
                if (str( timeForDelivery - timeForEndStatus)).startswith("-1 day") and (str( timeForStartStatus - timeForDelivery)).startswith("-1 day"):
                    return True
                else:
                    return False
        return False

    @staticmethod
    def isallpackagedelivered(truckspackage):
        isDelivered = 0
        for inlinePackage in truckspackage:
            if inlinePackage.status.startswith("DELIVERED AT"):
                isDelivered += 1
        return isDelivered

    @staticmethod
    def clearDeliveredRoute(trucks):
        for completedroute in trucks.completedroute:
            try:
                trucks.route.remove(completedroute)
            except:
                i =0

    @staticmethod
    def deliver_packages(trucks,hour, min, sec, startHr, startMin,startSec):
        miles_between = graph.edge_weights
        truck_start = trucks.start_time
        trucks.start_time = truck_start
        trucks.current_time = truck_start
        for i in range(0, len(trucks.route)-1):
            if i < len(trucks.truck_packages):

                distance = miles_between[trucks.route[i], trucks.route[i + 1]]
                if distance ==0.0:
                    distance = miles_between[trucks.route[i+1], trucks.route[i]]
                speed = trucks.speed
                minutes_decimal = distance / speed
                seconds_to_add = round(minutes_decimal * 60, 2)
                delivered_time = Utils.add_seconds(trucks.current_time, seconds_to_add)
                trucks.current_time = datetime(2023, 1, 1, delivered_time.hour, delivered_time.minute,
                                               delivered_time.second)
                #updated_delivery_status =
                if (Utils.isreadytodeliver(trucks.truck_packages, hour, min, sec, startHr, startMin,startSec,trucks.current_time)):
                    Utils.updatePackageStatus(trucks.truck_packages,trucks.route[i + 1],f"DELIVERED AT {str(delivered_time)}")
                    trucks.completedroute.append(trucks.route[i])
                else:
                    break
                trucks.finish_time = trucks.current_time
        if trucks.finish_time != None:
            trucks.start_time = trucks.finish_time
        isDelivered = Utils.isallpackagedelivered(trucks.truck_packages)
        if trucks.isInHub == False and isDelivered == len(trucks.truck_packages):
            print(trucks.isInHub)
            trucks.isInHub = True
            print(trucks.truck_id)
            print(trucks.route)
            if trucks.route[0] != trucks.hub_location:
                distance = miles_between[trucks.route[0], trucks.hub_location]
            else:
                distance = miles_between[trucks.route[len(trucks.route)-1], trucks.hub_location]
            if distance == 0.0:
                print("No route")
            speed = trucks.speed
            minutes_decimal = distance / speed
            seconds_to_add = round(minutes_decimal * 60, 2)
            delivered_time = Utils.add_seconds(trucks.current_time, seconds_to_add)
            trucks.current_time = datetime(2023, 1, 1, delivered_time.hour, delivered_time.minute,
                                           delivered_time.second)
            trucks.completedroute.append(trucks.route[0])
            trucks.finish_time = trucks.current_time
            print("PP Success")
        else:
            trucks.isInHub = False
        #print("Deliver Truck " + str(trucks.truck_id) + " Delivery:", *trucks.truck_packages,
                  #sep="\n")  # prints using new lines instead of a giant line



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




def isfloat(distances):
    return None