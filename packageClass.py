class Package:
    """
    This class represents a single package with all of its information and status.
    This class stores package data and tracks the package's status over time based on its timestamps.
    """
    def __init__(self, package_id, address, city, state, zip_code, delivery_deadline, weight, note):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.note = note

        self.status = "At Hub"
        self.depart_time = None
        self.delivery_time = None

    def update_status(self, new_status, time=None):
        """
        Updates the status of the package and records the timestamp.
        :param new_status (str): New status of the package("At Hub", "En Route", or "Delivered").
        :param time: The time associated with the status change.
        :return:
        """
        # if the package leaves the hub, record the departure time
        if new_status == "En Route" and time:
            self.depart_time = time
        #if the package is getting delivered record the delivery time
        if new_status == "Delivered" and time:
            self.delivery_time = time
        #updates to the current status
        self.status = new_status

    def get_status_at(self, check_time):
        """
        Returns the status of the package at the given time.

        If the package has a delivery time and check_time is at or after that, it's labeled as "Delivered".
        Else if the package has a departing time and check_time is at or after that, it's labeled as "En Route".
        Else it's labeled as "At Hub".
        """
        #If delivered, report the exact time of delivery
        if self.delivery_time and check_time >= self.delivery_time:
            return f"Delivered at {self.delivery_time.strftime('%I:%M %p')}"
        #if it has left the hub and not delivered yet, show en route
        if self.depart_time and check_time >= self.depart_time:
            return "En Route"
        #otherwise it means it still at hub
        return "At Hub"

    def __str__(self):
        """
        Returns a readable string representation of the package.
        """
        return (
            f"Package ID: {self.package_id}\n"
            f"Address: {self.address}\n"
            f"City: {self.city}\n"
            f"State: {self.state}\n"
            f"Zip Code: {self.zip_code}\n"
            f"Delivery Deadline: {self.delivery_deadline}\n"
            f"Weight: {self.weight}\n"
            f"Note: {self.note}\n"
            f"Status: {self.status}\n"
            f"Delivery Time: {self.delivery_time}\n"
        )

    def __repr__(self):
        return self.__str__()
