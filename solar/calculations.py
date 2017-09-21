import ephem
from ephem import cities


def look_up_coords(city_name):
    ven = cities.lookup(city_name)
    if not ven:
        return False
    return ven


def sun_rise(city_name):
    city = look_up_coords(city_name)
    if not city:
        pass
    print city
    sun_body = ephem.Sun()
    # observer = ephem.Observer()
    # observer.lat = city.lat
    # observer.lon = city.lon
    # observer.elevation = city.elevation

    return ephem.localtime(city.next_rising(sun_body))


def sun_set(city_name):
    city = look_up_coords(city_name)
    if not city:
        pass
    print city
    sun_body = ephem.Sun()
    # observer = ephem.Observer()
    # observer.lat = city.lat
    # observer.lon = city.lon
    # observer.elevation = city.elevation

    return ephem.localtime(city.next_setting(sun_body))
