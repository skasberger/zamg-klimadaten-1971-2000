#!/usr/bin/python

import sys
sys.path.append('/usr/share/pyshared/requests/packages')

from urllib3 import HTTPConnectionPool
import re

host = 'www.zamg.ac.at'
url = '/fix/klima/oe71-00/klima2000/diverses/daten.htm'

stat_nr_string_exp = 'var astrStatNr = new Array\((.*?)\)'
cont_string_exp = 'var astrCont = new Array\((.*?)\)'

def get_js_arr_str(expr, data, group = 1):
    m = re.search(expr, data)
    return m.group(group)

def rm_quotes(data):
    p = re.compile(r'\'')
    return p.sub('', data).strip()

def arr_filter(item):
    return (item != ''and item != ',')

pool = HTTPConnectionPool(host)
r = pool.urlopen('GET', url)
html = r.data

stat_nr_str = get_js_arr_str(stat_nr_string_exp, html)
stat_nr = filter(arr_filter, map(rm_quotes, stat_nr_str.split('\'')))

cont_str = get_js_arr_str(cont_string_exp, html)
cont = filter(arr_filter, map(rm_quotes, cont_str.split('\'')))

url_file = open("./data/raw/url_climate.txt", "w")

i = 0
for station in stat_nr:
    data_url = 'http://www.zamg.ac.at/fix/klima/oe71-00/klima2000/daten/klimadaten/' + cont[i] + '/' + station + '.htm'
    i = i + 1
    url_file.write(data_url + "\n")

url_file.close() # close the file handle


url_file = open("./data/raw/url_measurements.txt", "w")

for station in stat_nr:
    data_url = "http://www.zamg.ac.at/fix/klima/oe71-00/klima2000/daten/Datenbestand/" + station + ".htm"
    url_file.write(data_url + "\n")

url_file.close() # close the file handle
