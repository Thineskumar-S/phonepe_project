import mysql.connector



connection_object = mysql.connector.connect(
host=connection_string,
user=user_name,
password=password)

cursor_object=connection_object.cursor()