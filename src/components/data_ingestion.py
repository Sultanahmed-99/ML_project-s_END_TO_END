
import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation , DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig ,  ModelTrainer 
from src.exception import CustomException
from src.logger import logging

@dataclass
class DataIngestionConfig:
    """Class defining the configuration for data ingestion."""
  
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")


class DataIngestion:
    """Class for ingesting data, splitting it into training and testing datasets, and saving it to disk."""
    
    def __init__(self):
        """Initialize a DataIngestion object with the default configuration."""
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        """Reads a CSV file, performs a train-test split, and saves the resulting datasets to disk.
        Returns:
            Tuple of file paths to the training and testing datasets.
        """
        logging.info("Entered the data ingestion method or component")

        try:
            # Read in the data from a CSV file
            df = pd.read_csv("/Users/sly/Desktop/ML_projects/src/Notebook/data/StudentsPerformance.csv")
            logging.info("Read the dataset as a dataframe")

            # Create the directory for the training data file if it does not exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save the raw data to disk
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # Perform a train-test split
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            logging.info("Train-test split initiated")

            # Save the training and testing datasets to disk
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            # If an exception occurs during the data ingestion process, raise a custom exception
            raise CustomException(e  , sys)


## Just for Testing ##
if __name__ == '__main__':
    obj = DataIngestion()
    train_data , test_data = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr , test_arr,_ = data_transformation.initiate_data_transformation(train_data, test_data) 
    model_trainer = ModelTrainer()
    print(model_trainer.initiates_model_trainer(train_arr, test_arr) )