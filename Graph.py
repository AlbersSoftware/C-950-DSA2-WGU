import csv


class Graph:

    # initialize lists for the locations and edge weights
    # initializing empty list takes constant time and space O(1).
    def __init__(self):
        self.delivery_dict = {}
        self.edge_weights = {}

    # vertex added to the graph by mapping it to an address and the vertex is added as a key in the dict with address as its value.
    # adding a key value pair takes constant time and adding a single vertex to the delivery dict for its address takes constant space O(1).
    def add_vertex(self, vertex, address):
        self.delivery_dict[vertex] = address

    # Adds an edge between vertices. Weight represents the weight or distance associated with the edge in miles.
    # The edge weight dict is a tuple of vertices as the key and the weight as the value.
    # adding a single edge and its associated weight takes constant space and adding a key/value pair takes constant time O(1).
    def add_edge(self, vertex_a, vertex_b, weight=1.0):
        self.edge_weights[(vertex_a, vertex_b)] = weight

    # Associates each package with its corresponding vertex on the graph. It iterates through the list of packages and retrieves the destination vertex.
    # if it's not in the dict it adds the vertex with the above method 'add_vertex' and appends it to the list of packages.
    # O(n) space as n is the number of packages being placed in the delivery dict and time is O(n^2) when all packages have there own destination.
    # (n) iterations for adding vertices and (n^2) iterations for appending packages.
    def put_packages_in_delivery_dict(self, packages):
        for package in packages:
            vertex = package.destination
            if vertex not in self.delivery_dict:
                self.add_vertex(vertex)
            self.delivery_dict[vertex].append(package)


# This function returns a list of lists, where each inner list represents a row from the distance csv file creating edges between the vertices.
# O(n) space where (n) is the number of rows in the csv file and O(n) time as it iterates over each item and appends it to the list.
def get_all_distance_csv_data(filename):
    csv_data = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            csv_data.append(row)
    return csv_data
#This function also returns a list of lists, where each inner list represents a row from the address csv file.
# O(n) space where (n) is the number of rows in the csv file and O(n) time as it iterates over each item and appends it to the list.

def get_all_address_csv_data(filename):
    csv_data = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            csv_data.append(row)
    return csv_data
# this function checks if a value can be converted to a float.
# converting to a float is a constant time operation and doesn't use other data structures to scale input so is also constant space O(1).
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

# This function creates an instance of the graph and populates it with the csv data.
# Then iterates over the data and creates vertices for each address using the 'add_vertex' function.
# It also creates edges between vertices based on the distance values from the distance csv and if it can be conveted to a float or not.
# O(n) space where n is the number of rows in the csv file and O(n^2) time as it needs to iterate over the addresses to add vertices and then iterates over the distances to add edges.
# if all addresses have their own unique locations adding edges would be (n^2).
def get_graph(filename):
    data = get_all_distance_csv_data(filename)
    graph_distances = Graph()
    addresses = get_all_address_csv_data("Data/address_file.csv")
    for row in addresses:
        graph_distances.add_vertex(row[2], row)
    i = 0
    for row in data:
        j = 0
        for distances in row:
            if j < len(addresses) and addresses[i][2] != addresses[j][2]:
                if isfloat(distances):
                    graph_distances.add_edge(addresses[i][2],addresses[j][2], float(distances))
                else:
                    graph_distances.add_edge(addresses[i][2], addresses[j][2], 0.0)
            j += 1
        i += 1

    
    return graph_distances


# Initializes the graph and populates distance csv data.
graph = get_graph("Data/distance.csv")

# trucks start at the hub and get the edge weights from teh graph which is the distances from locations in miles.
def greedy_path_algorithm(route, start):
    graph_edge_weights = graph.edge_weights

    if ('4001 South 700 East', '4001 South 700 East') in graph_edge_weights.keys():
        del graph_edge_weights[('4001 South 700 East', '4001 South 700 East')]  # This removes edge weights between same starting node.

    #if ('600 E 900 South', '3595 Main St') not in graph_edge_weights.keys():
        #graph_edge_weights.

    truck_route_to_sort = route  # this is a copy of the original route with packages loaded onto the truck. It will be modified as locations are added to the greedy path.
    greedy_path = [start]  # this is the greedy path that starts at the hub

    # loop to iterate until all locations in the 'truck route to sort' have been added to the greedy path.
    # the algorithm checks if an edge weight exists between the last location added to the greedy path and the current location.
    # Start is the current location and min represents the distances or edge weights starting at 0.
    # if the edge weight exists, the distance is assigned to the distance var and if not distance will get an infinite value.
    # if the distance is smaller than the minimum distance and not equal to 0, a new minimum is updated.
    # After iterating through all locations in 'truck route to sort' it checks if the minimum distance is present and if not appends it to the greedy path.
    # The loop continues until all locations are added and then returns to greedy path which is the better path to take.
    # For space, N represents the number of location in the route from the graph and the 'edge weights', 'greedy path' and 'truck route to sort' grows with the size of input O(n).
    # Inside the loop is a nested for loop that iterates the locations in 'truck route to sort' where (n) represents the number of locations in the route creating O(n^2) time complexity.
    while len(truck_route_to_sort) != 0:
        min = [0, start]
        for location in truck_route_to_sort:
            if (greedy_path[-1], location) in graph_edge_weights:
                distance = graph_edge_weights[greedy_path[-1], location]
            else:
                distance = float('inf')
            if min[0] == 0:
                min = [distance, location]
            if distance < min[0] and distance != 0:
                min = [distance, location]
        if min[1] not in greedy_path:
            greedy_path.append(min[1])
        truck_route_to_sort.remove(min[1])

    return greedy_path

