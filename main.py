import streamlit as st
from PIL import Image
import mysql.connector
from interface import *
def run():
    
    
    connection_string="phonepeproject.cwoakibr9oeh.ap-south-1.rds.amazonaws.com"
    user_name="Thinesh"
    password="Thinesh1234"

    connection_object = mysql.connector.connect(
    host=connection_string,
    user=user_name,
    password=password)

    cursor_object=connection_object.cursor()
    cursor_object.execute("use phonepe")



    with st.container():
             image = Image.open('PhonePe_Logo.jpg')
             st.image(image)
             st.divider()
             with st.container():
                    
                    tab1,tab2,tab3,tab4=st.tabs(["Home",'Aggregation',"Map","User"])
                    with tab1:
                            #Home
                            with st.container():
                                    st.header("Home")
                    with tab2:
                            with st.container():        
                                    st.header("Aggregation")
                                    col1,col2,col3=st.columns(3)
                                    with col1:
                                        options=["transaction", "user"]
                                        selected1=st.selectbox("Choose to view",options,placeholder="transaction")
                                        year=[2018,2019,2020,2021,2022,2023]
                                        selected2=st.selectbox("choose the year",year,index=None,placeholder="default: 2023")
                                        quaters=["Q1","Q2","Q3","Q4"]
                                        selected3=st.selectbox("Choose the quater",quaters,index=None,placeholder="defalut: Q2" )

                                        reseted=st.button("Reset",type="primary")
                                        if reseted:
                                              selected1='transaction'
                                              selected2=2023
                                              selected3="Q3"

                                    with col2:
                                           st.title("Map")
                                    with col3:
                                           with st.container():
                                                  #dynamic index = india, when hovered it show all the details of the state.
                                                  result=get_transactions(selected1,selected2,selected3)
                                                  if selected1==None or selected1=="transaction":
                                                         total_trans=result[0]
                                                         total_amount=result[1]
                                                         average_amount_per_trans=result[2]
                                                         st.header("Transactions")
                                                         st.write("All PhonePe transactions (UPI + Cards + Wallets)")
                                                         st.write(total_trans)
                                                         st.write("Total Payment Value")
                                                         st.write(total_amount)
                                                         st.write("Avg.transaction value")
                                                         st.write(average_amount_per_trans)
                                                         

                                                  else:
                                                         registered_users=result[0]
                                                         app_opens=result[1]
                                                         st.header("users")
                                                         st.write("Registered PhonePe users")
                                                         st.write(registered_users)
                                                         st.write(app_opens)
       
                                                  st.divider()
                                           with st.container():
                                                  # dynamic
                                                  if selected1==None or selected1=="transaction":
                                                        st.header("Categories")
                                                        df=result[3]
                                                        st.write(df)
                                                        st.divider()
                                           with st.container():
                                                  if selected1==None or selected1=="transaction":
                                                        tab9,tab10,tab11=st.tabs(["States","Districts","Postal Codes"])
                                                        with tab9:
                                                              st.header("Top 10 states")
                                                        
                                                        with tab10:
                                                        
                                                               #dynamic
                                                               st.header("Top 10 Districts")
                                                        with tab11:
                                                        # dynamic
                                                         st.header("Postal Codes")  
                                                  else: 
                                                        tab9,tab10,tab11=st.tabs(["States","Districts","Postal Codes"])
                                                        with tab9:
                                                              st.header("Top 10 States")
                                                        
                                                        with tab10:
                                                               #dynamic
                                                               st.header("Top 10 Districts")
                                                        with tab11:
                                                        # dynamic
                                                         st.header("Postal Codes")  









                    with tab3:    
                            with st.container():
                                st.header("Map")
                    with tab4:
                            with st.container():
                                st.header("User")

            






if __name__=='__main__':
    run()

