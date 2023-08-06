# mar-db_utils

## Description
This is a library that contains a set of functions that can be used to interact with a databases.  Currently, the library only supports PostgreSQL.
To use, instantiate the PgDbOps class and pass in the database name, user, password, port, and sslmode as arguments.

The PgDbOps class has the following methods:
- connect_db
    - This method connects to the database and returns a connection object.
- close_db
    - This method closes the database connection.
- sqlrun
    - This method runs a single SQL statement.
- runinsmultiples
    - This method runs a single SQL statement multiple times.
- runbulkinsert
    - This method runs a bulk insert SQL statement. 
- insert_data
    - This method inserts data into a table. This method uses sqlrun to run the SQL statement.
- update_data
    - This method updates data in a table. This method uses sqlrun to run the SQL statement.
- delete_data
    - This method deletes data from a table.  This method uses sqlrun to run the SQL statement.
- select_data
    - This method selects data from a table.

## Setup
Create a virtual environment
Activate the virtual environment
Install the following libraries:
- psycopg2-binary
- pystest
- python-dotenv

Create a .env file and add the following:
- DB_NAME
- DB_USER
- DB_PORT
- DB_SSLMODE
- DB_PASSWORD
