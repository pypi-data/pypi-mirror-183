from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Check user input and return True/False'
LONG_DESCRIPTION = 'Checks the user input and returns True/False by comparing to a list of known entries e.g. "absolutely" --> True, "not on your life" --> False alongside other more common user inputs (yes,y,n,no)'

# Setting up
setup(
        name="yesnopy", 
        version=VERSION,
        author="Arnav Nagpure",
        author_email="<arnav.n256@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        
        keywords=['userinput', 'user input', 'input'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)