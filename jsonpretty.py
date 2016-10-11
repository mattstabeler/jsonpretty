#!/usr/local/bin/python

import json

import sys
lines = sys.stdin.readlines()

lines = "\r".join(lines)

data = json.loads(lines)


print json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
