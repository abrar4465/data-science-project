from src.logger import logging
from src.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion, DataIngestionConfig
import sys

if __name__ == "__main__":
    logging.info("Starting the application.")
    try:
        logging.info("Initializing DataIngestionConfig...")
        data_ingestion_config = DataIngestionConfig()
        
        logging.info("Creating DataIngestion object...")
        data_ingestion = DataIngestion()
        
        logging.info("Starting data ingestion process...")
        data_ingestion.initiate_data_ingestion()
        
        logging.info("Data ingestion completed successfully!")
        
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        raise CustomException(e, sys)