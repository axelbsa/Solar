import re
import chardet
import codecs


def parse():
    with codecs.open("allCountries.txt", encoding="utf-8") as f:
        print f.readline()
        for line in f:
            place = re.split("\t", line.strip())
            if place[6] == 'P' and place[8] == 'NO':
                chardet.detect(place)
                # print ' '.join([l.decode("utf-8") for l in place])


if __name__ == "__main__":
    parse()
