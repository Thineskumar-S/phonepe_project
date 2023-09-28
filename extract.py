import os
import json
import datetime
import pandas as pd 
import re


# driver function
def to_csv(main_path,dest_path,function1,function2):
    """ 
    Fun descritpion: this function takes 
    user defined functions as parameters
    and converts extracted data 
    to csv format.

    parms: 1.main_path= path to be declared during runtime.
    2.func1, func2 -> user defined functions.

    output= this function outputs csv file. 

    """ 
    main_path=main_path
    result=function1(main_path,function2)
    csv_name=function2.__name__
    extention=csv_name+".csv"
    csv_path=os.path.join(dest_path,extention)
    result.to_csv(csv_path,index=False)




"""
agg_main_path="G:\\phonepe project\\pulse\\data\\aggregated\\transaction\\country\\india"
os.chdir(main_path)
"""
#file_path_years
def years_path(main_path,function):
    os.chdir(main_path)    
    transaction=[]
    years=os.listdir()
    for year in years:
        if year=='state':
            break
        else:
            year_path=os.path.join(main_path,year)
            os.chdir(year_path)
            quaters=os.listdir()
            for quater in quaters:
                quater_path=os.path.join(year_path,quater)
                file_path=(quater_path)
                with open(file_path,'r') as file:
                    data=json.load(file)
                    results=function(data,file_path)
                    for result in results:
                        transaction.append(result)
    df=pd.DataFrame(transaction)
    return df

# states navigation

def states_path(main_path,function):
        os.chdir(main_path)    
        transaction=[]
        years=os.listdir()
        for year in years:
               if year=='state':                 
                            state_dir=os.path.join(main_path,year)
                            os.chdir(state_dir)
                            states=os.listdir()
                            for state in states:
                                    state_subfolder= os.path.join(state_dir,state)
                                    os.chdir(state_subfolder)
                                    state_years=os.listdir()
                                    for state_year in state_years:
                                                state_years_path =os.path.join(state_subfolder,state_year)
                                                os.chdir(state_years_path)
                                                quaters=os.listdir()
                                                for quater in quaters:
                                                        file_path=os.path.join(state_years_path,quater)
                                                        with open(file_path,'r') as file:
                                                           data=json.load(file)
                                                        results=function(data,file_path)
                                                        for result in results:
                                                                transaction.append(result)
               else:continue
        df=pd.DataFrame(transaction)
        return df


# agg ->transaction
def agg_trans_years(data,file_path):
    file_path=file_path

    start_time_seconds=(data['data']['from'])/1000
    end_time_seconds=data['data']['to']/1000

    s_time=datetime.datetime.fromtimestamp(start_time_seconds)
    e_time=datetime.datetime.fromtimestamp(end_time_seconds)
    # Define a function to find the quarter for a given month
    def find_quarter(month):
        if month in range(1, 4):
            return 'Q1 (J,F,M) '
        elif month in range(4, 7):
            return 'Q2 (A,M,J) '
        elif month in range(7, 10):
            return 'Q3 (J,A,S)'
        else:
            return 'Q4 (O,N,D)'

    # Find the quarters for the given timestamps
    quarter1 = find_quarter(s_time.month)
    quarter2 = find_quarter(e_time.month)

    # Determine the common quarter
    if quarter1 == quarter2:
        common_quarter = quarter1
    else:
        common_quarter = quarter1,quarter2
    length=len(data['data']['transactionData'])
    total_data=[]
    for i in range(length):

        extracted_data={'Time':s_time,
        "Quater":common_quarter,
        'categories':data['data']['transactionData'][i]['name'],
        'type':data['data']['transactionData'][i]['paymentInstruments'][0]['type'],
        'count':data['data']['transactionData'][i]['paymentInstruments'][0]['count'],
        'amount':data['data']['transactionData'][i]['paymentInstruments'][0]['amount']}
        total_data.append(extracted_data)

    
    return total_data

