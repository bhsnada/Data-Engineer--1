import sqlite3

CREATE_TABLE = '''
    CREATE TABLE IF NOT EXISTS organizations(
        "Index" INTEGER PRIMARY KEY,
        OrganizationId TEXT,
        Name TEXT,
        Website TEXT,
        Country TEXT,
        Description TEXT,
        Founded INTEGER,
        Industry TEXT,
        NumberOfEmployees INTEGER
    );
    '''

INSERT_DATA = '''
    insert into organizations (OrganizationId, Name, Website, Country, Description, Founded, Industry, NumberOfEmployees)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?);   
'''

CHECK_DATA = '''
    SELECT * FROM  organizations limit 10;
'''

def connect():
    return sqlite3.connect("data_db.db")


def create_tables(connection):
    with connection:
        connection.execute(CREATE_TABLE)


def ingest_data(connection, OrganizationId, Name, Website, Country, Description, Founded, Industry, NumberOfEmployees):
    with connection:
        connection.execute(INSERT_DATA,(OrganizationId, Name, Website, Country, Description, Founded, Industry, NumberOfEmployees))


def get_sample_data(connection):
        cur = connection.cursor()
        cur.execute(CHECK_DATA)
        rows = cur.fetchall()
        return rows



