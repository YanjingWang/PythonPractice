import os #os.getcwd()
import numpy as np
import pandas as pd # https://www.youtube.com/watch?v=1qMR1OjoeTM&list=PL3JVwFmb_BnSee8RFaRPZ3nykuMRlaQp1&index=24
import pypyodbc as odbc # conda install -c conda-forge pyp
import datetime
import time
from datetime import date

os.chdir(r"C:\Users\Ywang36\Downloads")
df = pd.read_excel('rs point list 2023 updated 08-29-22 11-14-23.xlsx',header=0)
df = pd.DataFrame(df)
df =df.applymap(str)
df = df[["DBN RPT","LastName","FirstName","RoleName","EmailAddress","UserID"]]
df.rename(columns = {'DBN RPT':'DBN','UserID':'UserName'}, inplace = True)
# code copied from: https://stackoverflow.com/questions/39128856/python-drop-row-if-two-columns-are-nan
df=df.dropna(subset=["EmailAddress", "UserName"], how='any')
# ls = [x.split() for x in df["LastName"] ]
# print((ls[0][0]), (ls[1][0]))
# code is copied from : https://stackoverflow.com/questions/71377372/how-to-extract-text-before-the-last-space-in-a-dataframe-column

# df['LastName']=df['LastName'].str.rsplit(' ', 0, expand=True) [0] #the first o means split by first whitespace
# df['LastName']=df['LastName'].str.rsplit('-', 0, expand=True) [0]
# df["UserName"]=df.loc[df["UserName"].isnull(),'UserName'] = df["FirstName"].str[:1] + df["LastName"] 
# df["EmailAddress"]=df.loc[df["EmailAddress"].isnull(),'EmailAddress'] = df["FirstName"].str[:1] + df["LastName"] + "@SCHOOLS.NYC.GOV"

# df.loc[df["UserName"] == '','UserName'] = df["FirstName"].str[:1] + df["LastName"]
# df.loc[df["EmailAddress"] == '','EmailAddress'] = df["FirstName"].str[:1] + df["LastName"]+"@SCHOOLS.NYC.GOV"
# df.["UserName"] = df.["UserNmae"].str.strip().replace('', np.nan).fillna(df["FirstName"].str[:1])
# df['UserName'] = df['UserName'].replace('', pd.NA).fillna(df["FirstName"].str[:1])
# df['UserName'] = (df['UserName'].str.strip()
#                                           .replace('',np.nan)
#                                           .groupby(df['EmailAddress'])
#                                           .transform(lambda x: x.bfill().ffill()))
# df = df["DBN"]+df["LastName"]+df["FirstName"]+df["RoleName"]+df["EmailAddress"]+df["UserName"] 
# df1=df['EmailAddress'].str.split('@').str[0]
# df1 = pd.DataFrame(df1)
# df1.columns=['extrated_username_from_email']
# df = pd.concat([df1, df], axis=1, join='inner')
# df=df.drop(['UserName'], axis=1)
# df=df.rename(columns={"extrated_username_from_email": "UserName"})
# df["EmailAddress"]=df.loc[df["EmailAddress"].isnull(),'EmailAddress'] = df["FirstName"].str[:1] + df["LastName"] + "@SCHOOLS.NYC.GOV"
df["UserName"]=df.loc[df["UserName"].isnull(),'UserName'] = df['EmailAddress'].str.split('@').str[0]
check_for_nan = df['UserName'].isnull().values.any()
print (check_for_nan)

df = df.drop_duplicates() #print(df)
df = df.drop(['FirstName', 'LastName','EmailAddress'], axis=1)
# code copied from : https://www.statology.org/swap-columns-pandas/
def swap_columns(df, col1, col2):
    col_list = list(df.columns)
    x, y = col_list.index(col1), col_list.index(col2)
    col_list[y], col_list[x] = col_list[x], col_list[y]
    df = df[col_list]
    return df
cleaned_data = swap_columns(df, "RoleName", "UserName")


# read data from sql and output it as a table
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
unioned_data =unioned_data.dropna(subset=["UserName", "RoleName"], how='any')
check_for_nan = df['RoleName'].isnull().values.any()
print (check_for_nan)
# unioned_data = unioned_data.reset_index(drop=True) # drop the index of dataframe 

# determining the name of the file
file_name = 'RSPointList_{0}.xlsx'.format(date.today().strftime("%m%d%Y")) 
# saving the excel
unioned_data.to_excel(file_name,index=False)