#agg_data_extract_state
def agg_trans_years_states(data,file_path):
    pattern = r'\\state\\([a-zA-Z&-]+)\\'

    # Use re.search to find the match
    match = re.search(pattern, file_path)

    state = match.group(1)
    start_time_seconds=(data['data']['from'])/1000
    end_time_seconds=data['data']['to']/1000

    s_time=datetime.datetime.fromtimestamp(start_time_seconds)
    e_time=datetime.datetime.fromtimestamp(end_time_seconds)
    # Define a function to find the quarter for a given month
    def find_quarter(month):
        if month in range(1, 4):
            return 'Q1 (J,F,M) '
        elif month in range(4, 7):
            return 'Q2 (A,M,J) '
        elif month in range(7, 10):
            return 'Q3 (J,A,S)'
        else:
            return 'Q4 (O,N,D)'

    # Find the quarters for the given timestamps
    quarter1 = find_quarter(s_time.month)
    quarter2 = find_quarter(e_time.month)

    # Determine the common quarter
    if quarter1 == quarter2:
        common_quarter = quarter1
    else:
        common_quarter = quarter1,quarter2
    length=len(data['data']['transactionData'])
    total_data=[]
    for i in range(length):

        extracted_data={'state':state,'Time':s_time,
        "Quater":common_quarter,
        'categories':data['data']['transactionData'][i]['name'],
        'type':data['data']['transactionData'][i]['paymentInstruments'][0]['type'],
        'count':data['data']['transactionData'][i]['paymentInstruments'][0]['count'],
        'amount':data['data']['transactionData'][i]['paymentInstruments'][0]['amount']}
        total_data.append(extracted_data)
    return total_data

"""
main_path="G:\\phonepe project\\pulse\\data\\aggregated\\user\\country\\india"
"""

  # agg -> user

# agg users data extract
def agg_user_years(data,file_path):
    pattern = r'\\(\d{4})\\(\d+)\.json'

    match = re.search(pattern, file_path)
    if match:
        year = match.group(1)
        quarter = match.group(2)
        # Format the quarter as Q1, Q2, etc.
        formatted_quarter = f'Q{quarter}'
    
    total_data=[]
    if data['data']['usersByDevice']:
        length=len(data['data']['usersByDevice'])
        for i in range(length):
            extracted_data={'year':year,"Quater":formatted_quarter,
                'users':data['data']['aggregated']['registeredUsers'],
                'app_opens':data['data']['aggregated']['appOpens'],
                'brand':data['data']['usersByDevice'][i]['brand'],
                'count':data['data']['usersByDevice'][i]['count'],
                'percentage':data['data']['usersByDevice'][i]['percentage']
                }

            total_data.append(extracted_data)
    else:
        extracted_data={'year':year,"Quater":formatted_quarter,
                'users':data['data']['aggregated']['registeredUsers'],
                'app_opens':data['data']['aggregated']['appOpens']}
        total_data.append(extracted_data)
    return total_data
#agg user states
def agg_user_states(data,file_path):
    pattern = r'\\state\\([a-zA-Z&\-]+)\\(\d{4})\\(\d+)\.json'

    # Use re.search to find the matches
    match = re.search(pattern, file_path)

    if match:
        state = match.group(1)
        year = match.group(2)
        quarter = match.group(3)
        formatted_quarter = f'Q{quarter}'
    total_data=[]

    if data['data']['usersByDevice']:
        length=len(data['data']['usersByDevice'])
        for i in range(length):
            extracted_data={"state":state,'year':year,"Quater":formatted_quarter,
                'users':data['data']['aggregated']['registeredUsers'],
                'app_opens':data['data']['aggregated']['appOpens'],
                'brand':data['data']['usersByDevice'][i]['brand'],
                'count':data['data']['usersByDevice'][i]['count'],
                'percentage':data['data']['usersByDevice'][i]['percentage']
                }

            total_data.append(extracted_data)
    else:
        extracted_data={'year':year,"Quater":formatted_quarter,
                'users':data['data']['aggregated']['registeredUsers'],
                'app_opens':data['data']['aggregated']['appOpens']}
        total_data.append(extracted_data)
    return total_data

"""
========================================================================================
Agg
========================================================================================
"""
""""
Map

main_path="G:\phonepe project\pulse\data\map\transaction\hover\country\india"

"""
#map trans years


def map_trans_years(data,file_path):
    pattern = r'\\(\d{4})\\(\d+)\.json'


    match = re.search(pattern, file_path)
    if match:
        year = match.group(1)
        quarter = match.group(2)
        # Format the quarter as Q1, Q2, etc.
        formatted_quarter = f'Q{quarter}'
        
        if data['data']['hoverDataList']:
            length=len(data['data']['hoverDataList'])
            total_data=[]
            for i in range(length):   
                extracted_data={'year':year,"Quater":formatted_quarter,
                    "name":data['data']['hoverDataList'][i]['name'],
                    'type':data['data']['hoverDataList'][i]['metric'][0]['type'],
                    'count':data['data']['hoverDataList'][i]['metric'][0]['count'],
                    'amount':data['data']['hoverDataList'][i]['metric'][0]['amount']}
                total_data.append(extracted_data)
        else:
            extracted_data={'year':year,"Quater":formatted_quarter,
                            "name":data['data']['hoverDataList'][i]['name']}
            total_data.append(extracted_data)
    return total_data
