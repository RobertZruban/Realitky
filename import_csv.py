import csv
import pandas as pd 
df = pd.read_csv(r'C:\Users\roboz.DESKTOP-F86F289\Desktop\Python\Final_scrapers\Location_centrum_csv.csv') 

from math import radians, cos, sin, asin, sqrt

def haversine(coordinates1, coordinates2):
    i = -1 
    for x in coordinates1:
        i = i+1

        lon1 = float(17.112676)
        lat1 = float(48.144842)
        lon2 = coordinates1[i]
        lat2 = coordinates2[i]
        #Change to radians
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])


        # Apply the harversine formula
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 3956
        miles_to_km = 1.609344
        total = c * r * miles_to_km
        distance_from_centre.append(total)
        
distance_from_centre = []
df["longitude"] = pd.to_numeric(df['longitude'],errors='coerce')
df["latitude"] = pd.to_numeric(df['latitude'],errors='coerce')
haversine(df["longitude"], df["latitude"])
distance_from_centre
df['distance_from_centre'] = distance_from_centre





