import pandas as pd
import  sqlite3

db_name = "STAFF.db"
table_name = "Departments"
attributes = ['DEFT_ID','DEP_NAME','MANAGER_ID','LOC_ID']

df = pd.read_csv("Departments.csv",names=attributes)

conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists="replace", index=False)

dict = {'DEFT_ID':['9'],'DEP_NAME':['Quality Assurance'],'MANAGER_ID':["30010"],'LOC_ID':['L0010']}
data_append = pd.DataFrame(dict)

data_append.to_sql(table_name, conn, if_exists='append', index=False)

querry = f'SELECT * FROM {table_name}'
querry_out = pd.read_sql(querry, conn)
print(querry_out)

conn.close()