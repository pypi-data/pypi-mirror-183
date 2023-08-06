from setuptools import setup

setup(
    name='mar-db_utils',  
    version='0.1',
    description="A simple set of Posgres DB utilities",
    url="https://github.com/maradder/db_utils",
    author="Marcus Radder",
    author_email="marcusradder@gmail.com",
    license='MIT',
    packages=['db_utils'],
    install_requires=[
        'psycopg2-binary',
        'pytest',
        'load_dotenv'
    ],
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )