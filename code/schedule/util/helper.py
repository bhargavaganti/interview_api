
from schedule.util.constants import WEEKS_NAME, WORKING_DAYS_NAME, WORKING_HOURS
import datetime

def valid_from_list(sample_list, container_list):
	"""
		Validation of paramaters are proper list
	"""
	valid = len(sample_list) > 0
	for sample in sample_list:
		valid = valid and sample in container_list
	return valid

def valid_slot(weeks, days, hours):
	valid_inputs = valid_from_list(weeks, WEEKS_NAME) and \
					valid_from_list(days, WORKING_DAYS_NAME) and \
					valid_from_list(hours, WORKING_HOURS)
	valid_time = len(hours) == 2 and int(hours[0]) < int(hours[1])
	return valid_inputs and valid_time

def date_of_weekday(week_no, week_day):
	today = datetime.date.today()
	days_diff = week_day - today.weekday()  
	date = today + datetime.timedelta(days=days_diff, weeks=week_no)
	return date

def date_to_weekday(date):
	today = datetime.date.today()
	weekday_no = date.weekday()
	weekday_name = WORKING_DAYS_NAME[weekday_no]
	week_no = date.isocalendar()[1] - today.isocalendar()[1]
	week_name = WEEKS_NAME[week_no]
	return week_name, weekday_name

def hour24_to_hour_12(hour):
	time = datetime.datetime.strptime(hour, "%H")
	return time.strftime("%I:%M %p")