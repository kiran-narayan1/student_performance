from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    try:
        requirements = []

        with open('requirements.txt') as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.replace('\n', '') for req in requirements]

            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)

        print('reuirements', requirements)
        return requirements

    except Exception as e:
        print(f'error while reading the requirements.txt {e}')


setup(
    name='student performance',
    version='0.0.1',
    author='kiran',
    author_email='@gmail.com',
    packages=find_packages(),
    install_requires=['pandas', 'numpy']

)
