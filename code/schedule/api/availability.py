#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint, request, abort, jsonify
from schedule import app
from schedule.model import availability_access
from schedule.util.constants import ALL_HOURS, ALL_DAYS, ALL_WEEKS, SUCCESS
from schedule.util.helper import valid_slot

bp = Blueprint('availability', __name__)

@bp.route('/create')
def create():
	username = request.args.get('username', '').strip()
	week_inp = request.args.get('weeks', ALL_WEEKS).strip()
	days_inp = request.args.get('days', ALL_DAYS).strip()
	hours_inp = request.args.get('hours', ALL_HOURS).strip()

	if username:
		weeks = week_inp.split(',')
		days = days_inp.split(',')
		hours = hours_inp.split(',')

		# removing duplicates
		weeks = list(set(weeks))
		days = list(set(days))

		if not valid_slot(weeks=weeks, days=days, hours=hours):
			abort(406, 'Invalid parameters')

		status = availability_access.add_slots(username=username,
										weeks=weeks,
										days=days,
										hours=hours)
		if status is SUCCESS:
			return jsonify({'message': 'Time slots added'})
		else:
			abort(500)

	else:
		abort(406, 'Missing parameters')
