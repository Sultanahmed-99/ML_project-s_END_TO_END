from src.exception import CustomeException 
import sys 
from src.components.model_trainer import ModelTrainerConfig , ModelTrainer
# from src.utils import evaluate_model

import numpy as np 

train_arr = np.array([[222,3333] , [3333,4444]])
test_array = np.array([[2222222] , [333333]])

if __name__ == '__main__':
    try:
        model_trainer  = ModelTrainer()
        print(model_trainer.initiates_model_trainer(train_arr, test_array))
    except Exception as e :
        raise CustomeException(e, sys)