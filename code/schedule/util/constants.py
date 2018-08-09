#!/usr/local/bin/python
# -*- coding: utf-8 -*-

SUCCESS = 'Success'
FAILED = 'Failed'


CANDIDATE = 'candidate'
INTERVIEWER = 'interviewer'
ROLES = [CANDIDATE, INTERVIEWER]

MIN_WORKING_HOUR = 9
MAX_WORKING_HOUR = 18
WORKING_HOURS = [str(i) for i in range(MIN_WORKING_HOUR, MAX_WORKING_HOUR+1)]

WORKING_DAYS_NO = [i for i in range(5)]
WORKING_DAYS_NAME = ['mon', 'tue', 'wed', 'thu', 'fri']

WEEKS_NO = [0, 1] 
WEEKS_NAME = ['current', 'next']

ALL_HOURS = ','.join([str(MIN_WORKING_HOUR), str(MAX_WORKING_HOUR)])
ALL_DAYS = ','.join(WORKING_DAYS_NAME)
ALL_WEEKS = ','.join(WEEKS_NAME)


WEEKS_DICT = {'current': 0, 'next': 1}
DAYS_DICT = { 'mon': 0, 'tue':1, 'wed': 2, 'thu': 3, 'fri': 4}
