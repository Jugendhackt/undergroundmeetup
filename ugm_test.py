import numpy as np
import csv
from ugm_interface import findNamedMeetPoint, load_metro_data

data = load_metro_data('data.generated.csv')

locations = [ "A01", "A20" ]

print("Finding meeting point for:")
print(locations)
print("=> Meeting point: " + findNamedMeetPoint(data, locations))
