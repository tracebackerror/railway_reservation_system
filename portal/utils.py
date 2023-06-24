import json
import random

railway_fares = None
with open("data/railway_fares.json") as f:
    railway_fares = json.load(f)

seats = None
with open("data/seats.json") as f:
    seats = json.load(f)

train = None
with open("data/train.json") as f:
    train = json.load(f)

def getRailwayRates(_from, to, classs):
    key = f"{_from}->{to}"
    rate = railway_fares[key][classs]
    return rate

def getSeat():
    return random.choice(seats)

def getTrainData():
    return train