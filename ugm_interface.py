import numpy as np
import csv
from ugm_algorithms import findMeetPoint


def get_station_name(metro_data, station):
    return metro_data["station_names"][station]


def get_station_names(metro_data, stations_list):
    return [[metro_data["station_names"][station]
            for station in stations] for stations in stations_list]


def get_station_index(metro_data, station):
    return metro_data["station_names"].index(station)


def findNamedMeetPoint(metro_data, positions):
    stations = [x for x in map(lambda x: get_station_index(metro_data, x),
                               positions)]
    meetpoint = findMeetPoint(metro_data["metro_data"], stations)
    return get_station_name(metro_data, meetpoint[0])


def findNamedMeetData(metro_data, positions):
    stations = [x for x in map(lambda x: get_station_index(metro_data, x),
                               positions)]
    meetpoint = findMeetPoint(metro_data["metro_data"], stations)
    return (get_station_name(metro_data, meetpoint[0]),
            dict(zip(
                positions,
                get_station_names(metro_data, meetpoint[1])
            )))


def load_metro_data(filename):
    station_names = open(filename).readline().strip().split(";")
    metro_data = np.loadtxt(open(filename, "r"),
                            delimiter=";", skiprows=1).transpose(1, 0)
    return {"station_names": station_names, "metro_data": metro_data}
