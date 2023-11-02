import streamlit as st
from PIL import Image
import mysql.connector
from interface import *
from viz import *
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

    st.set_page_config(page_title='PhonePe Pulse', page_icon='https://www.phonepe.com/pulse/',layout="wide")
    with st.container():
             image = Image.open('PhonePe_Logo.jpg')
             st.image(image)
             st.divider()
             with st.container():
                    
                    tab1,tab2,tab3,tab4=st.tabs(["Home",'EXPLORE DATA',"Map"," VIZ - INSIGHTS "])
                    with tab1:
                            #Home
                            with st.container():
                                    st.header("Home")
                                    with st.container():
                                          st.header(':violet[Digital Payements in India: A US$10 Tn opportunity]')
                                          st.write('Check out the new phonepe pulse - BCG report on what \
                                                   future holds for digital payments in india')
                                    with st.container():
                                          col_,col__=st.columns(2)
                                          with col_:
                                                 st.video(r'https://www.youtube.com/watch?v=c_1H6vivsiA',format="video/mp4",start_time=0)
                                          with col__:
                                                col,col1=st.columns(2)
                                                with col:       
                                                        image_path=r"pics\Screenshot-2023-10-13-140422.jpeg"
                                                        img=Image.open(image_path)
                                                        st.image(img, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
                                                        with st.container():
                                                          st.write(' ')
                                                          st.header('This project is inspired from Phonepe pulse')
                                                with col1:
                                                      image_path=r"pics\Screenshot 2023-10-13 133528.png"
                                                      img=Image.open(image_path)
                                                      st.image(img)
                                                      with st.container():
                                                          st.write('Extracted the data, transformd and loaded in to the DataWarehouse')
                                                          st.write('The project developed in mind of the fields,that are able to update dynamically. ')
                                                      






                    with tab2:
                            with st.container():        
                                    st.header("EXPLORE DATA")
                                    col1,col2,col3=st.columns(3)
                                    with col1:
                                        options=["transaction", "user"]
                                        selected1=st.selectbox("Choose to view",options,index=None,placeholder="Deafult: transaction")
                                        year=[2018,2019,2020,2021,2022,2023]
                                        selected2=st.selectbox("choose the year",year,index=None,placeholder="Default: 2023")
                                        quaters=["Q1","Q2","Q3","Q4"]
                                        selected3=st.selectbox("Choose the quater",quaters,index=None,placeholder="Defalut: Q2" )

                                        reseted=st.button("Reset",type="primary")
                                        st.write('If reseted, then year -2023 and Quater - Q2')
                                        if reseted:
                                              selected1='transaction'
                                              selected2=2023
                                              selected3="Q3"

                                    with col2:
                                           st.title("Map")
                                           with st.container():
                                                 map_fig=get_map(selected1,selected2,selected3)
                                                 st.plotly_chart(map_fig, use_container_width=True,theme='streamlit')
                                    with col3:
                                           with st.container():
                                                  #dynamic index = india, when hovered it show all the details of the state.
                                                  result=get_transactions(selected1,selected2,selected3)
                                                  if selected1==None or selected1=="transaction":
                                                         total_trans=result[0]
                                                         total_amount=result[1]
                                                         average_amount_per_trans=result[2]
                                                         st.header(f"Transactions")
                                                         st.write("All PhonePe transactions (UPI + Cards + Wallets)")
                                                         st.subheader(f':blue[{total_trans}]')
                                                         st.write(f"Total Payment Value ")
                                                         st.subheader(f':blue[{total_amount}]')
                                                         st.write("Avg.transaction value")
                                                         st.subheader(f':blue[{average_amount_per_trans}]')
                                                  else:
                                                         registered_users=result[0]
                                                         app_opens=result[1]
                                                         st.header("users")
                                                         st.write(f"Registered PhonePe users ")
                                                         st.write(f':blue[{registered_users}]')
                                                         st.write(f'Phonepe App Opens ')
                                                         st.write(f':blue[{app_opens}]')
       
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
                                                              result1=get_top10_states(selected1,selected2,selected3)
                                                              result1=pd.DataFrame(result1)
                                                              st.write(result1)
                                                        
                                                        with tab10:
                                                               st.header("Top 10 Districts")
                                                               result2=get_top10_states(selected1,selected2,selected3)
                                                               result2=pd.DataFrame(result2)
                                                               st.write(result2)

                                                        with tab11:
                                                               result3=get_top_10_pincodes(selected1,selected2,selected3)
                                                               st.header("Postal Codes.")  
                                                               st.write(result3)
                                                               
                                                  else: 
                                                        tab9,tab10,tab11=st.tabs(["States","Districts","Postal Codes"])
                                                        with tab9:
                                                              st.header("Top 10 States")
                                                              result4=get_top_10_user_states(selected1,selected2,selected3)
                                                              result4=pd.DataFrame(result4)
                                                              result4.reset_index(drop=True,inplace=True)
                                                              st.write(result4)

                                                        
                                                        with tab10:
                                                               #dynamic
                                                               st.header("Top 10 Districts")
                                                               result5=get_top_10_user_district(selected1,selected2,selected3)
                                                               result5=pd.DataFrame(result5)
                                                               result5.reset_index(drop=True,inplace=True)
                                                               st.write(result5)
                                                        with tab11:
                                                        # dynamic
                                                         st.header("Top 10 Postal Codes")  
                                                         result6=get_top_10_user_pincode(selected1,selected2,selected3)
                                                         result6=pd.DataFrame(result6)
                                                         result6.reset_index(drop=True,inplace=True)
                                                         st.write(result6)



                    with tab3:    
                                st.header("Map")
                                st.plotly_chart(map_fig,theme='streamlit',use_container_width=True)
                    with tab4:
                            with st.container():
                                st.header("Visual INSIGHTS")
                                tab1,tab2=st.tabs(['Overall-Data Viz ',"Speicific Data - Viz"])
                                with tab1:
                                      st.header("Overall-Data visualisation")
                                      result=get_overall()
                                      with st.container():
                                            col1,col2=st.columns(2)
                                            with col1:
                                              st.plotly_chart(result[0],theme='streamlit',use_container_width=True)
                                            with col2:
                                                  st.plotly_chart(result[1],theme='streamlit',use_container_width=True)
                                      with st.container():
                                              col1, col2=st.columns(2)
                                              with col1:
                                                    st.plotly_chart(result[2],theme='streamlit',use_container_width=True)
                                              with col2:
                                                    st.plotly_chart(result[3],theme='streamlit',use_container_width=True)

                                with tab2:
                                      st.header("Specific - Data visualisation")

                            #with st.container():
                                  



if __name__=='__main__':
    run()

