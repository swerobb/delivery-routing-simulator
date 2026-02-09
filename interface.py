from datetime import datetime


def user_interface(package_table, trucks):
    """
    Interface to view WGUPS program, displays summerized and detailed package
    information at a specific time. Also displays truck milage information.

    :param package_table: Hash table of packages
    :param trucks: List of trucks
    """
    def prompt_time():
        """
        Prompts the user to enter a time and returns the datetime object.
        """
        while True:
            time_input = input("Please Enter a time (HH:MM AM/PM): ")
            try:
                return datetime.strptime(time_input.strip().upper(), "%I:%M %p")
            except ValueError:
                print("Invalid time, please try again, use HH:MM AM/PM")

    def get_truck_assignment(package_id):
        """
        Retrieves the truck assignment for a given package id

        :param package_id: package id
        :return: String , "Truck.."
        """
        for truck in trucks:
            if package_id in truck.package_ids:
                return f"Truck {truck.truck_id}"
        return None

    #def print_cute_truck_image():
        truck = r"""
        
             ___________________________                      
            |                           |
            |     DELIVERY TRUCK        |_______    
            |                                   | 
            |___________________________________|
                ()()                    ()()
        """
       #print(truck)"

    #Builds the list of package ids by reading from the hashtable
    package_ids = sorted(
        package_id
        for bucket in getattr(package_table, "buckets_list", [])
        for package_id, _ in bucket
    )
    if not package_ids:
        package_ids = list(range(1, 41))

    #Main menu
    while True:
        print()
        print("   WGUPS DELIVERY SYSTEM INTERFACE  ")
        print("1. View All Package Information (Summarized)")
        print("2. View All Package Information (Detailed)")
        print("3. View Total Mileage")
        print("4. Exit")

        choice = input("Enter a number: ")

        #Shows summerized package information
        if choice == "1":
            check_time = prompt_time()
            print()
            print(f"Package Status Summary as of {check_time.strftime('%I:%M %p')}:")
            for package_id in package_ids:
                package = package_table.lookup(package_id)
                if not package:
                    continue
                truck_assignment = get_truck_assignment(package_id)
                status = package.get_status_at(check_time)
                if status == "At Hub":
                    location = "(At Hub)"
                elif status.startswith("Delivered"):
                    location = "(Delivered)"
                else:
                    location = f"({truck_assignment})" if truck_assignment else "(En Route)"
                print(f"Package {package_id:<2}: {status:<25}{location}")

        #Shows detailed package information
        elif choice == "2":
            check_time = prompt_time()
            print()
            print(f"Detailed Package Information as of {check_time.strftime('%I:%M %p')}:")
            for package_id in package_ids:
                package = package_table.lookup(package_id)
                if not package:
                    continue
                truck_assignment = get_truck_assignment(package_id) or "N/A"
                status = package.get_status_at(check_time)
                departed_display = (
                    package.depart_time.strftime('%I:%M %p')
                    if package.depart_time and check_time >= package.depart_time
                    else "N/A"
                )
                delivered_display = (
                    package.delivery_time.strftime('%I:%M %p')
                    if package.delivery_time and check_time >= package.delivery_time
                    else "N/A"
                )
                note_text = package.note if package.note else "None"

                print()
                print(f"Package {package.package_id}")
                print(f"  Address: {package.address}, {package.city}, {package.state} {package.zip_code}")
                print(f"  Deadline: {package.delivery_deadline}")
                print(f"  Weight: {package.weight}")
                print(f"  Note: {note_text}")
                print(f"  Assigned Truck: {truck_assignment}")
                print(f"  Status: {status}")
                print(f"  Departed: {departed_display}")
                print(f"  Delivered: {delivered_display}")

        #Shows total mileage for all trucks
        elif choice == "3":
            total_miles = sum(truck.mileage for truck in trucks)
            print()
            print(f"Total Mileage For All Trucks: {total_miles:.2f} miles")

        elif choice == "4":
            print("Exit")
            break

        else:
            print("Invalid choice, please try again")
