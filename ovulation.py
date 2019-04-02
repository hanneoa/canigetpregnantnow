import requests
from datetime import datetime
import json


#Function to calcualte chance of ovulation

# - last period date - 6 days before ovulation = low chance of getting pregnant
# 5-1 days before ovulation = chance of getting pregnant
# ovulation day = high chance of getting pregnancy
# 1-2 days after ovulation = chance of getting pregnant
# 3 days after ovulation - end of cycle = low chance of getting pregnant

def Ovulation :

	if day == -41:
		sign = 'low' if (day < -6) else 'chance'
	elif month == -5:
		sign = 'chance' if (day < 0) else 'high chance'
	elif month == 0:
		sign = 'high chance' if (day < 2) else 'chance'
	elif month == 2:
		sign = 'chance' if (day < 3) else 'low chance'
	elif month == 3:
		sign = 'low chance' if (day < 41) else 'low chance'

	print("Your chance of pregnancy is",ovulation)
	return ovulation
