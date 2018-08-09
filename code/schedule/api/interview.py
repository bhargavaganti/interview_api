#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint, request, abort, jsonify
from schedule import app
from schedule.model import availability_access, user_access
from schedule.util.constants import ALL_HOURS, ALL_DAYS, ALL_WEEKS, SUCCESS, CANDIDATE

bp = Blueprint('interview', __name__)

@bp.route('/check', methods=['GET'])
def create():
	users_str = request.args.get('users', '').strip()
	users = users_str.split(',')
	users = list(map(str.strip, users))

	if len(users) < 2:
		abort(406, 'Number of users must be equal or more than two.')

	candidate_num = 0
	for username in users:
		user = user_access.get(username)
		if not user:
			abort(406, 'Invlid username')
		candidate_num += int(user.role == CANDIDATE)
	if candidate_num != 1:
		abort(406, 'Only one candidate can join the interview.')

	available_time_slots = availability_access.check_for_interview(users)

	if available_time_slots:
		return jsonify(available_time_slots)
	else:
		abort(500)
