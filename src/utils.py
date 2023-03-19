# Have comman func


import sys 
import os 

import pandas as pd 
import numpy as np 

from src.exception import CustomeException
from src.logger import logging
import dill

def save_object(file_path , obj):
    try : 
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path , exist_ok=True)

        with open(file_path , 'wb') as file_obj:
            dill.dump(obj  , file_obj)


    except Exception as e : 
        raise CustomeException(e , sys)