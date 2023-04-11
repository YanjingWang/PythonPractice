import pyodbc
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
# print(StudentID, MatchKeyDuration) #return two lists
# print(MatchKeyDuration[0])
# print(StudentID[0])
ID_MatchKey_dict = dict(zip(StudentID, MatchKeyDuration))
Sorted_ID_MatchKey_dict = dict(
    sorted(ID_MatchKey_dict.items(), key=lambda x: x[0]))
# print(Sorted_ID_MatchKey_dict)
sql_RSProvisioning = "select  FirstAttendDate,MatchKeyDuration, * from SergeyG.RPT_RSProvisioning A WHERE FirstAttendDate is null and StudentID = ? and SCHOOLYEAR= '2022-2023' -- ORDER BY StudentID"
sql_INT_PA = "select  FirstAttendDate,MatchKeyDuration, * from SergeyG.INT_ProviderAssignment WHERE StudentID = ? and MatchKeyDuration= ? and SCHOOLYEAR= '2022-2023' and CreatedBy in ('Charter Initial Load','Initial Load') -- ORDER BY StudentID"
# loop through each element of the list and execute a SQL Server query with it as a variable
for element in StudentID:
    cursor.execute(sql_RSProvisioning, element)
    rows_rs = cursor.fetchall()
    # print(rows_rs)
    # print(type(rows)) #<class 'list'>
for i, j in zip(StudentID, MatchKeyDuration):
    cursor.execute(sql_INT_PA, (i, j))
    rows_pa = cursor.fetchall()
    # print(rows_pa)
    # compare two sql returned result: try catch senario 1: both NULL 2.real issue arose 3.mapping consusion  4. StudentID doesn't exist in PA
    # only 2. is real issue
    # figure out Charter Encounters drop out poior 9/1, maybe it drop out from PA because it has EA???
