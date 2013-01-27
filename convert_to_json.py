#!/usr/bin/python

import os
import csv
import codecs


def convert_metadata():
    in_file = csv.reader(open('./data/r/metadata.csv', 'r'))
    out_file = open('./data/json/metadata.json', 'w')

    # convert to json objects
    json_objs = []
    for record in in_file:
        lat_str = record[4]
        # remind to remove the 2 last byte, because the degree symbol is utf
        lat_degr = float(lat_str.split(' ')[0][:-2])
        lat_min = float(lat_str.split(' ')[1][:-1]) * 1/60
        lat = lat_degr + lat_min

        lng_str = record[5]
        # remind to remove the 2 last byte, because the degree symbol is utf
        lng_degr = float(lng_str.split(' ')[0][:-2])
        lng_min = float(lng_str.split(' ')[1][:-1]) * 1/60
        lng = lng_degr + lng_min

        obj_str  = '  { \n'
        obj_str += '    "id": "' + record[0] + '",\n'
        obj_str += '    "province": "' + record[1] + '",\n'
        obj_str += '    "place name": "' + record[2] + '",\n'
        obj_str += '    "sealevel": "' + record[3] + '",\n'
        obj_str += '    "latitude": "' + str(lat) + '",\n'
        obj_str += '    "longitude": "' + str(lng) + '",\n'
        obj_str += '    "data_url": "' + record[6] + '",\n'
        obj_str += '    "measurements_url": "' + record[7] + '",\n'
        obj_str += '    "csv": "csv/' + record[8] + '",\n'
        obj_str += '    "svg": "diagram/' + record[8].split('.')[0] + '.svg",\n'
        obj_str += '    "climate_diagram": "diagram/' + record[8].split('.')[0] + '.png"\n'
        obj_str += '  }'
        json_objs.append(obj_str)

    # open the array
    out_file.write('[\n')

    # write the objects
    out_file.write(',\n'.join(json_objs))

    # close the array
    out_file.write(']\n')

convert_metadata()

