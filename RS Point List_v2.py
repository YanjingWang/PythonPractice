import os #os.getcwd()
import numpy as np
import pandas as pd # https://www.youtube.com/watch?v=1qMR1OjoeTM&list=PL3JVwFmb_BnSee8RFaRPZ3nykuMRlaQp1&index=24
import pypyodbc as odbc # conda install -c conda-forge pyp
import datetime
import time
from datetime import date


os.chdir(r"C:\Users\Ywang36\Downloads")
df = pd.read_excel('rs point list 2023 updated 08-29-22 11-14-23.xlsx',header=0) # rs point list 2023 updated 08-29-22
df = pd.DataFrame(df)
df =df.applymap(str)
df = df[["DBN RPT","LastName","FirstName","RoleName","EmailAddress","UserID"]]
df.rename(columns = {'DBN RPT':'DBN','UserID':'UserName'}, inplace = True)

# drop all rows that both emailaddress column and username columns are empty
df = df.dropna(subset=['EmailAddress', 'UserName'], how='all')
# df=df.dropna(subset=['EmailAddress', 'UserName'], how='any') # should be 2392

# if username is nan then extract strings before @ in emailaddress column
# https://www.geeksforgeeks.org/python-string-till-substring/
# iterate rows: https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas

for index, row in df.iterrows():
    #print(row['UserName'],row['EmailAddress'])
    if row['UserName'] == 'nan':
        #print(row['UserName'],row['EmailAddress'])
        #print(type(row['UserName']))
        #print(type(row['EmailAddress']))
        spl_word = '@'
        row['UserName']=row['EmailAddress'].partition(spl_word)[0]

df = df.drop_duplicates() #print(df)
df = df.drop(['FirstName', 'LastName','EmailAddress'], axis=1)

# swap columns 
def swap_columns(df, col1, col2):
    col_list = list(df.columns)
    x, y = col_list.index(col1), col_list.index(col2)
    col_list[y], col_list[x] = col_list[x], col_list[y]
    df = df[col_list]
    return df
cleaned_data = swap_columns(df, "RoleName", "UserName")


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

sql_data = pd.DataFrame(data) #RPT LOCATION table PS reports, appending union
sql_data.columns =['DBN', 'UserName', 'RoleName']


unioned_data = pd.concat([cleaned_data, sql_data])
# unioned_data = unioned_data.reset_index(drop=True) # drop the index of dataframe 
unioned_data =unioned_data.dropna(subset=["UserName", "RoleName"], how='any')

# determining the name of the file
file_name = 'NewRSPointList_{0}.xlsx'.format(date.today().strftime("%m%d%Y")) 
# saving the excel
unioned_data.to_excel(file_name,index=False)


# verify whether it's same with manual excel
# https://stackoverflow.com/questions/56235226/pandas-analogue-to-sql-minus-except-operator-using-multiple-columns
# 
#df2 = df.set_index('col1').subtract(df1.set_index('col1'), axis='columns')

