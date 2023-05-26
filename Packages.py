from datetime import datetime
from typing import List




# initilize the package fields
class Package:
    def __init__(self, ID, destination, city, state, Zip, deadline, weight, notes, status):
        super().__init__()
        self.ID = ID
        self.destination = destination
        self.city = city
        self.state = state
        self.Zip = Zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = "Loaded"




    def __str__(self):
        return f"{self.ID}, {self.destination}, {self.city}, {self.state}, {self.Zip}, {self.deadline}, {self.weight}, {self.notes}, {self.status}"
# update status to on truck
    def load_to_truck(self, truck_id):
        self.status = f"On Truck {truck_id}"



