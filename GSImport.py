import os #os.getcwd()
import pandas as pd # https://www.youtube.com/watch?v=1qMR1OjoeTM&list=PL3JVwFmb_BnSee8RFaRPZ3nykuMRlaQp1&index=24
import pypyodbc as odbc # conda install -c conda-forge pyp

os.chdir(r"C:\Users\Ywang36\Downloads")
df = pd.read_csv('Superintendent Info  - https___tinyurl.com_SuptInfo - Dist Office.csv',header=None)
"""
pull data from google sheet to dataframe to do transformation: split cells with two or more values into single row based on ; delimeter
remove unnecessary semicolons and \n  if there is nothing in front of semicolons
https://stackoverflow.com/questions/50731229/split-cell-into-multiple-rows-in-pandas-dataframe
"""
df = pd.DataFrame(df)
df = df.iloc[3:]
new_header = df.iloc[0] #grab the first row for the header
df = df[1:] # take the data less the header row
df.columns = new_header #set the header row as the df header df is 45 rows × 37 columns


df_cols = list(df.columns) #37 cols
df_cols
for i in df_cols:
    df[i] = df[i].str.lstrip(';')


"""
Push Dataset to SQL Server (database system)
"""
DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'ES00VPADOSQL180,51433'
DATABASE_NAME = 'SEO_REPORTING'


def connection_stirng(driver_name, server_name, database_name):
    # uid=<username>;
    # pwd=<password>;
    conn_string = f"""
        DRIVER={{{driver_name}}};
        SERVER={server_name};
        DATABASE={database_name};
        Trust_Connection=yes;      
    """
    return conn_string


# connection object creation
try:
    conn = odbc.connect(connection_stirng(DRIVER_NAME, SERVER_NAME, DATABASE_NAME))
    print('Connection created')
except odbc.DatabaseError as e:
    print('Database Error:')
    #print(str(e.value[1]))
except odbc.Error as e:
    print('Connection Error')
    #print(str(e.value[1]))
else:
    cursor = conn.cursor()
    sql_insert = """
        TRUNCATE TABLE [SEO_REPORTING].[Wang].[lk_SuptSupportStructureGoog]    
        INSERT INTO [SEO_REPORTING].[Wang].[lk_SuptSupportStructureGoog]
        VALUES(?, ?, ?, ?, ?, 
               ?, ?, ?, ?, ?, 
               ?, ?, ?, ?, ?, 
               ?, ?, ?, ?, ?, 
               ?, ?, ?, ?, ?, 
               ?, ?, ?, ?, ?, 
               ?, ?, ?, ?, ?, ?, ?)
    """
 
    try:
        cursor.executemany(sql_insert, df)
        cursor.commit()
        print('Data import complete')
    except Exception as e:
        #print(str(e.value[1]))
        cursor.rollback()
    finally:
        cursor.close()
        conn.close()