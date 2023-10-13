import pandas as pd
import mysql.connector



connection_string="phonepeproject.cwoakibr9oeh.ap-south-1.rds.amazonaws.com"
user_name="Thinesh"
password="Thinesh1234"

connection_object = mysql.connector.connect(
host=connection_string,
user=user_name,
password=password)

cursor_object=connection_object.cursor()
cursor_object.execute("use phonepe")

def get_transactions(selected1,selected2,selected3):
    if selected1 is None and selected2 is None and selected3 is None:
        #display 2023, Q2
        query='select * from agg_trans_years'
        selected2=2023
        selected3='Q2'
        df=pd.read_sql(query,connection_object)
        filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
        total_tranaction=filtered_df['count'].sum()
        total_amount=filtered_df['amount'].sum()
        average_amount_per_trans=total_amount/total_tranaction
        cat_trans_amount=filtered_df.iloc[:,[2,4,5]]
        cc=cat_trans_amount.copy()
        cc.reset_index(drop=True, inplace=True)
        return total_tranaction,total_amount,average_amount_per_trans,cc
    
    elif selected1=='transaction':
         if selected2 is None and selected3 is None:
            #display 2023, Q2
                query='select * from agg_trans_years'
                df=pd.read_sql(query,connection_object)
                selected2=2023
                selected3="Q2"
                filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
                total_tranaction=filtered_df['count'].sum()
                total_amount=filtered_df['amount'].sum()
                average_amount_per_trans=total_amount/total_tranaction
                cat_trans_amount=filtered_df.iloc[:,[2,4,5]]
                cc=cat_trans_amount.copy()
                cc.reset_index(drop=True, inplace=True)
                return total_tranaction,total_amount,average_amount_per_trans,cc
         


         elif selected2==None and selected3 !=None:
             
            query='select * from agg_trans_years'
            df=pd.read_sql(query,connection_object)
            selected2=2023
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
            total_tranaction=filtered_df['count'].sum()
            total_amount=filtered_df['amount'].sum()
            average_amount_per_trans=total_amount/total_tranaction
            cat_trans_amount=filtered_df.iloc[:,[2,4,5]]
            cc=cat_trans_amount.copy()
            cc.reset_index(drop=True, inplace=True)
            return total_tranaction,total_amount,average_amount_per_trans,cc
        
         elif selected2!=None and selected3 !=None:
             
            query='select * from agg_trans_years'
            df=pd.read_sql(query,connection_object)
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
            total_tranaction=filtered_df['count'].sum()
            total_amount=filtered_df['amount'].sum()
            average_amount_per_trans=total_amount/total_tranaction
            cat_trans_amount=filtered_df.iloc[:,[2,4,5]]
            cc=cat_trans_amount.copy()
            cc.reset_index(drop=True, inplace=True)
            return total_tranaction,total_amount,average_amount_per_trans,cc
       
         elif  selected2!=None and selected3==None :
             
            query='select * from agg_trans_years'
            df=pd.read_sql(query,connection_object)
            filtered_df=df[(df['year']==selected2)&(df['Quater']=='Q4')]
            total_tranaction=filtered_df['count'].sum()
            total_amount=filtered_df['amount'].sum()
            average_amount_per_trans=total_amount/total_tranaction
            cat_trans_amount=filtered_df.iloc[:,[2,4,5]]
            cc=cat_trans_amount.copy()
            cc.reset_index(drop=True, inplace=True)
            return total_tranaction,total_amount,average_amount_per_trans,cc
        
         elif selected2!=None:
                    query='select * from agg_trans_years'
                    df=pd.read_sql(query,connection_object)
                    selected3='Q4'
                    filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
                    total_tranaction=filtered_df['count'].sum()
                    total_amount=filtered_df['amount'].sum()
                    average_amount_per_trans=total_amount/total_tranaction
                    cat_trans_amount=filtered_df.iloc[:,[2,4,5]]
                    cc=cat_trans_amount.copy()
                    cc.reset_index(drop=True, inplace=True)
                    return total_tranaction,total_amount,average_amount_per_trans,cc
         elif selected3!=None:
                    query='select * from agg_trans_years'
                    df=pd.read_sql(query,connection_object)
                    selected2=2023
                    filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
                    total_tranaction=filtered_df['count'].sum()
                    total_amount=filtered_df['amount'].sum()
                    average_amount_per_trans=total_amount/total_tranaction
                    cat_trans_amount=filtered_df.iloc[:,[2,4,5]]
                    cc=cat_trans_amount.copy()
                    cc.reset_index(drop=True, inplace=True)
                    return total_tranaction,total_amount,average_amount_per_trans,cc
    else:
         if selected2==None and selected3==None:
            query='select * from agg_user_years'
            df=pd.read_sql(query,connection_object)
            selected2=2023
            selected3="Q2"
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
            total_user=(filtered_df['users'].unique())
            total_app_opens=(filtered_df['app_opens'].unique())
            return total_user,total_app_opens
         elif selected2==None and selected3!=None:
            query='select * from agg_user_years'
            df=pd.read_sql(query,connection_object)
            selected2=2023
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
            total_user=(filtered_df['users'].unique())
            total_app_opens=(filtered_df['app_opens'].unique())
            return total_user,total_app_opens
            
         elif selected2 != None and selected3 != None:
            query='select * from agg_user_years'
            df=pd.read_sql(query,connection_object)
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
            total_user=(filtered_df['users'].unique())
            total_app_opens=(filtered_df['app_opens'].unique())
            return total_user,total_app_opens
         elif selected2 !=None and selected3==None:
            query='select * from agg_user_years'
            df=pd.read_sql(query,connection_object)
            selected3="Q4"
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
            total_user=(filtered_df['users'].unique())
            total_app_opens=(filtered_df['app_opens'].unique())
            return total_user,total_app_opens
         elif selected2!= None and selected3 !=None:
            query='select * from agg_user_years'
            df=pd.read_sql(query,connection_object)
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
            total_user=(filtered_df['users'].unique())
            total_app_opens=(filtered_df['app_opens'].unique())
            return total_user,total_app_opens
         elif selected2!=None:
              query='select * from agg_user_years'
              df=pd.read_sql(query,connection_object)
              selected3='Q4'
              filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
              total_user=(filtered_df['users'].unique())
              total_app_opens=(filtered_df['app_opens'].unique())
              return total_user,total_app_opens
         elif selected3!=None:
              query='select * from agg_user_years'
              df=pd.read_sql(query,connection_object)
              selected2=2023
              filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
              total_user=(filtered_df['users'].unique())
              total_app_opens=(filtered_df['app_opens'].unique())
              return total_user,total_app_opens
              
            

