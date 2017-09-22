import re
import chardet
import codecs

import psycopg2


insert_timezone = """
    INSERT INTO world (
        country_code, timezone_id, gmt_offset_winter,
        dst_offset_summer, rawoffset
    )
    VALUES ({:s}, {:s}, {:f}, {:f}, {:f})
"""


def db_connect():
    conn = psycopg2.connect(dbname="world", user="axelbs")
    return conn


def parse_countries(db_conn):
    with codecs.open("timeZones.txt", encoding="utf-8") as f:
        for line in f:
            place = re.split("\t", line.strip())
            if place[6] == 'P' and place[8] == 'NO':
                chardet.detect(place)
                # print ' '.join([l.decode("utf-8") for l in place])


def parse_timezones(db_conn):
    cur = db_conn.cursor()
    print cur
    with codecs.open("timeZones.txt", encoding="utf-8") as f:
        print f.readline()
        for line in f:
            tz_info = re.split("\t", f.readline().strip())
            cur.execute(insert_timezone.format
                        (
                            tz_info[0], tz_info[1], tz_info[2],
                            tz_info[3], tz_info[4]
                        ))
    cur.commit()


if __name__ == "__main__":
    parse_timezones(db_connect())
