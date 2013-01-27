#!/usr/bin/python

import os
import csv
import codecs

def create_summary(station_prefix):

    writer = csv.writer(open('./data/rstat/' + station_prefix + '_wl-data.csv', 'wb'))

    header = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    writer.writerow(header)

    percip_file = "./data/csv/" + station_prefix + "_3_precipitation.csv"
    percip_reader = csv.reader(open(percip_file, "rb"))
    percip_row_rsum = 2

    i = 0
    for row in percip_reader:
        i = i + 1
        if i == percip_row_rsum:
            values = row[0:12]
            values.insert(0, "rsum")
            writer.writerow(values)

            temp_file = "./data/csv/" + station_prefix + "_1_temperature.csv"
            temp_reader = csv.reader(open(temp_file, "rb"))
            temp_row_mtmax = 3
            temp_row_mtmin = 4
            temp_row_tmin = 6

            i = 0

            for row in temp_reader:
                i = i + 1
                if i == temp_row_mtmax:
                    values = row[0:12]
                    values.insert(0, "mtmax")
                    writer.writerow(values)


            temp_reader = csv.reader(open(temp_file, "rb"))

            i = 0
            for row in temp_reader:
                i = i + 1
                if i == temp_row_mtmin:
                    values = row[0:12]
                    values.insert(0, "mtmin")
                    writer.writerow(values)

            temp_reader = csv.reader(open(temp_file, "rb"))

            i = 0
            for row in temp_reader:
                i = i + 1
                if i == temp_row_tmin:
                    values = row[0:12]
                    values.insert(0, "tmin")
                    writer.writerow(values)


datadir = "./data/csv/"
files = os.listdir(datadir)
files.sort()

stations = []

for filename in files:
    file_name_parts = filename.split("_")

    if len(file_name_parts) < 3:
        continue

    district = file_name_parts[0]
    station_no = file_name_parts[1]
    station_prefix = district + "_" + station_no

    if not station_prefix in stations:
        stations.append(station_prefix)

for station_prefix in stations:
    create_summary(station_prefix)

meta_in = open("./data/metadata.csv", "rb")
meta_re = csv.reader(meta_in)

meta_out = open("./data/r/metadata.csv", "wb")
meta_wr = csv.writer(meta_out)

for row in meta_re:
    row.append(row[1] + "_" + row[0] + "_wl-data.csv")
    meta_wr.writerow(row)
    print "  created " + row[1] + "_" + row[0] + "_wl-data.csv"
