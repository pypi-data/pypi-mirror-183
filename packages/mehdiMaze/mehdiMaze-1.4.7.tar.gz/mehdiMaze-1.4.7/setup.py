#python setup.py sdist bdist_wheel
#python -m twine upload dist/*
#for use in another pc:
#pip install mehdiMaze
#python -m pip install --upgrade mehdiMaze

from setuptools import setup, find_packages
from pathlib import Path

setup(
        name="mehdiMaze", 
        version='1.4.7',
        author="Mehdi Samee Rad",
        author_email="SameeRad@aut.ac.ir",
        description='My first Python package',
        long_description=Path("README.md").read_text(),
        packages=find_packages(),
        
        # add any additional packages that 
        # needs to be installed along with your package.
        install_requires=["tabulate"], 
        
        keywords=['python', 'maze', 'game', 'samee', 'rad', 'mehdi'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
        ]
)