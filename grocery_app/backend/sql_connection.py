import pyodbc
__conn = None
def get_sql_connection():
    global __conn
    if __conn is None:
        try:
            server = r"DPU-COL-PC30"
            database = "Gs"

            __conn = pyodbc.connect(
                f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                f'SERVER={server};'
                f'DATABASE={database};'
                f'Trusted_Connection=yes;'
        )
        except pyodbc.Error:
            return None
    return __conn