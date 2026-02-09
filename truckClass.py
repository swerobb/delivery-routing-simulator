from datetime import timedelta
class Truck:
    """
    Represents a delivery truck in the system(Truck object).
    Each truck will track its ID, a list of package id's it needs to deliver, the mileage travelled,
    its current location, the current simulated time.
    """
    def __init__(self, truck_id, package_ids, start_time):
        """
        Initializes a new Truck object with an ID, packages, and start time
        :param truck_id: identifies the truck
        :param package_ids: list of package ids associated with the truck
        :param start_time: Timestamp when the truck leaves the hub
        """
        self.truck_id = truck_id
        self.package_ids = package_ids
        self.speed = 18
        self.mileage = 0.0
        self.current_time = start_time
        self.current_location = 0 #represents hub

    def drive_simulation(self, next_location, distance):
        """
        Simulates driving a truck based on its current location to the next location
        :param next_location: Index to identify the next location in the distance matrix
        :param distance: Distance represented in miles from current location to next location

        First we compute how long it takes to travel a certain distance at the trucks given speed.
        We then add that travel time to the trucks current time, next we add the distance to the trucks total mileage.
        The current location gets updated to the new location and we return the updated current time.

        Returns: the updated current time after going through the truck simulation.
        """
        #calculates the travel time as a timedelta based on distance and speed
        travel_time = timedelta(hours=distance / self.speed)
        #advances the truck's internal clock by the travel time
        self.current_time += travel_time
        #accumulates the distance travelled
        self.mileage += distance
        #moves the truck to the new location
        self.current_location = next_location
        #returns the updated time, needed for callers to see when the truck arrives
        return self.current_time

    #for debugging, checks truck status....current status: working.
    #def __str__(self):
        #return f"Truck {self.truck_id}: Mileage {self.mileage:.2f} miles, Time {self.current_time.strftime('%I:%M %p')}"
