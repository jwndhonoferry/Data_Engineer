# -*- coding: utf-8 -*-
"""
Created on Sun May 10 12:12:35 2020

@author: jiwandhono
"""

from sqlalchemy import create_engine
import pandas as pd
from configparser import ConfigParser
import psycopg2
import mysql.connector
import json
import matplotlib as plt
#kalau bisa pakai pandas
data_json = pd.read_json("example_2.json", orient = "index")

#pakai json karena memkai pandas tidak bisa
# data = json.load(open("data.json"))
# data2 = json.dumps(data)


try:
    # Load the JSON with orient specified
    #Try to change orient (values, column, records, except split)
    df = pd.read_json("example_2.json", orient = "index")
    
    # Plot total population in shelters over time
    # df["quiz"] = pd.to_datetime(df["quiz"])
    # df.plot(x=columns, 
    #         y=row)
    # plt.show()
    
except ValueError:
    print("pandas could not parse the JSON.")