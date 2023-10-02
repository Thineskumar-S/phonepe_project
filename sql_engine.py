import mysql.connector
import os
import csv


connection_string="phonepeproject.cwoakibr9oeh.ap-south-1.rds.amazonaws.com"
user_name="Thinesh"
password="Thinesh1234"
connection_object = mysql.connector.connect(
host=connection_string,
user=user_name,
password=password)

cursor_object=connection_object.cursor()


"""
# agg_trans_years
create_query="create table if not exists agg_trans_years (Time date,Quater varchar(10),Categories varchar(100),type varchar(20),count int, amount decimal(18,4))"
insert_query="insert into agg_trans_years (Time,Quater,categories,type,count,amount) values (%s,%s,%s,%s,%s,%s)"
file_path=r"G:\phonepe project\data\agg_trans_years.csv"

#agg_trans_years_states
create_query="create table if not exists agg_trans_years_states  (state varchar(100),Time date,Quater varchar(10),Categories varchar(100),type varchar(20),count int, amount decimal(18,4))"
insert_query="insert into agg_trans_years_states (state,Time,Quater,categories,type,count,amount) values (%s,%s,%s,%s,%s,%s,%s)"
file_path=r"G:\phonepe project\data\agg_trans_years_states.csv"

#agg_user_year

create_query="create table if not exists agg_user_years  (year year,Quater varchar(3),users int,app_opens int, brand varchar(50),count int,percentage decimal(15,10))"
insert_query="insert into agg_user_years (year,Quater,users,app_opens,brand,count,percentage) values (%s,%s,%s,%s,%s,%s,%s)"
file_path=r"G:\phonepe project\data\agg_user_years.csv"

#agg_user_states


# map_trans_states
create_query="create table if not exists map_trans_states (state varchar(100),year year,Quater varchar(3),District varchar(100),count int,amount decimal(20,10))"
insert_query="insert into map_trans_states (state,year,quater,district,count,amount) values (%s,%s,%s,%s,%s,%s)"
file_path=r"G:\phonepe project\data\map_trans_states.csv"

# map_trans_years


#map_user_states
create_query="create table if not exists map_user_states (state varchar(100),year year,Quater varchar(3),District varchar(100),users int, appopens int)"
file_path=r"G:\phonepe project\data\map_user_states.csv"

#map_users_years

create_query="create table if not exists map_user_years (year year,Quater varchar(3),state varchar(100),count int, amount int)"
file_path=r"G:\phonepe project\data\map_user_years.csv"

#top_trans_states_districts

create_query="create table if not exists top_trans_states_districts (state varchar(100),year year,Quater varchar(3),district varchar(100),count int, amount int)"
file_path=r"G:\phonepe project\data\top_trans_states_districts.csv"

# top_trans_states_pincodes
file_path1=r"G:\phonepe project\data\top_trans_states_pincodes.csv"
create_query1="create table if not exists top_trans_states_pincodes (state varchar(100),year year,Quater varchar(3),pincodes int,count int , amount decimal(18,9))"


# top_user_states_districts

create_query="create table if not exists top_user_states_districts (state varchar(100),year year,Quater varchar(3),name varchar(100), registered_users int)"
file_path=r"G:\phonepe project\data\top_user_states_districts.csv"

# top_user_states_pinocdes

create_query="create table if not exists top_user_states_pincode (state varchar(100),year year,Quater varchar(3), registered_users int)"
file_path=r"G:\phonepe project\data\top_user_states_pincode.csv"

# top_user_year_district

create_query="create table if not exists top_user_year_district (year year,Quater varchar(3), district varchar(100),registred_users int)"
file_path=r"G:\phonepe project\data\top_user_year_district.csv"

# top_user_year_pincode

create_query="create table if not exists top_user_year_pincode (year year,Quater varchar(3), pincode int ,registred_user int)"
file_path=r"G:\phonepe project\data\top_user_year_pincode.csv"

# top_user_year_state

create_query="create table if not exists top_user_year_state (year year,Quater varchar(3), state varchar(100),registered_users int)"
file_path=r"G:\phonepe project\data\top_user_year_state.csv"
"""
def load_data(create_query,file_path):
    cursor_object.execute('use phonepe')
    table_name=os.path.basename(file_path)
    with open(file_path,"r") as file:
        csv_reader=csv.reader(file)
        header=next(csv_reader,None)
        placeholders = ",".join(["%s" for _ in header])
        table_name=os.path.basename(file_path)
        table_name=table_name[0:-4]
        insert_query=f"insert into {table_name} ({','.join(header)}) values({placeholders})"
        cursor_object.execute(create_query)
        x=[tuple(row) for row in csv_reader]
        cursor_object.executemany(insert_query,x)
            
