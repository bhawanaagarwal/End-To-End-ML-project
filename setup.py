from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    '''
    returns the list of requirements
    '''
    HYPHEN_E_DOT = '-e .'
    requirements =[]
    with open(file_path) as file_obj:
        requirements = [text.replace("\n","") for text in file_obj.readlines()]
    

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
        
    return requirements




setup(
name = 'endtoendmlproject',
version= '0.0.1',
author = 'Bhawana',
author_email= 'agarwalbhawana92@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')



)