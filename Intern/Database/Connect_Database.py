import pyodbc

def connect_db():
    # Define the database connection parameters
    server = 'BANHMIBIETBAY\\SQLEXPRESS'
    database = 'Sales_Manager'
    username = 'sa'
    password = '180403'

    # Create the database connection
    conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
    return conn
