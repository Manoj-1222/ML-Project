from setuptools import setup,find_packages
from typing import List
HYPHEN_DOT_E = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path,'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n',"") for req in requirements]
        if HYPHEN_DOT_E in requirements:
            requirements.remove(HYPHEN_DOT_E)
            
    return requirements
setup(
    name='mlProject',
    version='0.0.1',
    author='Manoj',
    author_email='gogurlamanoj722@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements ('requirements.txt')
)
