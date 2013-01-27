#!/usr/bin/python

import os
import time
import csv
import urllib3
import re
import codecs

from BeautifulSoup import BeautifulSoup

from random import shuffle

def process_table(table, district, station_no, index):
    reversed = table[::-1]
    rotated = zip(*reversed[::-1])
    final = rotated
    writer = csv.writer(open('./data/csv/' + district + '_'+ station_no + '_' + csv_names[index] + '.csv', 'wb'))
    for rows in final:
        writer.writerow(rows)

def parse_tables(html, district, station_no):
    soup = BeautifulSoup(html)
    td_tags = soup.findAll('td')
    found_start = False
    cols_count = 0
    cols_in_line_count = 0
    table = []
    table_idx = -1

    for td in td_tags:
        content_str = td.string

        if content_str is None:
            continue

        if content_str == '&nbsp;':
            content_str = 'NA'

        if (content_str == start_marker): # found starting point of the measurment tables
            found_start = True
            cols_in_line_count = 0
            if (len(table) > 0):
                process_table(table, district, station_no, table_idx)
            table_idx = table_idx + 1
            table = []
            table.append([])
        else:
            cols_in_line_count = cols_in_line_count + 1

        if (content_str in line_markers):
            found_start = False
            cols_count = cols_in_line_count
            cols_in_line_count = 0
            table.append([])

        if (found_start or cols_in_line_count < cols_count):
            table[len(table)-1].append(content_str)
            cols_in_line_count = cols_in_line_count + 1

    if (len(table) > 0):
        process_table(table, district, station_no, table_idx)

def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

def remove_extra_spaces(data):
    p = re.compile(r'\s+')
    return p.sub(' ', data)

def parse_lat(html):
    soup = BeautifulSoup(html)
    tag = soup.find(text='geogr. Breite:')
    return tag.parent.findNext('td').string

def parse_lon(html):
    soup = BeautifulSoup(html)
    tag = soup.find(text=re.compile('geogr. L.*'))
    return tag.parent.findNext('td').string

def parse_station(html):
    soup = BeautifulSoup(html)
    tag = soup.find(text='Station:')
    with_garbage = remove_extra_spaces(remove_html_tags(`tag.findNext('td')`))
    with_garbage = with_garbage[::-1]
    idx = 0
    try:
        idx = with_garbage.index(">")
    except ValueError:
        idx = 0
    finally:
        without_garbage = with_garbage[0:idx]
    return without_garbage[::-1]

def parse_sea_level(html):
    soup = BeautifulSoup(html)
    tag = soup.find(text=re.compile('Seeh.*'))
    return tag.parent.findNext('td').string

def extract_measures(district, station_no):
    html_file = open("./data/raw/measurements/" + station_no + ".htm", "r")
    html = html_file.read()
    html_file.close()

    soup = BeautifulSoup(html)
    tr_tags = soup.findAll("tr")
    writer = csv.writer(open('./data/csv/' + district + '_' + station_no + '_0_measurements.csv', 'wb'))

    j = 0
    for tr in tr_tags:
        j = j + 1
        if j < 3:
            continue
        line = []
        td_tags = tr.findAll("td")
        for td in td_tags:
            value = td.string
            if (value is None):
                continue
            if value == "&nbsp;":
                value = ""
            line.append(value)
        writer.writerow(line)

def get_url(district, station_no):
    return 'http://www.zamg.ac.at/fix/klima/oe71-00/klima2000/daten/klimadaten/' + district + '/' + station_no + '.htm'

def get_measures_url(station_no):
    return "http://www.zamg.ac.at/fix/klima/oe71-00/klima2000/daten/Datenbestand/" + station_no + ".htm"

def walk(dir, result):
    dir = os.path.abspath(dir)
    for file in [file for file in os.listdir(dir) if not file in [".",".."]]:
        nfile = os.path.join(dir,file)
        if (nfile[-3:] == "htm"):
            result.append(nfile)
        if os.path.isdir(nfile):
            walk(nfile, result)


start_marker = 'Jan'
line_markers = ['Feb', 'Mar', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dez', 'Jahr']
csv_names = ['1_temperature', '2_special_days', '3_precipitation', '4_sun', '5_humidity', '6_snow_hail_storm', '7_wind', '8_wind_direction']

html_files = []
walk("./data/raw/climate", html_files)

overview_file = codecs.open("./data/metadata.csv", "w", "utf-8")

i = 0
for html_file in html_files:

    filename = ''.join(html_file.split('/')[-1:])
    station_no = filename.split('.')[0]
    district = ''.join(html_file.split('/')[-2])

    print "Processing station " + station_no + " in " + district + "..."

    print "  Loading page"
    source_file = open(html_file, "r")
    html = source_file.read()
    source_file.close()

    print "  Parsing station name"
    station_name = parse_station(html).strip()

    print "  Parsing sea level"
    sea_level = parse_sea_level(html)
    if (sea_level[-2:] == " m"):
      sea_level = sea_level[0:-2]

    print "  Parsing latitude"
    lat = parse_lat(html)

    print "  Parsing longitude"
    lon = parse_lon(html)

    print "  Parsing tables"
    parse_tables(html, district, station_no)

    print "  Processing measures"
    extract_measures(district, station_no)

    print "  Appending to overview"
    overview_file.write(station_no);
    overview_file.write(",")

    overview_file.write(district);
    overview_file.write(",")

    overview_file.write(station_name.decode("utf-8"))
    overview_file.write(",")

    overview_file.write(sea_level)
    overview_file.write(",")

    overview_file.write(lat)
    overview_file.write(",")

    overview_file.write(lon)
    overview_file.write(",")

    overview_file.write(get_url(district, station_no))
    overview_file.write(",")

    overview_file.write(get_measures_url(station_no))
    overview_file.write("\n")

overview_file.close()

