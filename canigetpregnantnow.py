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

from datetime import datetime

@app.route("/day1", methods=["POST"])
def Change_day1_to_integer():
	form_data = request.form #Getting hold of a Form object that is sent from a browser.
	day1 = form_data["day1"]
    formatday1 = datetime.datetime(day1)

@app.route("/CycleLength", methods=["POST"])
def Give_ovulation_date():
    form_data = request.form #Getting hold of a Form object that is sent from a browser.
	CycleLength = form_data["CycleLength"]

def Can_I_get_pregnant(day1, CycleLength):
    day1() + CycleLength()


def Give_first_day_of_cycle():
    day1 = raw_input()
    return int(day1)

def Give_length_of_cycle():
    CycleLength = raw_input()
    return int(CycleLength)

def Can_I_get_pregnant(day1, CycleLength):
    OvulationFirstDay = day1 + CycleLength/2
    return OvulationFirstDay


exampleDate = Give_first_day_of_cycle()
exampleLength = Give_length_of_cycle()
print Can_I_get_pregnant(exampleDate, exampleLength)
