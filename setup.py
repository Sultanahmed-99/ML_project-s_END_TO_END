# 
from setuptools import find_packages , setup  
from typing import List



HYPEN_E_DOT ='-e.' 
def get_requirements(file_path : str)->List[str]:
    """
    this function will return List of requirements 
    """
    # empty list to store requirement's in a list 
    requirements = []
    # open file path as file_obj
    with open(file_path) as file_obj:
        # read in all lines 
        requirements = file_obj.readlines()
        # handling the problem of readlines including \n 
        requirements = [req.replace("\n","") for req in requirements ]
        # handling problem of reading in -e . in requirement's.txt 
        if HYPEN_E_DOT in requirements :
            requirements.remove(HYPEN_E_DOT) 

 
    return requirements  

setup(
 # metadata
name= "Mlproject" ,
version= '0.0.1' , 
author= 'Sultan' , 
author_email='sultanworker@gmail.com' , 
packages= find_packages() , 
install_requires = get_requirements('requirements.txt') , 

)

# This code block sets up the metadata
#  for the project, including the project name,
#   version number, author, author email,
#   and required packages. The 'find_packages' 
#   function is used to automatically detect and 
#   include all project packages. 
#   The 'install_requires'
#    argument specifies 
#    the required packages that need to be installed 
#    in order to run the project successfully.