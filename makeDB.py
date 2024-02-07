import sqlite3

conn = sqlite3.connect('.\GetCSVFromChinook\Chinook.db')


cursor = conn.cursor()

with open('.\GetCSVFromChinook\Chinook_Sqlite.sql', 'r', encoding="UTF-8") as sql_file:
    sql_script = sql_file.read()

cursor.executescript(sql_script)


conn.commit()


conn.close()