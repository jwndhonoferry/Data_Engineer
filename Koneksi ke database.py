# -*- coding: utf-8 -*-
"""
Created on Mon May  4 11:23:30 2020

@author: jiwandhono
"""

from sqlalchemy import create_engine
import pandas as pd
from configparser import ConfigParser
import psycopg2
import mysql.connector

# URL = "host ='localhost' dbname = 'dvdrental' user='postgres' password='postgres'"
# psycopg2.connect(URL)

URL = "sqlite:///data.db"
query = """
SELECT hpd311calls.created_date, 
	   COUNT(*), 
       weather.tmax,
       weather.tmin
  FROM hpd311calls 
       JOIN weather
       ON hpd311calls.created_date = weather.date
 WHERE hpd311calls.complaint_type = 'HEAT/HOT WATER' 
 GROUP BY hpd311calls.created_date;"""

def db_engine(URL):
    engine = create_engine(URL)
    
    return engine
engine = db_engine(URL)

data = pd.read_sql(query, engine)


