import time
import json

filename = "index.json"

class Garden: 
    #auto makes and intakes inputs for a dict
    def __init__(self):
        self.plants = {}
    
    def save_file(self, file):
        with open (filename, "w") as file:
            json.dumps(file)
    
    #inputs name and water logic into a dict
    def add_plant(self, plant, water_time):
        self.plants[plant] = {
            'water_time': water_time,
            'last_watered': time.time()
            }

    def get_choice(self):
        while True:
            choice = input("what do you want to do?").lower().strip()
            
            if choice in ["water", "add plant"]:
                return choice
            else:
                print("sorry, that isn't an option")
        
            

        

    
