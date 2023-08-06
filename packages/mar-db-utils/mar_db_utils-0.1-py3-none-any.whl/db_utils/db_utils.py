import psycopg2
import psycopg2.extras

class PgDbOps:
    '''
    Class to handle Postgres DB operations
    :param params: dictionary of connection parameters
    '''
    def __init__(self, params):
        self.conn = None
        self.params = params
        
    def connect_db(self) -> None:
        """
            Connect to the PostgreSQL database server
            :return: connection object or None
        """
        try:
           # connect to the PostgreSQL server
            if self.conn is None:
                self.conn = psycopg2.connect(**self.params)
            print("Connection to PostgreSQL DB successful")
        except (Exception, psycopg2.DatabaseError) as error:
            raise Exception("Error connecting to DB: ", error)

    ## close the db connection
    def close_db(self) -> None:
        print("Closing DB connection")
        self.conn.close()
        self.conn = None

    ## following handles insert, update, delete
    ## insert data based on sql, uses %s in flds for data fields
    ## %s is used for value 
    def sqlrun(self, sql,flds=[],tsql="insert") -> int:
        '''
        Insert, update, or delete data from a table
        :param sql: SQL statement
        :param flds: list of values
        :param tsql: type of sql statement
        :return: id of inserted row or False if error
        '''
        
        self.connect_db()
        try:
            c = self.conn.cursor()
            c.execute(sql,flds)
            id = 0
            if tsql == "insert":
                id = c.fetchone()[0]
            self.conn.commit()
            self.close_db()
            return id
        except Exception as e:
            self.close_db()
            print("Did not process... ",sql,flds,e.args)
            return False

    ## following handles insert strings with multiple value entries
    ## may want to integrate with above as sql string would run
    def runinsmultiples(self, sql) -> int:
        '''
        Insert multiple rows into a table
        :param sql: SQL statement
        :return: id of inserted row or False if error
        '''
        self.connect_db()
        try:
            c = self.conn.cursor()
            c.execute(sql)
            id = c.fetchone()[0]
            self.conn.commit()
            self.close_db()
            return id
        except Exception as e:
            self.close_db()
            print("Did not MULTIPLE ingest... ",sql,e.args)
            return False
#   
    def runbulkinsert(self, sql, fmtspecs, vals) -> bool:
        '''
        Bulk insert data into a table
        :param sql: SQL statement
        :param fmtspecs: format specifications
        :param vals: list of values
        :return: True if successful, False otherwise
        '''
        global conn
        self.connect_db()
        try:
            c = self.conn.cursor()
            args = ','.join(c.mogrify("({0})".format(fmtspecs), i).decode('utf-8') for i in vals)
            c.execute(sql + (args))
            self.conn.commit()
            self.close_db()
            return True
        except Exception as e:
            print("bulk insert error: ", sql, e.args)
            self.close_db()
            return False   
#   
    def insert_data(self, sql,flds) -> int:
        '''
        Insert data into a table
        :param sql: SQL statement
        :param flds: list of values
        :return: id of inserted row or False if error
        '''
        return self.sqlrun(sql,flds,"insert")
#   
    def update_data(self, sql,flds=[],tsql="update") -> int:
        '''
        Update data in a table
        :param sql: SQL statement
        :param flds: list of values
        :return: id of updated row or False if error
        '''
        return self.sqlrun(sql,flds,tsql)
#   
    def delete_data(self, sql,flds=[],tsql="delete") -> int:
        '''
        Delete data from a table
        :param sql: SQL statement
        :param flds: list of values
        :return: id of deleted row or False if error
        '''
        return self.sqlrun(sql,flds,tsql)
#   
    ## following is pg ready
    def select_data(self, sql) -> list:
        '''
        Select data from a table
        :param sql: SQL statement
        :return: list of rows or False if error
        '''

        self.connect_db()
        if self.conn is not None:
            cur = self.conn.cursor()
        print("selecting data: ", sql)
        try:
            rcur = []
            cur.execute(sql)
            row = cur.fetchone()
            while row is not None:
                rcur.append(row)
                row = cur.fetchone()
            cur.close
            self.close_db()
            print("select data: ", rcur)
            return rcur
        except:
            print("select error: ", sql)
            self.close_db()
            return False