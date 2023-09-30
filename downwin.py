from datetime import datetime
import requests
from time import sleep
import sys

class DownWin:
    """It contain all the attributes and methods that main.py required."""
    def __init__(self):
        """Initilize all the attributes."""
        self.active = False
        pass

    def _am_or_pm(self, hour):
        """return am or pm accroiding to hour."""
        if hour > 12 and hour < 24:
            return "PM"
        return "AM"

    def current_time(self):
        """It return currect time as dictionary."""
        now = datetime.now() 
        current_t = {
            "hour": now.hour,
            "minate":now.minute,
            "second":now.second,
            "am/pm":self._am_or_pm(now.hour) 
                     }
        return current_t
    

    def _start_down(self, url, filename):
    
        print('Download Starting...')
        
        r = requests.get(url)
        
        with open(filename,'wb') as output_file:
            output_file.write(r.content)
        
        print('Download Completed!!!')
        self.active = False

        
        

    def check_current_time(self, current_time,url, filename):
        """It check current time and do action accoriding to condition."""
        # if current_time["hour"] == 23 and current_time["am/pm"] =="PM" and current_time["minate"] == 59:
           # Start downloading a file
        self._start_down(url, filename)
        sys.exit()

        # else:
        #     sleep(60)

        
