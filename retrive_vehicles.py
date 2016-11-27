#!/usr/bin/python

# This script retrieves vehicle location data form the raw historical data
#   input: <date>-vehicle.txt
#   output: rows of vehicle locations (json objects)
#
# Input file generated by
# [1]+  Done                    grep vehicle 2016.11.08.txt > 2016.11.08-vehicle.txt
# ouyang@Jiannans-MacBook-Air:/Volumes/Ouyang HD/projects/busgazer/161108$ du -h *
# 494M    2016.11.08-vehicle.txt
#  18G    2016.11.08.txt

import json
import io
import sys


def main():
  if len(sys.argv) < 2:
    print "Error: no input file given"
    print "Usage: %s <date>-vehicle.txt" % sys.argv[0]
    return

  input_fname = sys.argv[1]
  with open(input_fname) as data_file:    
    for line in data_file:
      get_vehicle_resp = json.loads(line)
      vehicles = get_vehicle_resp[u'bustime-response'][u'vehicle']
      for v in vehicles:
        print json.dumps(v)


if __name__ == "__main__":
    main()
