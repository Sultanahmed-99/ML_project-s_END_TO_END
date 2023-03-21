import sys 
from dataclasses import dataclass 
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer 
from sklearn.preprocessing import OneHotEncoder , StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from src.logger import logging 
from src.exception import CustomException
import os 
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_ob_file_path = os.path.join('artifacts' , 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_transformer_object(self):
        
        try:
            numerical_columns = ['reading score','writing score']
            categorical_columns = ['gender',
                                  'race/ethnicity',
                                  'parental level of education',
                                  'lunch',
                                  'test preparation course'
                                  ]
            # Create a pipeline 
            numeric_pipeline = Pipeline(
                steps= [
                    # Handling missing data 
                    ("Imputer" , SimpleImputer(strategy='median')) ,  # in case of outliers 
                    # Rescaling 
                    ('Scaler' , StandardScaler(with_mean=False)),
                ]

            )
            categorical_pipeline = Pipeline(
                steps = [
                    ('Imputer' , SimpleImputer(strategy='most_frequent')) ,
                    ('OneHotEncoder' , OneHotEncoder()) , 
                    ('Scaler' , StandardScaler(with_mean=False)),
                ] 
            )

            logging.info(f'Numerical columns : {numerical_columns}')
    

            logging.info(f'Categorical columns : {categorical_columns}')

            preprocessor = ColumnTransformer(
                [
                    ('Numeic_pipeline' , numeric_pipeline , numerical_columns),
                    ('Cat_pipeline' , categorical_pipeline , categorical_columns),
                ]
            )

            return preprocessor
            
        except Exception as e : 
            raise CustomeException(e, sys)



    def initiate_data_transformation(self , train_path , test_path):


        try : 
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info('Read train and test data completed')

            logging.info('Obtaining preprocessing object')
            preprocessor_obj = self.get_data_transformer_object()

            target_column_name = 'math score'
            numerical_columns = ['reading score','writing score']
            
            input_feature_train_df = train_df.copy()
            target_varible_train_df = train_df.pop(target_column_name)


            input_feature_test_df = test_df.copy()
            target_varible_test_df = test_df.pop(target_column_name)
 
            logging.info('Applying preprocessing object on training data frame and testing dataframe.')
            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr , np.array(target_varible_train_df)
            ]

            test_arr = np.c_[
                input_feature_test_arr , np.array(target_varible_test_df)
            ]

            logging.info('Saved preprocessing object.')

            save_object(
                file_path = self.data_transformation_config.preprocessor_ob_file_path,
                obj = preprocessor_obj

            )


            return (
                train_arr , 
                test_arr ,
                self.data_transformation_config.preprocessor_ob_file_path
            )

        except Exception as e: 
            raise CustomException(e, sys)
             