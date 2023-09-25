import os
import json
import datetime

"""
agg_main_path="G:\\phonepe project\\pulse\\data\\aggregated\\transaction\\country\\india"
os.chdir(main_path)
"""

# file navigation and extraction.
def aggregation_transaaction_years(main_path):
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
                    results=data_extraction(data)
                    for result in results:
                        transaction.append(result)
    df=pd.DataFrame(transaction)
    return df


def data_extraction(data):

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

#agg_data_extraxt_state
def data_extraction_agg_states(data,file_path):
    pattern = r'\\state\\([a-zA-Z&-]+)\\'

    # Use re.search to find the match
    match = re.search(pattern, file_path)

    #if match:
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


# agg_state   
def aggregation_transaaction_states(main_path):
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
                                                        results=data_extraction_agg_states(data,file_path)
                                                        for result in results:
                                                                transaction.append(result)
               else:continue
        df=pd.DataFrame(transaction)
        return df
  