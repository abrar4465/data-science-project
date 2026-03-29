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
        df = pd.read_sql_query("SELECT * FROM student", mydb)
        print(df.head())
        logger.info("Data read successfully from SQL database")
        return df
    except Exception as e:
        logger.error(f"Error reading data from SQL database: {e}")
        raise CustomException(e, sys)


class DataIngestionConfig:
    def __init__(self):
        self.raw_data_path = "artifacts/raw.csv"
        self.train_data_path = "artifacts/train.csv"
        self.test_data_path = "artifacts/test.csv"


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logger.info("Entering the data ingestion method or component")
        try:
            df = read_sql_data()
            logger.info("Read the dataset as dataframe")
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logger.info("Ingestion of the data is completed")
            
            return (
                self.ingestion_config.raw_data_path,
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logger.error(f"Error in data ingestion: {e}")
            raise CustomException(e, sys)