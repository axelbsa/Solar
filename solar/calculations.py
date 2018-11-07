import ephem
from ephem import cities

from db import Geoname
from sqlalchemy import func, desc


def look_up_coords(city_name):
    ven = cities.lookup(city_name)
    if not ven:
        return False
    return ven


def look_up_coords_from_db(city_name):
    # properties = Geoname.query.filter_by(name='london').first()
    #properties = Geoname.query.filter(
    #    func.lower(Geoname.name) == func.lower(city_name)
    #)

    properties = Geoname.query.filter(
        func.lower(Geoname.name) == func.lower(city_name)
    ).order_by(
        desc(Geoname.population)
    ).order_by(
        desc(Geoname.feature_code)
    ).all()

    if properties and len(properties) > 0:
        return properties[0]

    return None


def sun_rise(city_name):
    city = look_up_coords_from_db(city_name)
    if not city:
        return False
    sun_body = ephem.Sun()

    observer = ephem.Observer()
    observer.lat = str(city.latitude)
    observer.lon = str(city.longitude)
    observer.elevation = float(10.0)
    return ephem.localtime(observer.next_rising(sun_body))


def sun_set(city_name):
    city = look_up_coords_from_db(city_name)
    if not city:
        return False
    sun_body = ephem.Sun()

    observer = ephem.Observer()
    observer.lat = str(city.latitude)
    observer.lon = str(city.longitude)
    observer.elevation = float(10.0)
    return ephem.localtime(observer.next_setting(sun_body))
