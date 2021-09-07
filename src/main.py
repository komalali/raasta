import os
from datetime import date
from munge import find_all_permits
from notify import send_dm

def main():
    found = find_all_permits()
    if len(found) > 0:
        today = date.today().strftime("%Y-%m-%d")
        msg = "FOUND PERMITS!\n"
        for key, val in found.items():
            for d, num in val.items():
                msg += f"{num} available in {key} zone on {d}\n"
        url = f"https://www.recreation.gov/permits/233273/registration/detailed-availability?date={today}"
        msg += f"GO GET THEM! {url}"
    else:
        msg = "No permits found :("
    print(msg)
    return msg


if __name__ == "__main__":
    main()
    