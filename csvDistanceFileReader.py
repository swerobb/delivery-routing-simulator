import csv

def load_distance_data(csv_file_path):
    """
    Loads the distance data from the csv file and builds  1. Distance matrix which represents
    a 2D list of distances between each location, 2. Address list that represents a list of full
    address strings in row/index order. 3. Address matrix a dictionary mapping for full and short addresses to indices.
    and address matrix.
    """
    ##Opens the CSV file for reading, the encoding handles leading char causing issues.
    with open(csv_file_path, mode='r', newline='', encoding='utf-8-sig') as csv_file:
        csv_distance_reader = csv.reader(csv_file, delimiter=',')

        #2D list of float values, row and columns
        distance_matrix = []
        #List of full address strings ordered by index
        addresses = []
        #Map for address strings to index
        address_matrix = {}

        #Each row of the CSV corresponds to one address and its distances
        for csv_row in csv_distance_reader:
            #Removes and reads the first column as the full address
            full_address = csv_row.pop(0).strip()

            #Gets just the address part that we need before the first comma
            clean_address = full_address.split(",")[0].strip()

            #Adds the full address to list
            addresses.append(full_address)
            #remaning cells converted to floats and ignores empty strings
            row_floats = [float(value) for value in csv_row if value != '']
            distance_matrix.append(row_floats)

            #store both the cleaned address and full address versions in the lookup map
            address_matrix[clean_address] = len(addresses) - 1
            address_matrix[full_address] = len(addresses) - 1

    return distance_matrix, addresses, address_matrix

def make_square_matrix(triangular_matrix):
    """
    Converts a triangular matrix into a square matrix.
    Since the triangular matrix has values [i][j] the distance
    needs to need be i >= j.
    For each row i, we copy the value at [i][j] into the square matrix as [j]

    """
    #For each row i, we mirror the distance into previous rows j < i
    for i in range(len(triangular_matrix)):
        for j in range(i):
            #Append the symmetric distance value to row j so matrix [j][i] equals matrix [i][j]
            triangular_matrix[j].append(triangular_matrix[i][j])

    #Retruns a square matrix
    return triangular_matrix




