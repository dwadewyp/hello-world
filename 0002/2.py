__author__ = 'wyp'

import MySQLdb

try:
    conn = MySQLdb.Connect(host='localhost',user='root',passwd = 'baidapang',db='mysql',port=3306)
    cur = conn.cursor()

    coupon = open('random.txt','r')
    value = coupon.read().split("\n")
    # print value,type(value),"value"
    print value,type(value),"value"

    for i in value:
        print i,type(i),"iha"
        cur.execute('insert into coupon(couponn) values("%s");' %(i))

    conn.commit()
    cur.close()
    conn.close()
except MySQLdb.Error,e:
    print "Mysql Error %d :%s" %(e.args[0],e.args[1])

