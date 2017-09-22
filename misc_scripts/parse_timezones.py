import re
import chardet
import codecs


def parse_countries():
    with codecs.open("timeZones.txt", encoding="utf-8") as f:
        print f.readline()
        for line in f:
            place = re.split("\t", line.strip())
            if place[6] == 'P' and place[8] == 'NO':
                chardet.detect(place)
                # print ' '.join([l.decode("utf-8") for l in place])


def parse_timezones():
    with codecs.open("timeZones.txt", encoding="utf-8") as f:
        print f.readline()
        for line in f:
            print re.split("\t", f.readline().strip())


if __name__ == "__main__":
    parse_timezones()
