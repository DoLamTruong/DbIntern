import h3
def example(res):
    lat = 17.964874
    lng = 102.621389
    #   res = 1017.964874, 102.621389
    a = h3.geo_to_h3(lat, lng, res)
    return a
temp = example(9)
print(int(temp, base=16))
par = h3.h3_to_parent(temp, 8)
# print(h3.h3_to_parent(temp, 11)/h3.h3_to_parent(temp, 10))
print(par)
l = h3.h3_to_children(par, 9)
temp = "("
for i in l:
    temp += "'/x" + str(i) + "',"
# temp += ")"
last = """hi """
last += temp[:-1] + ")"
print(last) 
