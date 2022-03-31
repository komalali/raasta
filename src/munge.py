import requests
from fake_useragent import UserAgent
from datetime import datetime, date
from dataclasses import dataclass

headers = {
    "User-Agent": UserAgent().random,
    "accept": "application/json",
}

@dataclass
class Zone:
    name: str
    id: int

zones = [
    Zone(name="Core Enchantments", id=30),
    Zone(name="Snow Lake", id=23),
    Zone(name="Colchuck Lake", id=29)
]

def get_zone_data_from_payload(payload, zone: Zone):
    try:
        return payload[str(zone.id)]["date_availability"]
    except KeyError:
        return {}

def get_availability(data):
    today = date.today()

    found = {}
    if len(data) == 0:
        return found
    for key, val in data.items():
        if val["remaining"] > 0:
            day = key.split("T")[0]
            if datetime.strptime(day, "%Y-%m-%d").date() >= today:
                found[day] = val["remaining"]
    
    return found

def find_permits_in_zone(payload, zone: Zone):
    zone_data = get_zone_data_from_payload(payload, zone)
    return get_availability(zone_data)

def find_permits(payload):
    found = {}
    for zone in zones:
        found_in_zone = find_permits_in_zone(payload, zone)
        if len(found_in_zone) > 0:
            found[zone.name] = found_in_zone
    return found

def find_all_permits():
    current_month = date.today().strftime("%m")
    i = int(current_month)
    found = {}
    while i <= 10:
        r = requests.get(f"https://www.recreation.gov/api/permits/233273/availability/month?start_date=2022-{current_month}-01T00:00:00.000Z&commercial_acct=false&is_lottery=false", headers=headers)
        payload = r.json()["payload"]["availability"]
        permits_for_month = find_permits(payload)
        if len(permits_for_month) > 0:
            for key in permits_for_month:
                if key not in found:
                    found[key] = {}
                found[key].update(permits_for_month[key])
        i += 1
    return found
