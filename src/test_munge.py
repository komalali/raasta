import json
from munge import find_permits, find_permits_in_zone, zones

expected = {
    "2021-08-02": 2,
    "2021-08-21": 1,
    "2021-08-30": 2,
}

with open("test/data.json") as f:
    fake_data = json.load(f)
    found_in_zone = find_permits_in_zone(fake_data, zones[0])
    assert(expected == found_in_zone)
    print("Test passed!")

    found_total = find_permits(fake_data)
    assert(found_total == { "Core Enchantments": expected })
    print("Test passed!")

