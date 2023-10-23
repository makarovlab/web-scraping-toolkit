import re

def has_latitude(text: str) -> bool:
    has_latitude = False
    matched_latitudes = re.findall(r"-?(?<!\d)\d{,2}(?<=\d)\.\d{,20}", text)

    if any([float(lat) >= -90 and float(lat) <= 90 for lat in  matched_latitudes]):
        has_latitude = True

    return has_latitude


def has_longitude(text: str) -> bool:
    has_latitude = False
    matched_latitudes = re.findall(r"-?(?<!\d)\d{,3}(?<=\d)\.\d{,20}", text)

    if any([float(lat) >= -180 and float(lat) <= 180 for lat in  matched_latitudes]):
        has_latitude = True

    return has_latitude


def has_coordinates(text: str) -> bool:
    has_lat = has_latitude(text)
    has_lon = has_longitude(text)

    if has_lat and has_lon:
        return True
    else:
        return False