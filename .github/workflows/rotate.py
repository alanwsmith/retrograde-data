#!/usr/bin/env python3

import json
import sys
import os
import time
import sys

script_dir = sys.path[0]
json_dir = os.path.join(script_dir, "..", "..", "hourly")
current_dir = os.path.join(script_dir, "..", "..", "current")

planets = [
        'jupiter', 'mars', 'mercury', 'neptune', 
        'pluto', 'saturn', 'uranus', 'venus'
        ]

current_time = int(time.time())

for planet in planets:
    json_path = os.path.join(json_dir, f"{planet}.json")
    output_path = os.path.join(current_dir, f"{planet}.json")
    with open(json_path) as _json:
        data = json.load(_json)
        state = None
        for hour in data["retrograde"]:
            if current_time > hour[0]:
                state = hour[1]
            else:
                with open(output_path, "w") as _out:
                    output_data = { "retrograde": state }
                    json.dump(output_data, _out)
                break