#map -> trans states
def map_trans_states(data,file_path):
    pattern = r'\\state\\([a-zA-Z&\-]+)\\(\d{4})\\(\d+)\.json'

    # Use re.search to find the matches
    match = re.search(pattern, file_path)

    if match:
        state = match.group(1)
        year = match.group(2)
        quarter = match.group(3)
        formatted_quarter = f'Q{quarter}'

    all_data=[]

    if data['data']['hoverDataList']:
        districts=len(data['data']['hoverDataList'])
        for district in range(districts):
            extracted_data={"state":state,"year":year,"quater":formatted_quarter,
                            "district":data['data']['hoverDataList'][district]['name'],
                            "count":data['data']['hoverDataList'][district]['metric'][0]['count'],
                            "amount":data['data']['hoverDataList'][district]['metric'][0]['amount']}
            all_data.append(extracted_data)
    else:
        extracted_data={"state":state,'year':year,"Quater":formatted_quarter,"district":district,}
        all_data.append(extracted_data)
    return all_data



#map-> users-> years
def map_user_years(data,file_path):
    pattern = r'\\(\d{4})\\(\d+)\.json'


    match = re.search(pattern, file_path)
    if match:
        year = match.group(1)
        quarter = match.group(2)
        # Format the quarter as Q1, Q2, etc.
        formatted_quarter = f'Q{quarter}'
        
        total_data=[]
        if data['data']['hoverData']:
            states=data['data']['hoverData'].keys()
            for state in states:   
                extracted_data={'year':year,"Quater":formatted_quarter,
                    "state":state,
                    'count':data['data']['hoverData'][state]['registeredUsers'],
                    'amount':data['data']['hoverData'][state]['appOpens']}
                total_data.append(extracted_data)
        
    return total_data
#map->users-> states
def map_user_states(data,file_path):
    pattern = r'\\state\\([a-zA-Z&\-]+)\\(\d{4})\\(\d+)\.json'

    # Use re.search to find the matches
    match = re.search(pattern, file_path)

    if match:
        state = match.group(1)
        year = match.group(2)
        quarter = match.group(3)
        formatted_quarter = f'Q{quarter}'
    total_data=[]
    if data['data']['hoverData']:    
            districts=data['data']['hoverData'].keys()
            for district in districts: 
                extracted_data={"state":state,"year":year,"quater":formatted_quarter,
                "district":district,
                "users":data['data']['hoverData'][district]['registeredUsers'],
                "appOpens":data['data']['hoverData'][district]['appOpens']}
                total_data.append(extracted_data)
    else:
        extracted_data={"state":state,'year':year,"Quater":formatted_quarter,"district":district,}
        total_data.append(extracted_data)
    return total_data





""""
=========================================================================================================
                                               Top
=========================================================================================================
"""
"""
main_path=r"G:\phonepe project\pulse\data\top\transaction\country\india"
"""
# top trans years
def top_trans_years(data,file_path):

    pattern = r'\\(\d{4})\\(\d+)\.json'

    # Use re.search to find the matches
    match = re.search(pattern, file_path)

    year = match.group(1)
    quarter = match.group(2)
    formatted_quarter = f'Q{quarter}'    
    states=len(data['data']['states'])
    all_data=[]
    for state in range(states):
        extracted_data={"year":year,"quater":formatted_quarter,
            "state":data['data']['states'][state]['entityName'],
                        "type":data['data']['states'][state]['metric']['type'],
                        "count":data['data']['states'][state]['metric']['count'],
                        "amount":data['data']['states'][state]['metric']['amount']}
        all_data.append(extracted_data)
    return all_data    

# top trans states


def top_trans_states_pincodes(data,file_path):
    pattern = r'\\state\\([a-zA-Z&\-]+)\\(\d{4})\\(\d+)\.json'

    # Use re.search to find the matches
    match = re.search(pattern, file_path)

    if match:
        state = match.group(1)
        year = match.group(2)
        quarter = match.group(3)
        formatted_quarter = f'Q{quarter}'
    pincodes=len(data['data']['pincodes'])
    all_data_pincodes=[]             
    for pincode in range(pincodes):
        extracted_data_pincodes={'pincodes':data['data']['pincodes'][pincode]['entityName'],
                    'count':data['data']['pincodes'][pincode]['metric']['count'],
                    'amount':data['data']['pincodes'][pincode]['metric']['amount']}
        all_data_pincodes.append(extracted_data_pincodes)
    return all_data_pincodes


