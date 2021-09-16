import h3
import random


17.964874, 102.621389
result = "(17.964874, 102.621389,618764906283925503, 500002, TRUE)\n"
# Longstart, Longstop = 18.3, 20.69
# start, stop = 101.06 ,103.74
Longstart, Longstop = 17.953, 18.194
start, stop = 102.58 ,102.77
for i in range (1,200000):
    long = random.uniform(Longstart, Longstop)
    lat = random.uniform(start, stop)
    h = h3.geo_to_h3(long, lat, 9)
    result += ",(" + str(long) + ", " + str(lat) + "," + str(int(h, base=16)) + "," + str(i+300000) + ", TRUE)\n"
    # result += value
# print(result)
f = open("db3.txt", "a")
f.write(result)
f.close()