def get_top10_states(selected1,selected2,selected3):
    
     if all(var is None for var in (selected1, selected2, selected3)):
            query='select * from agg_trans_years_states'
            df=pd.read_sql(query,connection_object)
            filtered_df=df[(df['year']==2023)&(df['Quater']=='Q2')]       
            state_total_trans=filtered_df.groupby(['state'])['count'].agg(sum)
            top_10_states=state_total_trans.nlargest(10)
            return top_10_states
                    
     elif selected1=='transaction':
        if selected2==None and selected3==None: 
            query='select * from agg_trans_years_states'
            df=pd.read_sql(query,connection_object)
            filtered_df=df[(df['year']==2023)&(df['Quater']=='Q2')]
            state_total_trans=filtered_df.groupby(['state'])['count'].agg(sum)
            top_10_states=state_total_trans.nlargest(10)
            return top_10_states
        elif selected2==None and selected3 !=None:
            query='select * from agg_trans_years_states'
            df=pd.read_sql(query,connection_object)
            filtered_df=df[(df['year']==2023)&(df['Quater']==selected3)]
            state_total_trans=filtered_df.groupby(['state'])['count'].agg(sum)
            top_10_states=state_total_trans.nlargest(10)
            return top_10_states
        elif selected2!=None and selected3 !=None:
             
            query='select * from agg_trans_years_states'
            df=pd.read_sql(query,connection_object)
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
            state_total_trans=filtered_df.groupby(['state'])['count'].agg(sum)
            top_10_states=state_total_trans.nlargest(10)
            return top_10_states
        elif  selected2!=None and selected3==None :
             
            query='select * from agg_trans_years_states'
            df=pd.read_sql(query,connection_object)
            filtered_df=df[(df['year']==selected2)&(df['Quater']=='Q4')]
            state_total_trans=filtered_df.groupby(['state'])['count'].agg(sum)
            top_10_states=state_total_trans.nlargest(10)
            return top_10_states
        
     elif selected2!=None:
            query='select * from agg_trans_years_states'
            df=pd.read_sql(query,connection_object)
            filtered_df=df[(df['year']==selected2)&(df['Quater']=='Q4')]
            state_total_trans=filtered_df.groupby(['state'])['count'].agg(sum)
            top_10_states=state_total_trans.nlargest(10)
            return top_10_states
          
     elif selected3!=None:
            query='select * from agg_trans_years_states'
            df=pd.read_sql(query,connection_object)
            filtered_df=df[(df['year']==2023)&(df['Quater']==selected3)]
            state_total_trans=filtered_df.groupby(['state'])['count'].agg(sum)
            top_10_states=state_total_trans.nlargest(10)
            return top_10_states

     else:
         if selected2==None and selected3==None:
            query='select * from agg_user_states'
            df=pd.read_sql(query,connection_object)
            filtered_df=df[(df['year']==2023)&(df['Quater']=='Q2')]
            state_total_user=filtered_df.groupby(['state'])['count'].agg(sum)
            top_10_state_user=state_total_user.nlargest(10)
            return top_10_state_user
         elif selected2==None and selected3!=None:
            query='select * from agg_user_states'
            df=pd.read_sql(query,connection_object)
            filtered_df=df[(df['year']==2023)&(df['Quater']==selected3)]
            state_total_user=filtered_df.groupby(['state'])['count'].agg(sum)
            top_10_state_user=state_total_user.nlargest(10)
            return top_10_state_user
         elif selected2 != None and selected3 != None:
            query='select * from agg_user_states'
            df=pd.read_sql(query,connection_object)
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected2)]
            state_total_user=filtered_df.groupby(['state'])['count'].agg(sum)
            top_10_state_user=state_total_user.nlargest(10)
            return top_10_state_user
         elif selected2 !=None and selected3==None:
            query='select * from agg_user_years'
            df=pd.read_sql(query,connection_object)
            filtered_df=df[(df['year']==selected2)&(df['Quater']=="Q4")]
            state_total_user=filtered_df.groupby(['state'])['count'].agg(sum)
            top_10_state_user=state_total_user.nlargest(10)
            return top_10_state_user
    
