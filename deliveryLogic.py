
def nearest_neighbor_algorithm(distances, package_ids):
    """
    Calculates a route using a nearest neighbor heuristic based on the distance matrix.
    The algorithm begins at the hub, index 0, and moves to the next nearest
    unvisited location as packages are selected as a stop.
    This continues until the package ids list is exhausted at which point
    the truck returns to the hub.

    :param distances: The 2D distance matrix where distances[i][j]
        is the distance from location i to j.
    :param package_ids: List of package ids assigned to the trucks.
    :return: Returns a list of location indices from route_list and the
        total traveled distance from distance_travelled.
    """

    #Starts the algo at the hub
    routes_list = [0]
    #Tracks which locations have been visited
    visited = [False] * len(distances)
    visited[0] = True

    #Accumulates total distance travelled
    distance_travelled = 0

    #For each package stop we pick the next nearest unvisited location
    for _ in range(1, len(package_ids)):
        #The current index location
        last = routes_list[-1]
        #Represents the next location found so far
        nearest = None
        min_distance = float("inf")

        #Go through all locations to find the closest unvisited one
        for i in range(len(distances)):
            if not visited[i] and distances[last][i] < min_distance:
                min_distance = distances[last][i]
                nearest = i

        #If there are no more reachable unvisited locations then we stop looking
        if nearest is None:
            break

        #Go to the nect chosen location
        routes_list.append(nearest)
        visited[nearest] = True
        distance_travelled += min_distance

    #Returns to the hub at the end of the route
    back_to_hub = distances[routes_list[-1]][0]
    distance_travelled += back_to_hub
    routes_list.append(0)

    return routes_list, distance_travelled


def deliver_packages(truck, distance_matrix, package_table, address_map, addresses):
    """
    Simulates  delivering all packages in a truck.
    :param truck: Truck object to track current time, location and mileage
    :param distance_matrix: Matrix of the distances between the address indices.
    :param package_table: Hashtable of packages keyed by package id number
    :param address_map: Dictionary that maps address strings to indices in the distance matrix.
    :param addresses: List of addresses in index order.

    The trucks start out as being at the hub. As long as there are packages assigned to the truck
    we will split up packages into the ones that can be delivered now and those that need to wait due
    to a "Wrong address" note before 10:20 am. If there's nothing that can be delivered then we can
    go ahead and skip time to 10:20am. From the current location we will choose
    the next package whose address is the nearest. All packages will be assigned as
    "EN Route" once the truck leaves to the hub. The truck will then drive to the chosen
    address and mark any package for that location as "Delivered". After the last package has been
    delivered the truck will return back to the hub.

    """
    hub_index = 0
    truck.current_location = hub_index

    #Filters out for packages that exist in the package table
    pending_ids = [package_id for package_id in truck.package_ids if package_table.lookup(package_id)]

    #Flag to make sure "En Route" is set only once
    en_route_set = False

    #Continue till all assigned packages have been delivered or removed
    while pending_ids:
        #Sets the time for package 9
        hold_time = truck.current_time.replace(hour=10, minute=20)

        available_ids = []
        hold_ids = []

        #Separates pending packages into either the available list or hold list
        for package_id in pending_ids:
            package = package_table.lookup(package_id)
            if not package:
                continue
            #If packages note is "Wrong address" don't deliver before the hold time
            if "Wrong address" in package.note and truck.current_time < hold_time:
                hold_ids.append(package_id)
            else:
                available_ids.append(package_id)

        #Exits if nothing is on hold or gets delivered
        if not available_ids:
            if not hold_ids:
                break

            #If only the packages held back remain then move the
            # trucks time forward to 10:20am and deliver those packages
            truck.current_time = hold_time
            truck.current_location = hub_index
            available_ids = hold_ids

        #Current location in the distance matrix
        current_index = truck.current_location


        #This helper function gets us the distance from the current location
        # to a packages address
        def distance_to_package(package_id):
            package = package_table.lookup(package_id)
            index = address_map.get(package.address, hub_index)
            return distance_matrix[current_index][index]

        #Will select the next package whose destination is closest to
        # the current location
        next_id = min(available_ids, key=distance_to_package)
        next_package = package_table.lookup(next_id)
        next_index = address_map.get(next_package.address, hub_index)


        #Marks all packages as "En Route" when trucks leaves hub
        if not en_route_set:
            for pending_id in pending_ids:
                package = package_table.lookup(pending_id)
                if package:
                    package.update_status("En Route", truck.current_time)
            en_route_set = True


        #Moves truck from current location to the next packages address
        leg_distance = distance_matrix[current_index][next_index]
        truck.drive_simulation(next_index, leg_distance)

        #Builds list of package ids that should be removed from pending ids at current stop
        delivered_now = []
        for package_id in pending_ids:
            package = package_table.lookup(package_id)
            if not package:

                #Removes package from list if not found in table
                delivered_now.append(package_id)
                continue

            #Delivers the packages that their index matches the stop
            package_index = address_map.get(package.address, hub_index)
            if package_index != next_index:
                continue
            if "Wrong address" in package.note and truck.current_time < hold_time:
                continue

            #Marks package as "Delivered" at trucks current time
            package.update_status("Delivered", truck.current_time)
            delivered_now.append(package_id)

        #Removes delivered package ids from the pending list
        for package_id in delivered_now:
            if package_id in pending_ids:
                pending_ids.remove(package_id)

    #REturns the truck back to the hub if needed once all packages delivered
    if truck.current_location != hub_index:
        leg_distance = distance_matrix[truck.current_location][hub_index]
        truck.drive_simulation(hub_index, leg_distance)
