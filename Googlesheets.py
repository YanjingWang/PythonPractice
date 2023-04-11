import os #os.getcwd()
import pandas as pd # https://www.youtube.com/watch?v=1qMR1OjoeTM&list=PL3JVwFmb_BnSee8RFaRPZ3nykuMRlaQp1&index=24
import pypyodbc as odbc
from Google import Create_Service

"""
Getting Dataset from Google Sheets
"""
CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets'] # read and write permission if only need read access use .ReadOnly

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

google_sheets_id = '1mCmAhwYLYAGHabyDntbMOaIdg3X5PqhvVCfz7VL0hqw'

response = service.spreadsheets().values().get(
    spreadsheetId=google_sheets_id,
    majorDimension='ROWS',
    range='Dist Office'  # work sheet tab
).execute()

rows_original = response['values'][3:]   # to remove rows we don't need >>> rows.keys >>> rows.get('range')
rows = response['values']
"""
pull data from google sheet to dataframe to do transformation: split cells with two or more values into single row based on ; delimeter
remove unnecessary semicolons and \n  if there is nothing in front of semicolons
https://stackoverflow.com/questions/50731229/split-cell-into-multiple-rows-in-pandas-dataframe
"""
df = pd.DataFrame(rows)
df = df.iloc[3:]
new_header = df.iloc[0] #grab the first row for the header
df = df[1:] # take the data less the header row
df.columns = new_header #set the header row as the df header df is 45 rows × 37 columns
df = pd.DataFrame(df)

df_cols = list(df.columns) #37 cols
df_cols
for i in df_cols:
    df[i] = df[i].str.lstrip(';')
# (df.set_index(['Supt'
# ,'GalaxyLocationCodes'
# ,'District(s)'
# ,'Family Leadership Coordinate Email'
# ,'Family Support Coordinator'
# ,'FSC Email'
# ,'Student Services Manager'
# ,'Academic Policy and Performance & Asessment Leads'
# ,'Academic Policy and Performance & Asessment Leads - Email'
# ,'Director for Special Education'
# ,'Administrator of Special Education'
# ,'Administrator of Special Education Email'
# ,'Specialized Student Support Lead'
# ,'Specialized Student Support Lead Email'
# ,'Director for Multilingual Learners/English Language Learners'
# ,'Director for Multilingual Learners/English Language Learners Email'])
#    .apply(lambda x: x.str.split(';').explode())
#    .reset_index()) 
def tidy_split(df, column, sep=';', keep=False):
    """
    Split the values of a column and expand so the new DataFrame has one split
    value per row. Filters rows where the column is missing.

    Params
    ------
    df : pandas.DataFrame
        dataframe with the column to split and expand
    column : str
        the column to split and expand
    sep : str
        the string used to split the column's values
    keep : bool
        whether to retain the presplit value as it's own row

    Returns
    -------
    pandas.DataFrame
        Returns a dataframe with the same columns as `df`.
    """
    indexes = list()
    new_values = list()
    #df = df.dropna(subset=[column])
    for i, presplit in enumerate(df[column].astype(str)):
        values = presplit.split(sep)
        if keep and len(values) > 1:
            indexes.append(i)
            new_values.append(presplit)
        for value in values:
            indexes.append(i)
            new_values.append(value)
    new_df = df.iloc[indexes, :].copy()
    new_df[column] = new_values
    return new_df

