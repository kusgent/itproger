import time
import datetime as d
import sys, os, platform
from math import sqrt as s, ceil

time.sleep(1)
print("Hello!")

print(d.datetime.now().date())
print(d.datetime.now().date().month)
print(d.datetime.now().time())

print(sys.path)
print(os.name)
print(platform.system())

print(ceil(s(9)))