"""
def convert_temperature():
    in_file = csv.reader(open('./data/r/metadata.csv', 'r'))
    out_file = open('./data/json/temperature.json', 'w')

    # convert to json objects
    json_objs = []
    for record in in_file:
        lat_str = record[4]
        # remind to remove the 2 last byte, because the degree symbol is utf
        lat_degr = float(lat_str.split(' ')[0][:-2])
        lat_min = float(lat_str.split(' ')[1][:-1]) * 1/60
        lat = lat_degr + lat_min

        lng_str = record[5]
        # remind to remove the 2 last byte, because the degree symbol is utf
        lng_degr = float(lng_str.split(' ')[0][:-2])
        lng_min = float(lng_str.split(' ')[1][:-1]) * 1/60
        lng = lng_degr + lng_min

        obj_str  = '  { \n'
        obj_str += '    "id": "' + record[0] + '",\n'
        obj_str += '    "province": "' + record[1] + '",\n'
        obj_str += '    "place name": "' + record[2] + '",\n'
        obj_str += '    "sealevel": "' + record[3] + '",\n'
        obj_str += '    "latitude": "' + str(lat) + '",\n'
        obj_str += '    "longitude": "' + str(lng) + '",\n'
        obj_str += '    "data_url": "' + record[6] + '",\n'
        obj_str += '    "measurements_url": "' + record[7] + '",\n'
        obj_str += '    "csv": "csv/' + record[8] + '",\n'
        obj_str += '    "svg": "diagram/' + record[8].split('.')[0] + '.svg",\n'
        obj_str += '    "climate_diagram": "diagram/' + record[8].split('.')[0] + '.png"\n'
        obj_str += '  }'
        json_objs.append(obj_str)

    # open the array
    out_file.write('[\n')

    # write the objects
    out_file.write(',\n'.join(json_objs))

    # close the array
    out_file.write(']\n')

convert_temperature()

def convert_special_days():
    in_file = csv.reader(open('./data/r/metadata.csv', 'r'))
    out_file = open('./data/json/special_days.json', 'w')

    # convert to json objects
    json_objs = []
    for record in in_file:
        lat_str = record[4]
        # remind to remove the 2 last byte, because the degree symbol is utf
        lat_degr = float(lat_str.split(' ')[0][:-2])
        lat_min = float(lat_str.split(' ')[1][:-1]) * 1/60
        lat = lat_degr + lat_min

        lng_str = record[5]
        # remind to remove the 2 last byte, because the degree symbol is utf
        lng_degr = float(lng_str.split(' ')[0][:-2])
        lng_min = float(lng_str.split(' ')[1][:-1]) * 1/60
        lng = lng_degr + lng_min

        obj_str  = '  { \n'
        obj_str += '    "id": "' + record[0] + '",\n'
        obj_str += '    "province": "' + record[1] + '",\n'
        obj_str += '    "place name": "' + record[2] + '",\n'
        obj_str += '    "sealevel": "' + record[3] + '",\n'
        obj_str += '    "latitude": "' + str(lat) + '",\n'
        obj_str += '    "longitude": "' + str(lng) + '",\n'
        obj_str += '    "data_url": "' + record[6] + '",\n'
        obj_str += '    "measurements_url": "' + record[7] + '",\n'
        obj_str += '    "csv": "csv/' + record[8] + '",\n'
        obj_str += '    "svg": "diagram/' + record[8].split('.')[0] + '.svg",\n'
        obj_str += '    "climate_diagram": "diagram/' + record[8].split('.')[0] + '.png"\n'
        obj_str += '  }'
        json_objs.append(obj_str)

    # open the array
    out_file.write('[\n')

    # write the objects
    out_file.write(',\n'.join(json_objs))

    # close the array
    out_file.write(']\n')

convert_special_days()

def convert_precepitation():
    in_file = csv.reader(open('./data/r/metadata.csv', 'r'))
    out_file = open('./data/json/precepitation.json', 'w')

    # convert to json objects
    json_objs = []
    for record in in_file:
        lat_str = record[4]
        # remind to remove the 2 last byte, because the degree symbol is utf
        lat_degr = float(lat_str.split(' ')[0][:-2])
        lat_min = float(lat_str.split(' ')[1][:-1]) * 1/60
        lat = lat_degr + lat_min

        lng_str = record[5]
        # remind to remove the 2 last byte, because the degree symbol is utf
        lng_degr = float(lng_str.split(' ')[0][:-2])
        lng_min = float(lng_str.split(' ')[1][:-1]) * 1/60
        lng = lng_degr + lng_min

        obj_str  = '  { \n'
        obj_str += '    "id": "' + record[0] + '",\n'
        obj_str += '    "province": "' + record[1] + '",\n'
        obj_str += '    "place name": "' + record[2] + '",\n'
        obj_str += '    "sealevel": "' + record[3] + '",\n'
        obj_str += '    "latitude": "' + str(lat) + '",\n'
        obj_str += '    "longitude": "' + str(lng) + '",\n'
        obj_str += '    "data_url": "' + record[6] + '",\n'
        obj_str += '    "measurements_url": "' + record[7] + '",\n'
        obj_str += '    "csv": "csv/' + record[8] + '",\n'
        obj_str += '    "svg": "diagram/' + record[8].split('.')[0] + '.svg",\n'
        obj_str += '    "climate_diagram": "diagram/' + record[8].split('.')[0] + '.png"\n'
        obj_str += '  }'
        json_objs.append(obj_str)

    # open the array
    out_file.write('[\n')

    # write the objects
    out_file.write(',\n'.join(json_objs))

    # close the array
    out_file.write(']\n')

convert_precipitation()

def convert_sun():
    in_file = csv.reader(open('./data/r/metadata.csv', 'r'))
    out_file = open('./data/json/sun.json', 'w')

    # convert to json objects
    json_objs = []
    for record in in_file:
        lat_str = record[4]
        # remind to remove the 2 last byte, because the degree symbol is utf
        lat_degr = float(lat_str.split(' ')[0][:-2])
        lat_min = float(lat_str.split(' ')[1][:-1]) * 1/60
        lat = lat_degr + lat_min

        lng_str = record[5]
        # remind to remove the 2 last byte, because the degree symbol is utf
        lng_degr = float(lng_str.split(' ')[0][:-2])
        lng_min = float(lng_str.split(' ')[1][:-1]) * 1/60
        lng = lng_degr + lng_min

        obj_str  = '  { \n'
        obj_str += '    "id": "' + record[0] + '",\n'
        obj_str += '    "province": "' + record[1] + '",\n'
        obj_str += '    "place name": "' + record[2] + '",\n'
        obj_str += '    "sealevel": "' + record[3] + '",\n'
        obj_str += '    "latitude": "' + str(lat) + '",\n'
        obj_str += '    "longitude": "' + str(lng) + '",\n'
        obj_str += '    "data_url": "' + record[6] + '",\n'
        obj_str += '    "measurements_url": "' + record[7] + '",\n'
        obj_str += '    "csv": "csv/' + record[8] + '",\n'
        obj_str += '    "svg": "diagram/' + record[8].split('.')[0] + '.svg",\n'
        obj_str += '    "climate_diagram": "diagram/' + record[8].split('.')[0] + '.png"\n'
        obj_str += '  }'
        json_objs.append(obj_str)

    # open the array
    out_file.write('[\n')

    # write the objects
    out_file.write(',\n'.join(json_objs))

    # close the array
    out_file.write(']\n')

convert_sun()

def convert_humidity():
    in_file = csv.reader(open('./data/r/metadata.csv', 'r'))
    out_file = open('./data/json/humidity.json', 'w')

    # convert to json objects
    json_objs = []
    for record in in_file:
        lat_str = record[4]
        # remind to remove the 2 last byte, because the degree symbol is utf
        lat_degr = float(lat_str.split(' ')[0][:-2])
        lat_min = float(lat_str.split(' ')[1][:-1]) * 1/60
        lat = lat_degr + lat_min

        lng_str = record[5]
        # remind to remove the 2 last byte, because the degree symbol is utf
        lng_degr = float(lng_str.split(' ')[0][:-2])
        lng_min = float(lng_str.split(' ')[1][:-1]) * 1/60
        lng = lng_degr + lng_min

        obj_str  = '  { \n'
        obj_str += '    "id": "' + record[0] + '",\n'
        obj_str += '    "province": "' + record[1] + '",\n'
        obj_str += '    "place name": "' + record[2] + '",\n'
        obj_str += '    "sealevel": "' + record[3] + '",\n'
        obj_str += '    "latitude": "' + str(lat) + '",\n'
        obj_str += '    "longitude": "' + str(lng) + '",\n'
        obj_str += '    "data_url": "' + record[6] + '",\n'
        obj_str += '    "measurements_url": "' + record[7] + '",\n'
        obj_str += '    "csv": "csv/' + record[8] + '",\n'
        obj_str += '    "svg": "diagram/' + record[8].split('.')[0] + '.svg",\n'
        obj_str += '    "climate_diagram": "diagram/' + record[8].split('.')[0] + '.png"\n'
        obj_str += '  }'
        json_objs.append(obj_str)

    # open the array
    out_file.write('[\n')

    # write the objects
    out_file.write(',\n'.join(json_objs))

    # close the array
    out_file.write(']\n')

convert_humidity()

def convert_snow_hail_storm():
    in_file = csv.reader(open('./data/r/metadata.csv', 'r'))
    out_file = open('./data/json/snow_hail_storm.json', 'w')

    # convert to json objects
    json_objs = []
    for record in in_file:
        lat_str = record[4]
        # remind to remove the 2 last byte, because the degree symbol is utf
        lat_degr = float(lat_str.split(' ')[0][:-2])
        lat_min = float(lat_str.split(' ')[1][:-1]) * 1/60
        lat = lat_degr + lat_min

        lng_str = record[5]
        # remind to remove the 2 last byte, because the degree symbol is utf
        lng_degr = float(lng_str.split(' ')[0][:-2])
        lng_min = float(lng_str.split(' ')[1][:-1]) * 1/60
        lng = lng_degr + lng_min

        obj_str  = '  { \n'
        obj_str += '    "id": "' + record[0] + '",\n'
        obj_str += '    "province": "' + record[1] + '",\n'
        obj_str += '    "place name": "' + record[2] + '",\n'
        obj_str += '    "sealevel": "' + record[3] + '",\n'
        obj_str += '    "latitude": "' + str(lat) + '",\n'
        obj_str += '    "longitude": "' + str(lng) + '",\n'
        obj_str += '    "data_url": "' + record[6] + '",\n'
        obj_str += '    "measurements_url": "' + record[7] + '",\n'
        obj_str += '    "csv": "csv/' + record[8] + '",\n'
        obj_str += '    "svg": "diagram/' + record[8].split('.')[0] + '.svg",\n'
        obj_str += '    "climate_diagram": "diagram/' + record[8].split('.')[0] + '.png"\n'
        obj_str += '  }'
        json_objs.append(obj_str)

    # open the array
    out_file.write('[\n')

    # write the objects
    out_file.write(',\n'.join(json_objs))

    # close the array
    out_file.write(']\n')

convert_snow_hail_storm()

def convert_wind():
    in_file = csv.reader(open('./data/r/metadata.csv', 'r'))
    out_file = open('./data/json/wind.json', 'w')

    # convert to json objects
    json_objs = []
    for record in in_file:
        lat_str = record[4]
        # remind to remove the 2 last byte, because the degree symbol is utf
        lat_degr = float(lat_str.split(' ')[0][:-2])
        lat_min = float(lat_str.split(' ')[1][:-1]) * 1/60
        lat = lat_degr + lat_min

        lng_str = record[5]
        # remind to remove the 2 last byte, because the degree symbol is utf
        lng_degr = float(lng_str.split(' ')[0][:-2])
        lng_min = float(lng_str.split(' ')[1][:-1]) * 1/60
        lng = lng_degr + lng_min

        obj_str  = '  { \n'
        obj_str += '    "id": "' + record[0] + '",\n'
        obj_str += '    "province": "' + record[1] + '",\n'
        obj_str += '    "place name": "' + record[2] + '",\n'
        obj_str += '    "sealevel": "' + record[3] + '",\n'
        obj_str += '    "latitude": "' + str(lat) + '",\n'
        obj_str += '    "longitude": "' + str(lng) + '",\n'
        obj_str += '    "data_url": "' + record[6] + '",\n'
        obj_str += '    "measurements_url": "' + record[7] + '",\n'
        obj_str += '    "csv": "csv/' + record[8] + '",\n'
        obj_str += '    "svg": "diagram/' + record[8].split('.')[0] + '.svg",\n'
        obj_str += '    "climate_diagram": "diagram/' + record[8].split('.')[0] + '.png"\n'
        obj_str += '  }'
        json_objs.append(obj_str)

    # open the array
    out_file.write('[\n')

    # write the objects
    out_file.write(',\n'.join(json_objs))

    # close the array
    out_file.write(']\n')

convert_wind()

def convert_wind_direction():
    in_file = csv.reader(open('./data/r/metadata.csv', 'r'))
    out_file = open('./data/json/wind_direction.json', 'w')

    # convert to json objects
    json_objs = []
    for record in in_file:
        lat_str = record[4]
        # remind to remove the 2 last byte, because the degree symbol is utf
        lat_degr = float(lat_str.split(' ')[0][:-2])
        lat_min = float(lat_str.split(' ')[1][:-1]) * 1/60
        lat = lat_degr + lat_min

        lng_str = record[5]
        # remind to remove the 2 last byte, because the degree symbol is utf
        lng_degr = float(lng_str.split(' ')[0][:-2])
        lng_min = float(lng_str.split(' ')[1][:-1]) * 1/60
        lng = lng_degr + lng_min

        obj_str  = '  { \n'
        obj_str += '    "id": "' + record[0] + '",\n'
        obj_str += '    "province": "' + record[1] + '",\n'
        obj_str += '    "place name": "' + record[2] + '",\n'
        obj_str += '    "sealevel": "' + record[3] + '",\n'
        obj_str += '    "latitude": "' + str(lat) + '",\n'
        obj_str += '    "longitude": "' + str(lng) + '",\n'
        obj_str += '    "data_url": "' + record[6] + '",\n'
        obj_str += '    "measurements_url": "' + record[7] + '",\n'
        obj_str += '    "csv": "csv/' + record[8] + '",\n'
        obj_str += '    "svg": "diagram/' + record[8].split('.')[0] + '.svg",\n'
        obj_str += '    "climate_diagram": "diagram/' + record[8].split('.')[0] + '.png"\n'
        obj_str += '  }'
        json_objs.append(obj_str)

    # open the array
    out_file.write('[\n')

    # write the objects
    out_file.write(',\n'.join(json_objs))

    # close the array
    out_file.write(']\n')

convert_wind_direction()
"""
