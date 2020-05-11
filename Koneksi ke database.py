# -*- coding: utf-8 -*-
"""
Created on Mon May  4 11:23:30 2020

@author: jiwandhono
"""

from sqlalchemy import create_engine
import pandas as pd
# from configparser import ConfigParser
# import psycopg2
# import mysql.connector

# URL = "host ='localhost' dbname = 'dvdrental' user='postgres' password='postgres'"
# psycopg2.connect(URL)

URL = "sqlite:///data.db"
# query1 = """
# SELECT hpd311calls.created_date, 
#        weather.tmax,
#        weather.tmin
#   FROM hpd311calls 
#        JOIN weather
#        ON hpd311calls.created_date = weather.date
#  WHERE hpd311calls.complaint_type = 'HEAT/HOT WATER' 
#  GROUP BY hpd311calls.complaint_type;"""
query1 = """ 
 SELECT 
 weather.date ,weather.tmax, weather.tmin
 FROM weather
 GROUP BY weather.date
 """

query2 = """SELECT hpd311calls.created_date, 
       COUNT(*)
  FROM hpd311calls 
 WHERE hpd311calls.complaint_type = 'HEAT/HOT WATER' 
 GROUP BY hpd311calls.created_date;"""

def db_engine(URL):
    engine = create_engine(URL)
    
    return engine
engine = db_engine(URL)

weather = pd.read_sql(query1, engine)
call = pd.read_sql(query2, engine)

#Jadi ingin menggabungkan antara call dan weather
# df1.merge(df2, left_on = df1_kolom, right_on = df2_kolom)
merged = call.merge(weather, left_on="created_date", right_on = "date")

