def get_top10_districts(selected1,selected2,selected3):
     
            if all(var is None for var in (selected1, selected2, selected3)):
                query='select * from top_trans_states_districts'
                df=pd.read_sql(query,connection_object)
                filtered_df=df[(df['year']==2023)&(df['Quater']=='Q2')]       
                top_10_districts=filtered_df.groupby('district')['count'].agg(sum).nlargest(10)
                return top_10_districts
                        
            elif selected1=='transaction':
                if selected2==None and selected3==None: 
                    query='select * from top_trans_states_districts'
                    df=pd.read_sql(query,connection_object)
                    filtered_df=df[(df['year']==2023)&(df['Quater']=='Q2')]
                    top_10_districts=filtered_df.groupby('district')['count'].agg(sum).nlargest(10)
                    return top_10_districts
                elif selected2==None and selected3 !=None:
                    query='select * from top_trans_states_districts'
                    df=pd.read_sql(query,connection_object)
                    filtered_df=df[(df['year']==2023)&(df['Quater']==selected3)]
                    top_10_districts=filtered_df.groupby('district')['count'].agg(sum).nlargest(10)
                    return top_10_districts
                elif selected2!=None and selected3 !=None:
             
                    query='select * from top_trans_states_districts'
                    df=pd.read_sql(query,connection_object)
                    filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
                    top_10_districts=filtered_df.groupby('district')['count'].agg(sum).nlargest(10)
                    return top_10_districts
                elif  selected2!=None and selected3==None :
             
                        query='select * from top_trans_states_districts'
                        df=pd.read_sql(query,connection_object)
                        filtered_df=df[(df['year']==selected2)&(df['Quater']=='Q4')]
                        top_10_districts=filtered_df.groupby('district')['count'].agg(sum).nlargest(10)
                        return top_10_districts
                elif selected2!=None:
                        query='select * from top_trans_states_districts'
                        df=pd.read_sql(query,connection_object)
                        filtered_df=df[(df['year']==selected2)&(df['Quater']=='Q4')]
                        top_10_districts=filtered_df.groupby('district')['count'].agg(sum).nlargest(10)
                        return top_10_districts
                    
                elif selected3!=None:
                        query='select * from top_trans_states_districts'
                        df=pd.read_sql(query,connection_object)
                        filtered_df=df[(df['year']==2023)&(df['Quater']==selected3)]
                        top_10_districts=filtered_df.groupby('district')['count'].agg(sum).nlargest(10)
                        return top_10_districts

