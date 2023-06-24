import random
import json
import string

city = ['Bengaluru', 'Chennai', 'Delhi', 'Goa', 'Kolkata', 'Pune', 'Mumbai']
json_data = {}

for i in city:
    for j in city:
        json_data[f"{i}->{j}"] = {
            "1a": random.randint(4000, 5000),
            "2a": random.randint(3000, 4000),
            "3e": random.randint(2000, 3000),
            "3a": random.randint(1500, 2000),
            "sl": random.randint(500, 1500),
            "2s": random.randint(100, 500),
        }

with open("data/railway_fares.json","w") as f:
    json.dump(json_data,f)

json_data = []
for i in range(25):
    for i in range(25):
        json_data.append(f"CNF {random.choice(string.ascii_uppercase)}-{i}")
    json_data.append(f"WL {random.randint(1, 50)}")

with open("data/seats.json","w") as f:
    json.dump(json_data,f)