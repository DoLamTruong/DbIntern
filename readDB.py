import psycopg2
import time
import h3
longtitude = 11.15
latitude = 104.77


def queryVal(res, h):
    if (res == 9):
        return "('x" + str(h) + "')" , res -1

    par = h3.h3_to_parent(h, res -1)
    l = h3.h3_to_children(par, 9)
    temp = "("
    for i in l:
        temp += "'/x" + str(i) + "',"
    return temp[:-1] + ")" , res-1


conn = psycopg2.connect(
    host="localhost",
    port = 5432,
    database="demo",
    user="root",
    password="root")
cur = conn.cursor()



def run(longtitude, latitude):
    begin = time.time() 
    # ==========================================
    resolution = 9
    h = h3.geo_to_h3(longtitude, latitude, resolution)
    query_results = []
    while (len(query_results)<5):
        val, resolution = queryVal(resolution, h)
        querystr = """select driverid from driverlocation
        where h3index in """ + val
        cur.execute(querystr)
        # cur.execute("""select driverid from driverlocation
        # where h3index in ('/x89416eb0137ffff', '/x89658656343ffff', '/x89414b854a7ffff', '/x89416889b2bffff', '/x894150ad303ffff')""")
        query_results = cur.fetchall()

    # ==========================================
    end = time.time() 
    print(query_results[:5])
    print('time execute: ', end - begin, 'seconds')
# Close the cursor and connection to so the server can allocate
# bandwidth to other requests
run (12.15, 104.77)
cur.close()
conn.close()
