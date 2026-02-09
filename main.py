#STUDENT ID: 011918336

from csvDistanceFileReader import load_distance_data, make_square_matrix
from csvPackageFileReader import load_packages
from deliveryLogic import deliver_packages
from truckClass import Truck
from datetime import datetime
from interface import user_interface
"""
Main file to run entire delivery simulation from start to finish, also launches the 
user interface to display package and truck information.

Here we load distance and package data from our CS files, build the full distance matrix and package hashtable.
We manually assign package IDs to the three trucks, trucks objects get created at a given start time.
First truck 1 and truck 2 are simulated, truck 3 runs after truck 1 or truck 2 finishes its deliveries.
Truck 3 now gets simulated.  
"""
#Loads the distanc data and makes distance matrix square
distance_matrix, addresses, address_map = load_distance_data('wgupsDistanceFile.csv')
distance_matrix = make_square_matrix(distance_matrix)

#Loads all package into a hashtable by package id
package_table = load_packages('wgupsPackageFile.csv')

#Assign packages to trucks, based on the project's given constraints
truck1_packages = [1, 4, 7, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 39, 40]
truck2_packages = [2, 3, 5, 8, 10, 11, 12, 17, 18, 21, 23 ,24, 27, 33, 36, 38]
truck3_packages = [6, 9, 22, 26, 25, 28, 32, 35]

#Sets a universal time for when trucks leave the hub, project constraint
start_time = datetime.strptime("08:00", "%H:%M")

#Creates Truck objects with their assigned package and start time
truck1 = Truck(1, truck1_packages, start_time)
truck2 = Truck(2, truck2_packages, start_time)
truck3 = Truck(3, truck3_packages, start_time)

#Delivers packages for truck 1 & 2, both start at 8am and run full route
deliver_packages(truck1, distance_matrix, package_table, address_map, addresses)
deliver_packages(truck2, distance_matrix, package_table, address_map, addresses)

#determine first available driver to simulate driving truck 3
deliver_available_time = min(truck1.current_time, truck2.current_time)

#Corrects for package 9 dilemma
#Truck 3 will be held until a driver is free
# and the address correction time has been reached
address_correction_time = datetime.combine(
    deliver_available_time.date(),
    datetime.strptime("10:20", "%H:%M").time()
)

#Set the third trucks departure time so its not earlier than
# the available driver time or 10:20am
if deliver_available_time < address_correction_time:
    deliver_available_time = address_correction_time
truck3.current_time = deliver_available_time

#Simulates truck 3 delivering packages
deliver_packages(truck3, distance_matrix, package_table, address_map, addresses)

#Displays user interface
user_interface(package_table, [truck1, truck2, truck3])
