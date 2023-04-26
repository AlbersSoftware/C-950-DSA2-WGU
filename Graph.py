import csv


class Graph:

    # Constructor creating empty lists for the locations and edge weights
    def __init__(self):
        self.delivery_dict = {}  # has the same function of an adjacency list
        self.edge_weights = {}

    # Adds a vertex to the graph
    def add_vertex(self, vertex, address):
        self.delivery_dict[vertex] = address  # creates a dictionary with the street address as the key

    # Adds an undirected edge between vertices. Weight is equivalent to miles
    def add_edge(self, vertex_a, vertex_b, weight=1.0):
        self.edge_weights[(vertex_a, vertex_b)] = weight  # creates a dict where key : value == vertices : miles

    # Associates each package with its corresponding vertex on the graph
    # O(N^2)
    def put_packages_in_delivery_dict(self, packages):
        for package in packages:
            vertex = package.destination
            if vertex not in self.delivery_dict:
                self.add_vertex(vertex)
            self.delivery_dict[vertex].append(package)


# This function grabs the entire distance csv file.
# This is needed in order to create edges between vertex_a and vertex_b
# O(N)
def get_all_distance_csv_data(filename):
    csv_data = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            csv_data.append(row)
    return csv_data

def get_all_address_csv_data(filename):
    csv_data = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            csv_data.append(row)
    return csv_data

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

# This function creates the graph
# O(N^2)
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

    '''i = 0
    for row in data:
        graph_distances.add_vertex(row[0], addresses[i])  # Vertex is associated with the street address
        i += 1
    for row in data:
        for i in range(3, len(row)):  # Starts at 3 because indices 0-2 are name, street, and zip, which are not needed
         if row[i] != '':
           graph_distances.add_edge(row[1], data[i-3][1], float(row[i]))  # data[i-3][1] gets each connected street vertex'''
    return graph_distances


# Initialize the graph for further use
graph = get_graph("Data/distance.csv")


def greedy_path_algorithm(route):
    start = "4001 South 700 East"  # all trucks start their deliveries at the hub
    graph_edge_weights = graph.edge_weights  # get the edge weights from the graph

    if ('4001 South 700 East', '4001 South 700 East') in graph_edge_weights.keys():
        del graph_edge_weights[('4001 South 700 East', '4001 South 700 East')]  # remove edge weight between same node

    #if ('600 E 900 South', '3595 Main St') not in graph_edge_weights.keys():
        #graph_edge_weights.

    truck_route_to_sort = route  # this is the route created initially as packages were loaded to the truck
    greedy_path = [start]  # the greedy_path will be the better route to take, starting at the hub

    # using a while loop because the truck_route_to_sort will have
    # locations removed as they are added to the greedy_path
    while len(truck_route_to_sort) != 0:
        min = [0, start]  # "0" is the edge weight and "start" is the address, which will change throughout the loop
        for location in truck_route_to_sort:
            if (greedy_path[-1], location) in graph_edge_weights:
                distance = graph_edge_weights[greedy_path[-1], location]
            else:
                distance = float('inf')
            if min[0] == 0:  # helps establish starting location as well as self-loops to the same location
                min = [distance, location]
            if distance < min[0] and distance != 0:
                min = [distance, location]
        if min[1] not in greedy_path:  # eliminates double visits to the same place
            greedy_path.append(min[1])
        truck_route_to_sort.remove(min[1])  # removes the location and repeat the while loop until empty

    # This is the better route for the truck to take
    return greedy_path

