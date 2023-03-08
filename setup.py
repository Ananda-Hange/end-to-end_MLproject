from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_reqirements(file_path:str)->List[str]:
    """
    this func will return the list of requirements

    """
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [i.replace("\n",'') for i in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(

    name='end-to-end_MLprojrect',
    version='0.0.1',
    author='Ananda',
    author_email='anandahange@gmail.com',
    packages=find_packages(),
    install_requires=get_reqirements('requirements.txt')

)