import requests
import json
import csv

"""
Videó: https://youtu.be/B1v4aE4_O3A
Patreon: https://patreon.com/vault1337
Google Maps Distance Matrix API: https://developers.google.com/maps/documentation/distance-matrix/overview
"""

api_key = "IDE_ÍRD_BE_A_SAJÁT_API_KULCSOD"

origin = "Vault 1337"

with open("destinations.csv", "wt", encoding="windows-1250", newline="\n") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    with open("distance/locations.txt", "rt", encoding="utf-8") as destinations:
        for destination in destinations:
            url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination}&key={api_key}"

            payload={}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            distance = json.loads(response.text)
            if distance["rows"][0]["elements"][0]["status"] == "OK":
                actual_destination = distance["destination_addresses"][0]
                actual_distance = distance["rows"][0]["elements"][0]["distance"]["value"]
                writer.writerow([actual_destination, actual_distance])
            else:
                print(f"Nem tudjuk, merre van {destination}")