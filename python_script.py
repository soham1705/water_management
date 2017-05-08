import requests
import urllib
import traceback
import re
import MySQLdb
while 1:
    s=""
    l=""
    try:
        v=requests.get('http://192.168.43.134:1336')
        #print "111",v.content
        #print v.content
    except :
        s = str(traceback.format_exc())
    #print (s)
    if "Bad" in s:
        s=s[s.index("Bad"):]
        s=s[15:]
        #print 
        #print s
        try:
            s=s[:s.index(')')-6]
            print s , " ml"
           # l=s.split(":")
        except:
            pass



    # Open database connection
    db = MySQLdb.connect("localhost","water_consumer","test1234","watermeter" )
    billl=int(s)*2.36;
# prepare a cursor object using cursor() method
    cursor = db.cursor()

# Select qSQL with id=4.
    #cursor.execute("SELECT qSQL FROM TBLTEST WHERE id = 4")

    #SQL query to INSERT a record into the table FACTRESTTBL.
    cursor.execute("UPDATE bill SET consumed=" + s +",bil=" + str(billl) +" where username='soham_m1705';");
    # Commit your changes in the database
    db.commit()

    db.close()

        #print "this is l"
        #print l
        #if l:
            #print ("we have: "+urllib.quote(l[0]))
            #r=urllib.urlopen("https://energymanagement.pythonanywhere.com/energy_management/default/temp?f1="+urllib.quote(l[0]))
         #   print r,"success"
        
    
