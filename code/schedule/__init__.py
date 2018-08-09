#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, make_response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import configparser

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

def configure():
	from schedule.api.user import bp as user_bp
	from schedule.api.availability import bp as availability_bp
	from schedule.api.interview import bp as interview_bp
	app.register_blueprint(user_bp, url_prefix='/user')
	app.register_blueprint(availability_bp, url_prefix='/availability')
	app.register_blueprint(interview_bp, url_prefix='/interview')

	config = configparser.ConfigParser()
	config.read('config.ini')
	db_uri = config['schedule']['db_uri']
	engine = create_engine(db_uri, convert_unicode=True)
	db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

	from schedule.model import db
	db.session = db_session

def main():
	configure()
	app.run('0.0.0.0', 1818)

if __name__ == '__main__':
	main()
