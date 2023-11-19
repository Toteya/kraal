#!/usr/bin/python
"""
Initialises the test_models package
"""
from os import environ

environ['KRAAL_MYSQL_USER'] = 'root'
environ['KRAAL_MYSQL_PWD'] = 'password'
environ['KRAAL_MYSQL_HOST'] = 'localhost'
environ['KRAAL_MYSQL_DB'] = 'kraal_test_db'
environ['KRAAL_ENV'] = 'test'
