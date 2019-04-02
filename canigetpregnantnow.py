#This is the backend Python file for Can I Get Pregnant Now?

#Logic
#Python will receive the date of the first day of the last period
#Python will receive the average length of cycle
#Program will work out ovulation stage of cycle
    #take date format and change to integer
    #half the average length of cycle
    #add to the first day of the last period
    #push out first day (and following 5-10 days) as ovulation stage
    #convert back to date

from flask import Flask, render_template, request
from datetime import datetime

app = Flask("Test")

print "Current day:" % now.day

@app.route("/")
def landingPage():
	return render_template("index.html")

@app.route("/results", methods=["POST"])
def Change_day1_to_integer():
	form_data = request.form #Getting hold of a Form object that is sent from a browser.
	day1 = form_data["results"]
	formatday1 = datetime.datetime(day1)
	print day1

@app.route("/results", methods=["POST"])
def Give_ovulation_date():
	form_data = request.form
	print "test"
	return render_template("index.html")

#def Can_I_get_pregnant(day1, CycleLength):
#    day1() + CycleLength()
#	return 5

def Give_first_day_of_cycle():
   day1 = raw_input()
   return int(day1)

def Give_length_of_cycle():
    CycleLength = raw_input()
    return int(CycleLength)

def Can_I_get_pregnant(day1, CycleLength):
	OvulationFirstDay = day1 + CycleLength/2
	return OvulationFirstDay


def Ovulation_week(OvulationFirstDay):
	if OvulationFirstDay >= 14 and OvulationFirstDay <= 21:
		return 'You could get pregnant this week'
	if OvulationFirstDay <= 14 and OvulationFirstDay >= 21:
		return 'You are less likely to get pregnant this week'


#exampleDate = Give_first_day_of_cycle()
#exampleLength = Give_length_of_cycle()
#print Can_I_get_pregnant(exampleDate, exampleLength)

app.run()