def get_top_10_pincodes(selected1,selected2,selected3):

    if all(var is None for var in (selected1, selected2, selected3)):
        selected1="transaction"
        selected2=2023,
        selected3='Q2'
        query=f"select * from top_trans_states_pincodes;"
        df=pd.read_sql(query,connection_object)
        filtered_df=df[(df['year']==selected2) & (df['Quater']==selected3)]
        top_10_trans_pincodes = filtered_df.nlargest(10, 'count')[['pincodes', 'count']]
        top_10_trans_pincodes.reset_index(drop=True, inplace=True)
        return top_10_trans_pincodes
                    
    elif selected1=='transaction':
        if selected2==None and selected3==None: 
                        selected2=2023
                        selected3='Q2'
                        query=f"select * from top_trans_states_pincodes;"
                        df=pd.read_sql(query,connection_object)
                        filtered_df=df[(df['year']==selected2) & (df['Quater']==selected3)]
                        top_10_trans_pincodes = filtered_df.nlargest(10, 'count')[['pincodes', 'count']]
                        top_10_trans_pincodes.reset_index(drop=True, inplace=True)
                        return top_10_trans_pincodes

        elif selected2==None and selected3 !=None:
                
                selected2=2023
                query=f"select * from top_trans_states_pincodes;"
                df=pd.read_sql(query,connection_object)
                top_10_trans_pincodes = filtered_df.nlargest(10, 'count')[['pincodes', 'count']]
                filtered_df=df[(df['year']==selected2) & (df['Quater']==selected3)]
                top_10_trans_pincodes.reset_index(drop=True, inplace=True)
                return top_10_trans_pincodes
        elif selected2!=None and selected3 !=None:
                #selected2 and selected3 are dynamic
                query=f"select * from top_trans_states_pincodes;"
                df=pd.read_sql(query,connection_object)
                filtered_df=df[(df['year']==selected2) & (df['Quater']==selected3)]
                top_10_trans_pincodes = filtered_df.nlargest(10, 'count')[['pincodes', 'count']]
                top_10_trans_pincodes.reset_index(drop=True, inplace=True)
                return top_10_trans_pincodes
        elif  selected2!=None and selected3==None :
                # selected3 is q4
                selected="Q4"
                query=f"select * from top_trans_states_pincodes;"
                df=pd.read_sql(query,connection_object)
                filtered_df=df[(df['year']==selected2) & (df['Quater']==selected3)]
                top_10_trans_pincodes = filtered_df.nlargest(10, 'count')[['pincodes', 'count']]
                top_10_trans_pincodes.reset_index(drop=True, inplace=True)
                return top_10_trans_pincodes
        elif selected2!=None:
                
                selected3="Q4"
                query=f"select * from top_trans_states_pincodes;"
                df=pd.read_sql(query,connection_object)
                filtered_df=df[(df['year']==selected2) & (df['Quater']==selected3)]
                top_10_trans_pincodes = filtered_df.nlargest(10, 'count')[['pincodes', 'count']]
                top_10_trans_pincodes.reset_index(drop=True, inplace=True)
                return top_10_trans_pincodes

        elif selected3!=None:
                # selected 2= 2023 and selected3 is dynamic
                selected2=2023
                query=f"select * from top_trans_states_pincodes;"
                df=pd.read_sql(query,connection_object)
                top_10_trans_pincodes = filtered_df.nlargest(10, 'count')[['pincodes', 'count']]
                top_10_trans_pincodes.reset_index(drop=True, inplace=True)
                return top_10_trans_pincodes
  #-----------------------------------------------------------------------------------------------#


def get_top_10_user_states (selected1,selected2,selected3):
         

        if selected2==None and selected3==None:
            query="select * from top_user_year_state"
            df=pd.read_sql(query,connection_object)
            selected2=2023
            selected3="Q2"
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]                        
            top_10_user_states=filtered_df.nlargest(10,'registered_users')[["state",'registered_users']]
            return top_10_user_states
        elif selected2==None and selected3!=None:
            query="select * from top_user_year_state"
            df=pd.read_sql(query,connection_object)
            selected2=2023
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
            
            top_10_user_states=filtered_df.nlargest(10,'registered_users')[["state",'registered_users']]
            return top_10_user_states
            
        elif selected2 != None and selected3 != None:
            query="select * from top_user_year_state"
            df=pd.read_sql(query,connection_object)
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]            
            top_10_user_states=filtered_df.nlargest(10,'registered_users')[["state",'registered_users']]
            return top_10_user_states
        elif selected2 !=None and selected3==None:
            query="select * from top_user_year_state"
            df=pd.read_sql(query,connection_object)
            selected3="Q4"
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]            
            top_10_user_states=filtered_df.nlargest(10,'registered_users')[["state",'registered_users']]
            return top_10_user_states
        elif selected1=='user' and selected2!= None and selected3 !=None:
            query="select * from top_user_year_state"
            df=pd.read_sql(query,connection_object)
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]            
            top_10_user_states=filtered_df.nlargest(10,'registered_users')[["state",'registered_users']]
            return top_10_user_states          


