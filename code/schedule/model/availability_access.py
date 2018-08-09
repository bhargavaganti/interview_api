#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import or_, and_
from schedule.model import db, Availability
from schedule.util.constants import WEEKS_DICT, DAYS_DICT, SUCCESS, FAILED, MIN_WORKING_HOUR, MAX_WORKING_HOUR
from schedule.util.helper import date_of_weekday, date_to_weekday, hour24_to_hour_12
import datetime

def add_slots(username, weeks, days, hours):
	today = datetime.date.today()
	for w in weeks:
		for d in days:
			week_no = WEEKS_DICT[w]
			week_day = DAYS_DICT[d]
			start_hour, end_hour = map(int, hours)
			date = date_of_weekday(week_no=week_no, week_day=week_day)
			availability = Availability(username=username,
										date=date,
										start_hour=start_hour,
										end_hour=end_hour)
			interscections = get_intersections(availability)
			if interscections:
				availability = join(interscections, availability)
			
			# No need to add old dates to DB
			if date >= today:
				db.session.add(availability)
	try:
		db.session.commit()
	except Exception as e:
		db.session.rollback()
		return FAILED

	return SUCCESS

def get_intersections(availability):
	"""
		Getting intersection with given availability time 
	"""
	q = db.session.query(Availability)
	q = q.filter(Availability.username==availability.username)
	q = q.filter(Availability.date==availability.date)
	q = q.filter(
		or_(
			and_(Availability.start_hour <= availability.end_hour, Availability.start_hour >= availability.start_hour),
			and_(Availability.end_hour <= availability.end_hour, Availability.end_hour >= availability.start_hour)))
	return q.all()

def join(interscections, availability):
	"""
		Joining all intersected availabilities in to one availability.
		Returning one availability which is containing all intersections.
	"""
	for av in interscections:
		availability.start_hour = min(availability.start_hour, av.start_hour)
		availability.end_hour = max(availability.end_hour, av.end_hour)
		db.session.delete(av)
	return availability

def get_all_availabilities_by_username(username):
	today = datetime.datetime.today()
	q = db.session.query(Availability)
	q = q.filter(Availability.username == username)
	q = q.filter(Availability.date >= today)
	q = q.order_by(Availability.date)
	return q.all()

def get_availabilities_by_date_and_username(username, date):
	q = db.session.query(Availability)
	q = q.filter(Availability.username == username)
	q = q.filter(Availability.date == date)
	return q.all()

def hourly_availability_count(availabilities):
	"""
		Calculating hours array
		hours (array) : hourly available contestant number
	"""
	hours = [0]* (MAX_WORKING_HOUR+1)
	for availability in availabilities:
		hours[availability.start_hour] += 1
		hours[availability.end_hour] -= 1
	for i in range(MIN_WORKING_HOUR, MAX_WORKING_HOUR):
		hours[i] += hours[i-1]
	return hours

def all_users_available_slots(hours, user_num):
	"""
		Finds 
	"""
	slots = []
	start, end = 0, 0
	for i in range(MIN_WORKING_HOUR, MAX_WORKING_HOUR+1):
		if hours[i] != user_num:
			continue
		if hours[i-1] < user_num:
			start = i
		if hours[i+1] < user_num:
			end = i+1
			start_12h = hour24_to_hour_12(str(start))
			end_12h = hour24_to_hour_12(str(end))
			new_slot = {'start': start_12h, 'end': end_12h}
			slots.append(new_slot)
	return slots

def check_for_interview(users):
	user_num = len(users)
	sample_username = users.pop(0)
	sample_user_availabilities = get_all_availabilities_by_username(sample_username)

	results = []
	for availability in sample_user_availabilities:
		availabilities = [availability]
		for username in users:
			user_avs = get_availabilities_by_date_and_username(username, availability.date)
			availabilities += user_avs

		hours = hourly_availability_count(availabilities)		
		slots = all_users_available_slots(hours, user_num)
		if slots:
			week_name, weekday_name = date_to_weekday(availability.date)
			new_schedule = {'week': week_name, 'day': weekday_name, 'time_slots': slots}
			results.append(new_schedule)

	return results







