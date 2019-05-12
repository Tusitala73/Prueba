import datetime
import time
import os


while (True):
    os.system('cls')
    dt = datetime.datetime.now()
    print( "{}:{}:{}".format( dt.hour, dt.minute, dt.second ) )
    time.sleep(1)
 

    

