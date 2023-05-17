import xml.etree.ElementTree as ET
import os
from shutil import copyfile
import csv
import sys
from xml.sax.saxutils import escape

test = ""

dirname = os.path.dirname(__file__)

# checking for obits with missing name information
filename = os.path.join(dirname, 'casket_obituaries.csv')
c = 0
with open(filename, "r") as obit_file:
    obit_reader = csv.reader(obit_file)
    for obit in obit_reader:
        if (int(len(obit[1]) < 2) + int(len(obit[2]) < 2) + int(len(obit[4]) < 2) + int(len(obit[3]) < 1) + int("nknown" in ''.join([obit[1], obit[2], obit[3], obit[4]]))) >= 3 and obit[4] != "Sister":
            print(obit[0], obit[4], obit[2], obit[1])
            c += 1
print(c)

# figuring out indices of obit elements
idfile = '/Users/sarahmacdonald/work/islandora_import/﻿ID.xml'
c = 0
repofile = os.path.join(dirname, 'stfx_casketobits.csv')
with open(repofile, 'r') as repo_file:
    repo = csv.reader(repo_file)
    idtree = ET.parse(idfile)
    idt = idtree.iter()
    idtt = []
    for x in idt:
        idtt.append(x.tag.replace('{http://www.loc.gov/mods/v3}', ''))
    # list of indices of obit data
    indices = []
    for o in repo:
        if c == 0 and o != ['/']:
            for i in o:
                newi = str(i).replace('mods_', '').replace('_mt', '')
                if '.' in newi:
                    newi = newi.split('.')[-1]
                if newi in idtt:
                    indices.append(c)
                c += 1
repo_file.close()

# new obit data with only obit data from islandora and not other fields
c = 0
new_data = os.path.join(dirname, 'new_obits_data.csv')
with open(new_data, 'w') as new_obits:
    obit_writer = csv.writer(new_obits)
    with open(repofile, 'r') as repo_file:
        repo = csv.reader(repo_file)
        for i in repo:
            newrow = []
            for ii in indices:
                newrow.append(i[ii])
            if c == 0:
                indice_titles = newrow
                c += 1
            obit_writer.writerow(newrow)
repo_file.close()
new_obits.close()

# check that every identifier from the casket obits spreadsheet is present in islandora
print(indice_titles.index('dc.identifier'))
missing_ids = 0
with open(new_data, 'r') as cool_datas:
    cool_data = csv.reader(cool_datas)
    new_cool_data = []
    for x in cool_data:
        new_cool_data.append(x[19].split(',')[-1])
    print(new_cool_data)
    with open(filename, 'r') as orig_datas:
        orig_data = csv.reader(orig_datas)
        # checking for missing identifiers
        for i in orig_data:
            if i[0] not in new_cool_data:
                missing_ids += 1
        # checking for duplicates
        new_new_cool_data = []
        for obit_id in new_cool_data:
            if new_cool_data not in new_new_cool_data:
                new_new_cool_data.append(obit_id)
            else:
                print(obit_id)
print(missing_ids)