#!/usr/bin/env python3

import json
import sys
import os
import time
import sys

# script_dir = sys.path[0]
# json_dir = os.path.join(script_dir, "..", "..", "hourly")
# current_dir = os.path.join(script_dir, "..", "..", "current")

# script_dir = sys.path[0]
json_dir = os.path.join("hourly")
current_dir = os.path.join("current")

planets = [
        'jupiter', 'mars', 'mercury', 'neptune', 
        'pluto', 'saturn', 'uranus', 'venus'
        ]

current_time = int(time.time())

print(current_time)

with open('here-2.txt', 'w') as _ot2:
    _ot2.write('here is the thing for the test')

for planet in planets:
    print(planet)
    with open(f"hourly/{planet}.json") as _json:
        print("file is open")
        data = json.load(_json)
        state = None
        for hour in data["retrograde"]:
            if current_time > hour[0]:
                state = hour[1]
            else:
                with open(f"current/{planet}.json", "w") as _out:
                    print("writing out")
                    output_data = { "retrograde": state }
                    json.dump(output_data, _out)
                break














