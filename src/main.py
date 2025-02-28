import os
from driver import Driver
import time
def startlambda(event, context):
    start_time = time.time()
    print(Driver.get_today_jobs())
    end_time = time.time()
    print(f"Runtime: {end_time - start_time} seconds")

startlambda(None,None)