def top_trans_states_districts(data,file_path):
    pattern = r'\\state\\([a-zA-Z&\-]+)\\(\d{4})\\(\d+)\.json'

    # Use re.search to find the matches
    match = re.search(pattern, file_path)

    if match:
        state = match.group(1)
        year = match.group(2)
        quarter = match.group(3)
        formatted_quarter = f'Q{quarter}'
    districts=len(data['data']['districts'])
    all_data=[]
    for district in range(districts):
        extracted_data={"state":state,"year":year,"quater":formatted_quarter,"district":data['data']['districts'][district]['entityName'],
                        "count":data['data']['districts'][district]['metric']['count'],
                        "amount":data['data']['districts'][district]['metric']['amount']}
        all_data.append(extracted_data)
        return all_data

# user trans years -states, districts, pincodes


def top_user_year_pincode(data,file_path):
    pattern = r'\\(\d{4})\\(\d+)\.json'


    match = re.search(pattern, file_path)
    if match:
        year = match.group(1)
        quarter = match.group(2)
        # Format the quarter as Q1, Q2, etc.
        formatted_quarter = f'Q{quarter}'
    
    all_data=[]
    pincodes=len(data['data']['pincodes'])
    for pincode in range(pincodes):
            extracted_data={'year':year,"Quater":formatted_quarter,"pincode":data['data']['pincodes'][pincode]['name'],
                    "registred_user":data['data']['pincodes'][pincode]['registeredUsers']}
            all_data.append(extracted_data)
    return all_data

def top_user_year_district(data,file_path):
    pattern = r'\\(\d{4})\\(\d+)\.json'


    match = re.search(pattern, file_path)
    if match:
        year = match.group(1)
        quarter = match.group(2)
        # Format the quarter as Q1, Q2, etc.
        formatted_quarter = f'Q{quarter}'
    all_data=[]
    districts=len(data['data']['districts'])
    for district in range(districts):
        extracted_data={'year':year,"Quater":formatted_quarter,"district":data['data']['districts'][district]['name'],
                        "registred_users":data['data']['districts'][district]['registeredUsers']}
        all_data.append(extracted_data)
    return all_data

def top_user_year_state(data,file_path):
    pattern = r'\\(\d{4})\\(\d+)\.json'


    match = re.search(pattern, file_path)
    if match:
        year = match.group(1)
        quarter = match.group(2)
        # Format the quarter as Q1, Q2, etc.
        formatted_quarter = f'Q{quarter}'

    all_data=[]
    states=len(data['data']['states'])
    for state in range(states):

        extracted_data={'year':year,"Quater":formatted_quarter,'state':data['data']['states'][state]['name'],
                        'registered_users':data['data']['states'][state]['registeredUsers']}
        all_data.append(extracted_data)

    return all_data

# top users states district, pincode


def top_user_states_pincode(data,file_path):
    pattern = r'\\state\\([a-zA-Z&\-]+)\\(\d{4})\\(\d+)\.json'

    # Use re.search to find the matches
    match = re.search(pattern, file_path)

    if match:
        state = match.group(1)
        year = match.group(2)
        quarter = match.group(3)
        formatted_quarter = f'Q{quarter}'
    districts=len(data['data']['districts'])
    all_data=[]
    for district in range(districts):
        extracted_data={"state":state,"year":year,"quater":formatted_quarter,
                        "registered_users":data['data']['districts'][district]['registeredUsers']}
        all_data.append(extracted_data)
        return all_data 
    
    
def top_user_states_districts(data,file_path):
    pattern = r'\\state\\([a-zA-Z&\-]+)\\(\d{4})\\(\d+)\.json'

    # Use re.search to find the matches
    match = re.search(pattern, file_path)

    if match:
        state = match.group(1)
        year = match.group(2)
        quarter = match.group(3)
        formatted_quarter = f'Q{quarter}'
    districts=len(data['data']['districts'])
    all_data=[]
    for district in range(districts):
        extracted_data={"state":state,"year":year,"quater":formatted_quarter,"name":data['data']['districts'][district]['name'],
                    "registered_users":data['data']['districts'][district]['registeredUsers']}
        all_data.append(extracted_data)
        return all_data