import csv
import re
import chardet
import codecs
import sys
csv.field_size_limit(sys.maxsize - 1)

import psycopg2
from psycopg2 import sql

insert_timezone = """
    INSERT INTO timezone (
        country_code, timezone_id, gmt_offset_winter,
        dst_offset_summer, rawoffset
    )
    VALUES ('{:s}', '{:s}', '{:f}', '{:f}', '{:f}')
"""

insert_geoname = """
    INSERT INTO geoname (
        geonameid, name, asciiname, alternatenames, latitude, longitude,
        feature_class, feature_code, country_code, population, elevation,
        timezone_id
    )
    VALUES (
    %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s
    )
"""


def db_connect():
    conn = psycopg2.connect(dbname="world", user="axelbs")
    return conn


def parse_countries(db_conn):
    cur = db_conn.cursor()
    accepted_regions = ["PPLA", "PPLA2", "PPLA3", "PPLA4", "PPLC"]
    for x in xrange(1, 5):
        filenames = "allCountries_{}.txt".format(x)
        with open(filenames) as f:
            spamreader = csv.reader(f, delimiter='\t', quotechar='|')
            print "Reading filename:{}".format(filenames)
            for row in spamreader:
                # 10291158, Oceanic Khorfakkan Resort and Spa, Oceanic Khorfakkan Resort and Spa, , 25.37166, 56.34921, S, HTL, AE, , 06, , , , 0, , 1, Asia/Dubai, 2015-05-27
                try:
                    geonameid = int(row[0])
                    name_utf = row[1]
                    asciiname = row[2]
                    alternatenames = row[3]
                    latitude = float(row[4])
                    longitude = float(row[5])
                    feature_class = row[6]
                    feature_code = row[7]
                    country_code = row[8]
                    alt_country_code = row[9]
                    admin1_code = row[10]
                    admin2_code = row[11]
                    admin3_code = row[12]
                    admin4_code = row[13]
                    population = int(row[14]) if row[14] else 0
                    elevation = int(row[15]) if row[15] else 0
                    dig_elevation = row[16]  # digital elevation model, srtm3 or gtopo30, average elevation of 3''x3'' (ca 90mx90m) or 30''x30'' (ca 900mx900m) area in meters, integer. srtm processed by cgiar/ciat.
                    timezone = row[17]
                    modification_date = row[18]
                    if ((feature_class == 'P' and feature_code in accepted_regions) or
                            feature_class == 'P' and country_code == 'NO' and feature_code == "PPL"):
                        cur.execute(insert_geoname,
                            (geonameid, name_utf, asciiname, alternatenames, latitude, longitude,
                            feature_class, feature_code, country_code, population, elevation, timezone)
                        )
                except Exception as e:
                    print e
                    print "pop:{} pop_type:{}, elevation:{} ele_type:{}".format(population, type(population), elevation, type(elevation))
                    print row
                    break
        db_conn.commit()
    return
    for line in f:
        place = re.split("\t", line.strip())
        if place[6] == 'P' and place[8] == 'NO':
            chardet.detect(place)
            # print ' '.join([l.decode("utf-8") for l in place])


def parse_timezones(db_conn):
    cur = db_conn.cursor()
    with codecs.open("timeZones.txt", encoding="utf-8") as f:
        print f.readline()
        for line in f:
            tz_info = re.split("\t", f.readline().strip())
            cur.execute(insert_timezone.format
                        (
                            tz_info[0], tz_info[1], float(tz_info[2]),
                            float(tz_info[3]), float(tz_info[4])
                        ))
    db_conn.commit()


if __name__ == "__main__":
    parse_countries(db_connect())
    # parse_timezones(db_connect())
