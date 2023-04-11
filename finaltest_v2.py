from sqlalchemy import create_engine
import pyodbc
import pandas as pd
from tabulate import tabulate

# # print list of available ODBC drivers
# print(pyodbc.drivers())
# establish a connection to the SQL Server
conn = pyodbc.connect(
    'Driver={SQL Server Native Client 11.0};Server=ES00VPADOSQL180,51433;Database=SEO_REPORTING;Trusted_Connection=yes;')
# create a cursor to execute SQL statements
cursor = conn.cursor()
# execute a SQL Server query and fetch the results into a list
query_result = cursor.execute("select  A.StudentID,  A.MatchKeyDuration  from SergeyG.RPT_RSProvisioning A \
                                JOIN SergeyG.INT_ProviderAssignment B on A.StudentID = B.StudentID \
                                where A.FirstAttenddate IS NULL AND B.FirstAttenddate IS NOT NULL \
                                AND B.SCHOOLYEAR= '2022-2023' AND A.SCHOOLYEAR= '2022-2023' \
                                AND A.MatchKeyDuration = B.MatchKeyDuration \
                                AND B.CreatedBy in ('Charter Initial Load','Initial Load') \
                                ORDER BY StudentID").fetchall()
StudentID = [row[0] for row in query_result]
MatchKeyDuration = [row[1] for row in query_result]
print(len(MatchKeyDuration))
print(len(StudentID))

ID_MatchKey_dict = dict(zip(StudentID, MatchKeyDuration))
Sorted_ID_MatchKey_dict = dict(
    sorted(ID_MatchKey_dict.items(), key=lambda x: x[0]))
# print(Sorted_ID_MatchKey_dict)
sql_RSProvisioning = "select  FirstAttendDate,MatchKeyDuration from SergeyG.RPT_RSProvisioning A WHERE FirstAttendDate is null and StudentID = ? and SCHOOLYEAR= '2022-2023' -- ORDER BY StudentID"
sql_INT_PA = "select  FirstAttendDate,MatchKeyDuration from SergeyG.INT_ProviderAssignment WHERE StudentID = ? and MatchKeyDuration= ? and SCHOOLYEAR= '2022-2023' and CreatedBy in ('Charter Initial Load','Initial Load') -- ORDER BY StudentID"
# loop through each element of the list and execute a SQL Server query with it as a variable
for element in StudentID:
    cursor.execute(sql_RSProvisioning, element)
    lists_rs = cursor.fetchall()
    print(lists_rs)
    # print(tabulate(lists_rs, headers='firstrow', tablefmt='grid'))
for i, j in zip(StudentID, MatchKeyDuration):
    cursor.execute(sql_INT_PA, (i, j))
    lists_pa = cursor.fetchall()
    print(lists_pa)
    # print(tabulate(lists_rs, headers='firstrow', tablefmt='grid'))

"""
rs is a list of lists. Each inner list contains one or two tuples. 
Each tuple has two elements: the first element is either None or a datetime.date object representing a date, 
and the second element is a string that appears to contain an identification number followed by a description of a speech-language therapy group in English.
If rs is a list of lists, the output should be <class 'list'>.
"""
###########################################################################################

# Replace these values with your own
server = 'ES00VPADOSQL180,51433'
database = 'SEO_REPORTING'
# username = 'CENTRAL\ywang36'
# password = 'your_password'

# # Create a connection string
# conn_str = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'
# Create a connection string
conn_str = f'mssql+pyodbc://{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes'

# Create an engine
engine = create_engine(conn_str)


# df_rs = pd.DataFrame(lists_rs, columns=['IndiceIDMKDur'])
# df_pa = pd.DataFrame(lists_rs, columns=['IndiceIDMKDur'])

# Save the DataFrame as a SQL Server table
# df_rs.to_sql('rs_table', engine, index=False, if_exists='replace')
# df_pa.to_sql('pa_table', engine, index=False, if_exists='replace')

# lists_rs.to_sql('rs_table', engine, index=False, if_exists='replace')
# lists_pa.to_sql('pa_table', engine, index=False, if_exists='replace')

# Create a new table
cursor.execute('''
    DROP TABLE IF EXISTS [dbo].[rs_table];
    CREATE TABLE rs_table (
        FirstAttendDate datetime,
        MatchKeyDuration varchar(255)
    )
''')

# Insert the data from list_rs into the table
for item in lists_rs:
    cursor.execute(
        'INSERT INTO rs_table (FirstAttendDate, MatchKeyDuration) VALUES (?, ?)', item)

# Commit the changes and close the connection
conn.commit()
conn.close()
