import numpy as np
import csv
from ugm_algorithms import findMeetPoint

def get_station_name(metro_data, station):
    return metro_data["station_names"][station]

def get_station_index(metro_data, station):
    return metro_data["station_names"].index(station)

def findNamedMeetPoint(metro_data, positions):
    return get_station_name(metro_data, int(findMeetPoint(metro_data["metro_data"],
        [x for x in map(lambda x: get_station_index(metro_data, x), positions)])))

def load_metro_data(filename):
    station_names = open('data.csv').readline().strip().split(";")
    metro_data = np.loadtxt(open("data.csv", "rb"), delimiter=";", skiprows=1).transpose(1,0)
    return { "station_names" : station_names, "metro_data" : metro_data }