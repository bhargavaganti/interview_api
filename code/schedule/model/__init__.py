#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime, Boolean, Index, Text, Date
from sqlalchemy.ext.declarative import declarative_base

db = declarative_base()

class User(db):
    __tablename__ = 'tbl_user'
    username = Column(String(64), primary_key=True)
    name = Column(String(256), nullable=False)
    role = Column(String(32), nullable=False)


class Availability(db):
    __tablename__ = 'tbl_availability'
    id = Column(Integer, primary_key=True)
    username = Column(String(64),
    				ForeignKey(User.__tablename__ + '.username', deferrable=True),
            		nullable=False)
    date = Column(Date, nullable=False)
    start_hour = Column(Integer, nullable=False)
    end_hour = Column(Integer, nullable=False)
