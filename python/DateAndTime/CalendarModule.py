from datetime import datetime as dt
from time import gmtime, strftime

sDate = input()
tDate = dt.strptime(sDate, "%m %d %Y")
print(tDate.strftime("%A").upper())
