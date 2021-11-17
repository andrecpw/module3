from datetime import datetime
from datetime import timedelta

def dong():
    gmt = datetime.now()
    bcn = gmt + timedelta(hours=1)
    return bcn.strftime('%H:%M')