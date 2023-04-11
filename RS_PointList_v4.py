from openpyxl import load_workbook
import os  # os.getcwd()
import numpy as np
# https://www.youtube.com/watch?v=1qMR1OjoeTM&list=PL3JVwFmb_BnSee8RFaRPZ3nykuMRlaQp1&index=24
import pandas as pd
import pypyodbc as odbc  # conda install -c conda-forge pyp
import datetime
import time
from datetime import date


os.chdir(r"C:\Users\Ywang36\Downloads")
# rs point list 2023 updated 08-29-22 # rs point list 2023 updated 08-29-22 11-21-22 #rs point list 2023 updated 08-29-22 11-21-22
df = pd.read_excel(
    'rs point list 2023 updated 08-29-22 03-31-23.xlsx', header=0)
df = pd.DataFrame(df)
df = df.applymap(str)
df = df[["DBN RPT", "LastName", "FirstName",
         "RoleName", "EmailAddress", "UserID"]]
df.rename(columns={'DBN RPT': 'DBN', 'UserID': 'UserName'},
          inplace=True)  # 2404 eows


# drop all rows that both emailaddress column and username columns are empty
# df = df.dropna(subset=['EmailAddress', 'UserName'], how='any')
# df=df.dropna(subset=['EmailAddress', 'UserName'], how='any') # should be 2392

# if username is nan then extract strings before @ in emailaddress column
# https://www.geeksforgeeks.org/python-string-till-substring/
# iterate rows: https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas
for index, row in df.iterrows():
    # print(row['UserName'],row['EmailAddress'])
    if row['EmailAddress'] == 'nan' and row['UserName'] == 'nan':
        df.drop(index, inplace=True)  # 2396 rows, dropped 8 blank rows
        # print(row)

for index, row in df.iterrows():
    # print(row['UserName'],row['EmailAddress'])
    if row['UserName'] == 'nan' and row['EmailAddress'] != 'nan':
        # print(row['UserName'],row['EmailAddress'])
        # print(type(row['UserName']))
        # print(type(row['EmailAddress']))
        spl_word = '@'
        row['UserName'] = row['EmailAddress'].partition(spl_word)[0]

# https://sparkbyexamples.com/pandas/pandas-drop-rows-with-nan-values-in-dataframe/#:~:text=By%20using%20dropna()%20method,you%20should%20use%20inplace%3DTrue%20.
# handle irregular missing value:  EmailAddress cell and UserName cell were merged as ONE cell instead of two
# fill empty values with NaN https://stackoverflow.com/questions/13445241/replacing-blank-values-white-space-with-nan-in-pandas
df = df.replace(r'^\s*$', np.nan, regex=True)
df = df.dropna(subset=['UserName'], axis=0)
print(df[df.columns[0]].count())
df = df.drop_duplicates()
print(df[df.columns[0]].count())
# df_unsplited = df[df['DBN'] == '22KP22'] #2393 SHOULD BE THE ROGHT COUNTS INSTEAD OF 2396'15K592','20K062','22KP22'
# df_unsplited
# df
##########################################################################################################################
##########################################################################################################################
df = df.drop(['FirstName', 'LastName', 'EmailAddress'],
             axis=1)  # which is first???
# https://stackoverflow.com/questions/71142305/dropping-duplicate-rows-ignoring-case-lowercase-or-uppercase
df = df.drop_duplicates()  # print(df)
print(df[df.columns[0]].count())
# df = df.groupby(df['UserName'].str.lower(), as_index=False, sort=False).first()
# df = df[~df['UserName'].str.lower().duplicated()]
list2 = ['afernandez', 'ccapetanakis']
# drop rows from above list
df = df[df.UserName.isin(list2) == False]
# swap columns


def swap_columns(df, col1, col2):
    col_list = list(df.columns)
    x, y = col_list.index(col1), col_list.index(col2)
    col_list[y], col_list[x] = col_list[x], col_list[y]
    df = df[col_list]
    return df


cleaned_data = swap_columns(df, "RoleName", "UserName")
cleaned_data
print(cleaned_data[cleaned_data.columns[0]].count())
##########################################################################################################################
##########################################################################################################################
# read data from sql and output it as a table code copied from : https://www.statology.org/swap-columns-pandas/
# https://stackoverflow.com/questions/50862705/in-python-display-output-of-sql-query-as-a-table-just-like-it-does-in-sql
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


conn = odbc.connect(connection_stirng(DRIVER_NAME, SERVER_NAME, DATABASE_NAME))
print('Connection created')
cursor = conn.cursor()
stri = "select distinct \
 			a.[SchoolDBN] as DBN \
,upper(left(a.principalemail, charindex('@', principalemail) - 1)) as UserName\
,a.PrincipalTitle \
 		FROM [SEO_MART].[dbo].[RPT_Locations] as a \
			where Schooltype = 'CSD' \
 				and ActiveFlag = 'Y'--1619 \
			and a.principalemail is not null"
cursor.execute(stri)
data = cursor.fetchall()
cursor.commit()
cursor.close()
conn.close()

sql_data = pd.DataFrame(data)  # RPT LOCATION table PS reports, appending union
sql_data.columns = ['DBN', 'UserName', 'RoleName']


unioned_data = pd.concat([cleaned_data, sql_data])
# unioned_data = unioned_data.reset_index(drop=True) # drop the index of dataframe
unioned_data = unioned_data.dropna(subset=["UserName", "RoleName"], how='any')
unioned_data = unioned_data.drop_duplicates()  # print(df)
######################################################################################################
######################################################################################################
# determining the name of the file
file_name = 'RSPointList_{0}.xlsx'.format(date.today().strftime("%m%d%Y"))
# saving the excel
unioned_data.to_excel(file_name, index=False)
print(cleaned_data[cleaned_data.columns[0]].count())


# code is copied from: https://www.youtube.com/watch?v=WH46-L2eM-k
wb = load_workbook(filename=file_name)
ws = wb.active
ws.title = "RSPointList"
wb.save(file_name)