def get_top_10_user_district (selected1,selected2,selected3):
                    

        if selected2==None and selected3==None:
            query="select * from top_user_year_district"
            df=pd.read_sql(query,connection_object)
            selected2=2023
            selected3="Q2"
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
            top_10_user_district=filtered_df.nlargest(10,'registred_users')[["district",'registred_users']]     
            top_10_user_district.reset_index(drop=True,inplace=True)
            return top_10_user_district
        elif selected2==None and selected3!=None:
            query="select * from top_user_year_district"
            df=pd.read_sql(query,connection_object)
            selected2=2023
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
            top_10_user_district=filtered_df.nlargest(10,'registred_users')[["district",'registred_users']]
            top_10_user_district.reset_index(drop=True,inplace=True)
            return top_10_user_district
            
        elif selected2 != None and selected3 != None:
            query="select * from top_user_year_district"
            df=pd.read_sql(query,connection_object)
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)] 
            top_10_user_district=filtered_df.nlargest(10,'registred_users')[["district",'registred_users']]           
            top_10_user_district.reset_index(drop=True,inplace=True)
            return top_10_user_district
        elif selected2 !=None and selected3==None:
            query="select * from top_user_year_district"
            df=pd.read_sql(query,connection_object)
            selected3="Q4"
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]    
            top_10_user_district=filtered_df.nlargest(10,'registred_users')[["district",'registred_users']]
            top_10_user_district.reset_index(drop=True,inplace=True)
            return top_10_user_district
        elif selected1=='user' and selected2!= None and selected3 !=None:
            query="select * from top_user_year_district"
            df=pd.read_sql(query,connection_object)
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
            top_10_user_district=filtered_df.nlargest(10,'registred_users')[["district",'registred_users']]
            top_10_user_district.reset_index(drop=True,inplace=True)
            return top_10_user_district



def get_top_10_user_pincode(selected1,selected2,selected3):




    if selected2==None and selected3==None:
        query="select * from top_user_year_pincode"
        df=pd.read_sql(query,connection_object)
        selected2=2023
        selected3="Q2"
        filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
        top_10_user_pincode=filtered_df.nlargest(10,'registred_user')[["pincode",'registred_user']]     
        top_10_user_pincode.reset_index(drop=True,inplace=True)
        return top_10_user_pincode
    elif selected2==None and selected3!=None:
        query="select * from top_user_year_pincode"
        df=pd.read_sql(query,connection_object)
        selected2=2023
        filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
        top_10_user_pincode=filtered_df.nlargest(10,'registred_user')[["pincode",'registred_user']]     
        top_10_user_pincode.reset_index(drop=True,inplace=True)
        return top_10_user_pincode  
    elif selected2 != None and selected3 != None:
        query="select * from top_user_year_pincode"
        df=pd.read_sql(query,connection_object)
        filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)] 
        top_10_user_pincode=filtered_df.nlargest(10,'registred_user')[["pincode",'registred_user']]     
        top_10_user_pincode.reset_index(drop=True,inplace=True)
        return top_10_user_pincode
    elif selected2 !=None and selected3==None:
        query="select * from top_user_year_pincode"
        df=pd.read_sql(query,connection_object)
        selected3="Q4"
        filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]    
        top_10_user_pincode=filtered_df.nlargest(10,'registred_user')[["pincode",'registred_user']]     
        top_10_user_pincode.reset_index(drop=True,inplace=True)
        return top_10_user_pincode
    elif selected1=='user' and selected2!= None and selected3 !=None:
        query="select * from top_user_year_pincode"
        df=pd.read_sql(query,connection_object)
        filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
        top_10_user_pincode=filtered_df.nlargest(10,'registred_user')[["pincode",'registred_user']]     
        top_10_user_pincode.reset_index(drop=True,inplace=True)
        return top_10_user_pincode






                        
     