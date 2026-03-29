import os
import sys
from src.exception import CustomException
from src.logger import logger
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

def read_sql_data(): 
    logger.info("Reading data from SQL database")
    try:
        mydb = pymysql.connect(host=host, user=user, password=password, db=db)
        logger.info(f"Successfully connected to SQL database: {mydb}")
        df = pd.read_sql_query("SELECT * FROM student", mydb)  # ✅ Fixed table name
        print(df.head())
        logger.info("Data read successfully from SQL database")
        return df
    except Exception as e:
        logger.error(f"Error reading data from SQL database: {e}")
        raise CustomException(e, sys)