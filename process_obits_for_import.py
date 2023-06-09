import xml.etree.ElementTree as ET
import os
import csv

# split casket obituary spreadsheet into xml files
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'casket_obituaries.csv')
c = 0
with open(filename, "r") as obit_file:
    obit_reader = csv.reader(obit_file)
    for obit in obit_reader:
        # get title, first name, middle name, last name, and maiden name
        if obit[3].__len__() > 0:
            middle = ' ' + obit[3] + ' '
        else:
            middle = ' '
        if obit[6].__len__() > 0:
            maiden = '(' + obit[6] + ') '
        else:
            maiden = ''
        # makes name element and titleInfo_title element
        name = """<titleInfo>
        <title>""" + obit[4] + ' ' + obit[2] + middle + maiden + obit[1] + """</title>
    </titleInfo>
    <name>""" + obit[4] + ' ' + obit[2] + middle + maiden + obit[1] +"""</name>
    """

        if obit[5].__len__() > 0:
            rel_name = """<religious_name>""" + obit[5] + """</religious_name>
    """
        else:
            rel_name = """"""

        if obit[7].__len__() > 0:
            affiliation = """<affiliation>""" + obit[7].replace('&', 'and') + """</affiliation>
    """
        else:
            affiliation = """"""

        if obit[8].__len__() > 0:
            bplace = """<birth_place>""" + obit[8].replace('&', 'and') + """</birth_place>
    """
        else:
            bplace = """"""

        if obit[9].__len__() != 0 and obit[9].__len__() > 3:
            bdate = """<birth>""" + obit[9].strip() + """</birth>
    """
        else:
            bdate = """"""

        if obit[10].__len__() > 0:
            dplace = """<death_place>""" + obit[10].replace('&', 'and') + """</death_place>
    """
        else:
            dplace = """"""

        if obit[11].__len__() > 0:
            ddate = """<death>""" + obit[11].strip() + """</death>
    """
        else:
            ddate = """"""

        if obit[12].__len__() > 0:
            age = """<age>""" + obit[12] + """</age>
    """
        else:
            age = """"""

        if obit[13].__len__() > 0:
            year = """<casket_year>""" + obit[13] + """</casket_year>
    """
        else:
            year = """"""

        if obit[14].__len__() > 0:
            vol = """<casket_vol>""" + obit[14].replace('&', 'and') + """</casket_vol>
    """
        else:
            vol = """"""

        if obit[15].__len__() > 0:
            iss = """<casket_issue>""" + obit[15].replace('&', 'and') + """</casket_issue>
    """
        else:
            iss = """"""

        if obit[16].__len__() > 0:
            page = """<casket_page>""" + obit[16].replace('&', 'and') + """</casket_page>
    """
        else:
            page = """"""

        if obit[17].__len__() > 0:
            date = """<obit_date>""" + obit[17] + """</obit_date>
    """
        else:
            date = """"""

        if obit[18].__len__() > 0:
            spouse = """<spouse>""" + obit[18].replace('&', 'and') + """</spouse>
    """
        else:
            spouse = """"""

        if obit[19].__len__() > 0:
            spouse_death = """<spouse_death>""" + obit[19].replace('&', 'and') + """</spouse_death>
    """
        else:
            spouse_death = """"""

        if obit[20].__len__() > 0:
            father = """<father>""" + obit[20].replace('&', 'and') + """</father>
    """
        else:
            father = """"""

        if obit[21].__len__() > 0:
            father_town = """<father_town>""" + obit[21].replace('&', 'and') + """</father_town>
    """
        else:
            father_town = """"""

        if obit[22].__len__() > 0:
            mother = """<mother>""" + obit[22].replace('&', 'and') + """</mother>
    """
        else:
            mother = """"""

        if obit[23].__len__() > 0:
            mother_town= """<mother_town>""" + obit[23].replace('&', 'and') + """</mother_town>
    """
        else:
            mother_town = """"""

        if obit[24].__len__() > 0:
            sibs = """<siblings>""" + obit[24].replace('&', 'and') + """</siblings>
    """
        else:
            sibs = """"""

        if obit[25].__len__() > 0:
            other = """<other_relations>""" + obit[25].replace('&', 'and') + """</other_relations>
    """
        else:
            other = """"""

        if obit[26].__len__() > 0:
            notes = """<notes>""" + obit[26].replace('&', 'and') + """</notes>
    """
        else:
            notes = """"""
        # string of xml file text
        xml = """<?xml version="1.0" encoding="UTF-8"?>
<mods xmlns="http://www.loc.gov/mods/v3" xmlns:mods="http://www.loc.gov/mods/v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xlink="http://www.w3.org/1999/xlink">
    <identifier>"""+obit[0]+"""</identifier>
    """ \
    +name \
    + rel_name \
    + affiliation \
    + bplace \
    + bdate \
    + dplace \
        + ddate \
        + age \
        + year + vol + iss + page + date \
        + spouse \
        + spouse_death \
        + mother \
        + mother_town \
        + father \
        + father_town \
        + sibs \
        + other \
        + notes 
        # remove final indent
        xml = xml[:-5]
        # add constant elements
        constants = """
    <physicalDescription>
        <form authority="marcform">microform</form>
    </physicalDescription>
    <location>
        <physicalLocation>Located in the Microform Room, Angus L. Macdonald Library.</physicalLocation>
    </location>
</mods>"""
        xml = xml + constants
        # obituary identifier is the xml file name
        idd = obit[0]
        xml_file_name = idd + ".xml"
        # i would also check any syntax errors here, however you choose
        # write xml file to directory
        f = open(os.path.join(dirname, "islandora_import", xml_file_name), "w")
        f.write(xml)
        f.close()
        c += 1
