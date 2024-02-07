import pandas as pandas
import sqlite3 as sql

conn = sql.connect(".\GetCSVFromChinook\Chinook.db")

query = "SELECT * FROM Customer;"

df = pandas.read_sql_query(query, conn)

print(df.head())

#outputFile = ".\GetCSVFromChinook\output\\test.csv"

#df.to_csv(outputFile, index=True)

conn.close()