# df1=tidy_split(df, 'Supt', sep=';')
# df2=tidy_split(df, 'Galaxy Location Codes', sep=';')
# df3=tidy_split(df, 'District(s)', sep=';')
# df4=tidy_split(df, 'Superintendent Address', sep=';')
# df5=tidy_split(df, 'Main District Office Room Number', sep=';')
# df6=tidy_split(df, 'Superintendent', sep=';')
# df7=tidy_split(df, 'Superintendent Email', sep=';')
# df8=tidy_split(df, 'Executive Director of School Support and Operations', sep=';')
# df9=tidy_split(df, 'Executive Director of School Support and Operations Email', sep=';')
# df10=tidy_split(df, 'Deputy Superintendent', sep=';')
# df11=tidy_split(df, 'Deputy Superintendent Email', sep=';')
# df12=tidy_split(df, 'Admin Assistant', sep=';')
# df13=tidy_split(df, 'Admin Assistant Email', sep=';')
# df14=tidy_split(df, 'Teacher Development and Evaluation Coach', sep=';')
# df15=tidy_split(df, 'TDEC Email', sep=';')
# df16=tidy_split(df, 'Field Support Liaison / Special Instruction Liaison', sep=';')
# df17=tidy_split(df, 'Field Support Liaison / Special Instruction Liaison Email', sep=';')
# df18=tidy_split(df, 'Director for Continuous Improvement', sep=';')
# df19=tidy_split(df, 'Director for Continuous Improvement Email', sep=';')
# df20=tidy_split(df, 'Family Leadership Coordinator', sep=';')
# df21=tidy_split(df, 'Family Leadership Coordinator Email', sep=';')
# df22=tidy_split(df, 'Family Support Coordinator', sep=';')
# df23=tidy_split(df, 'FSC Email', sep=';')
# df24=tidy_split(df, 'Student Services Manager', sep=';')
# df25=tidy_split(df, 'Student Services Manager Email', sep=';')
# df26=tidy_split(df, 'Academic Policy and Performance & Assessment Leads', sep=';')
# df27=tidy_split(df, 'Academic Policy and Performance & Assessment Leads - Email', sep=';')
# df28=tidy_split(df, 'Director for Special Education', sep=';')
# df29=tidy_split(df, 'Director for Special Education Email', sep=';')
# df30=tidy_split(df, 'Administrator of Special Education', sep=';')
# df31=tidy_split(df, 'Administrator of Special Education Email', sep=';')
# df32=tidy_split(df, 'Specialized Student Support Lead', sep=';')
# df33=tidy_split(df, 'Specialized Student Support Lead Email', sep=';')
# df34=tidy_split(df, 'Director for Multilingual Learners/English Language Learners', sep=';')
# df35=tidy_split(df, 'Director for Multilingual Learners/English Language Learners Email', sep=';')
# df36=tidy_split(df, 'MLL Services Administrator', sep=';')
# df37=tidy_split(df, 'MLL Services Administrator Email', sep=';')
# join all cleaned columns to merge into a new dataframe
# df = pd.concat([df1[Supt],df2[Galaxy Location Codes]])
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
    print(str(e.value[1]))
except odbc.Error as e:
    print('Connection Error')
    print(str(e.value[1]))
else:
    cursor = conn.cursor()
    sql_insert = """
        TRUNCATE TABLE [SEO_REPORTING].[Wang].[lk_SuperDist]
        INSERT INTO [SEO_REPORTING].[Wang].[lk_SuperDist]
        VALUES(?, ?, ?, ?, ?, 
               ?, ?, ?, ?, ?, 
               ?, ?, ?, ?, ?, 
               ?, ?, ?, ?, ?, 
               ?, ?, ?, ?, ?, 
               ?, ?, ?, ?, ?, 
               ?, ?, ?, ?, ?, ?, ?)
    """
    sql_clean="""
        TRUNCATE TABLE [SEO_REPORTING].[Wang].[lk_SuperDist_Cleaned]
        INSERT INTO [SEO_REPORTING].[Wang].[lk_SuperDist_Cleaned]
        VALUES(?, ?, ?, ?, ?, 
               ?, ?, ?, ?, ?, 
               ?, ?, ?, ?, ?, 
               ?, ?, ?, ?, ?, 
               ?, ?, ?, ?, ?, 
               ?, ?, ?, ?, ?, 
               ?, ?, ?, ?, ?, ?, ?)
        TRUNCATE TABLE [SEO_REPORTING].[Wang].[lk_SuptDistrict]
        INSERT INTO [SEO_REPORTING].[Wang].[lk_SuptDistrict] (
        --[SuperintendentLocationCodeID] -- This is the incremental PK
            ,[SourceName]
            ,[SourceLocationCode]
            ,[SuperintendentLocationCode] 
            ,[GalaxyLocationCode] 
            ,[District] 
            ,[SuperintendentAddress]
            ,[RoomNumber] 
            ,[ProcessedBy] 
            ,[ProcessedDate]
        ) 
        SELECT
            'GoogleSheet',
            ,[SuperintendentLocationCode]
            ,[SuperintendentLocationCode]
            ,[GalaxyLC]
            ,[District]
            ,[SuperintendentAdress]
            ,[DistrictOffRoomNum]
            ,'Wang'
            ,getdate()
        FROM
            [SEO_REPORTING].[Wang].[lk_SuperDist_Cleaned]

        TRUNCATE TABLE [SEO_REPORTING].[Wang].[lk_SuptDistrictStaff] 
        INSERT INTO [SEO_REPORTING].[Wang].[lk_SuptDistrictStaff] 
        ([SuperintendentLocationCode] 
            ,[StaffRole]
            ,[StaffName]
            ,[StaffEmail]
            ,[ProcessedBy]
            ,[ProcessedDate]
        )
        SELECT [SuperintendentLocationCode]
        ,
        FROM [SEO_REPORTING].[Wang].[lk_SuperDist_Cleaned]
    """
    try:
        cursor.executemany(sql_insert, rows_original)
        cursor.commit()
        cursor.executemany(sql_clean, df)
        cursor.commit()
        print('Data import complete')
    except Exception as e:
        print(str(e.value[1]))
        cursor.rollback()
    finally:
        cursor.close()
        conn.close()
