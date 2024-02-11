import os
from dotenv import load_dotenv
from peewee import MySQLDatabase
 
load_dotenv()
 
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
hostname = os.getenv('HOST')
database = os.getenv('DATABASE')

db = MySQLDatabase(
    database, user=username,
    password=password, host=hostname, port=3306
)
