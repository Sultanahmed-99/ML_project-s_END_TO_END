# from src.exception import CustomException  # import the CustomException class from a custom module
from src.logger import logging  # import the logging library from a custom module
import dill  # import the dill library for object serialization
import os  # import the os library for file path operations
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV





def save_object(file_path, obj):
    """
    Save an object to a file.

    Args:
        file_path: The path to the file where the object should be saved.
        obj: The object to be saved.

    Returns:
        None.

    Raises:
        CustomException: If an error occurs while saving the object.
    """
    try:
        # Create the directory specified by the file_path if it doesn't exist, but don't raise an error if it already exists
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        # Use dill to dump the object to the specified file path
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        # If an error occurs, raise a CustomException with the error message and details
        raise CustomException(e, sys)



def evaluate_model(x_train , y_train , x_test  , y_test , models , param):# , params
    try : 
        
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]]

            gcv = GridSearchCV(model , param_grid=para , cv = 5 , n_jobs=-1)
            gcv.fit(x_train , y_train)

            
            model.set_params(**gcv.best_params_)
           
            model.fit(x_train , y_train)
            

            y_train_pred = model.predict(x_train)

            y_test_pred = model.predict(x_test)

            train_model_score = r2_score(
                y_train , y_train_pred
            )
            
            test_model_score = r2_score(
                y_test , y_test_pred
            )

            report[list(models.keys())[i]] = test_model_score
        logging.info("Traninig the Models is done.")
        return report
         
    except Exception as e :
        raise CustomException(e , sys)
      



if __name__ == '__main__':
    print(model)