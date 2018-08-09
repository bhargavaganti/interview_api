#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint, request, abort, jsonify
from schedule import app
from schedule.model import user_access
from schedule.util.constants import ROLES, SUCCESS

bp = Blueprint('user', __name__)

@bp.route('/create')
def create():
	username = request.args.get('username', '').strip()
	name = request.args.get('name', '').strip()
	role = request.args.get('role', '').strip()

	if username and name and role:
		user = user_access.get(username)
		if user:
			abort(406, 'User already exists')
		if role not in ROLES:
			abort(406, 'Invalid user role')
		status = user_access.create(username=username,
								   name=name,
								   role=role)
		if status is SUCCESS:
			return jsonify({'message': 'User with username=%s created' % username})
		else:
			abort(500)
	else:
		abort(406, 'Missing parameters')
