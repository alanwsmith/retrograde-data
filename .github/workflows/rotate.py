#!/usr/bin/env python3

import json
import sys
import os
import time
import sys
import datetime

script_dir = sys.path[0]
data_dir = os.path.abspath(os.path.join(script_dir, "..", "..", "hourly"))
output_dir = os.path.abspath(os.path.join(script_dir, "..", "..", "current"))

planets = [
        'jupiter', 'mars', 'mercury', 'neptune', 
        'pluto', 'saturn', 'uranus', 'venus'
        ]

current_time = int(time.time())

print(f"Running process for: {current_time}")

for planet in planets:
    print(f"Processing planet: {planet}")
    with open(f"{data_dir}/{planet}.json") as _json:
        data = json.load(_json)
        state = None
        for hour in data["retrograde"]:
            if current_time > hour[0]:
                state = hour[1]
            else:
                with open(f"{output_dir}/{planet}.json", "w") as _out:
                    output_data = { 
                        "updated": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
                        "retrograde": state
                    }
                    json.dump(output_data, _out)
                break

