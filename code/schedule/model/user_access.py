#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from schedule.model import db, User
from schedule.util.constants import SUCCESS, FAILED

def create(username, name, role):
	user = User(username=username,
				name=name,
				role=role)
	try:
		db.session.add(user)
		db.session.commit()
	except Exception as e:
		db.session.rollback()
		return FAILED

	return SUCCESS

def get(username):
	return db.session.query(User).get(username)