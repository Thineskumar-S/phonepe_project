import streamlit as st
from PIL import Image


def run():

    connection_object = mysql.connector.connect(
    host=connection_string,
    user=user_name,
    password=password)

    cursor_object=connection_object.cursor()



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
                                        data1=["transaction", "user"]
                                        st.selectbox("Choose to view",data1)
                                        data2=["query"]
                                        st.selectbox("Choose the quater",data2)
                                    with col2:
                                           st.title("Map")
                                    with col3:
                                           with st.container():
                                                  #dynamic index = india, when hovered it show all the details of the state.
                                                  st.header("Transactions")
                                                  st.write("All PhonePe transactions (UPI + Cards + Wallets")
                                                  # dynamic hover
                                                  st.write("value for: Total payment value")
                                                  # dynamic hover 
                                                  st.write(" value for: Avg. transaction value ")
                                                  st.divider()
                                           with st.container():
                                                  # dynamic
                                                  st.header("Categories")
                                                  st.divider()
                                           with st.container():
                                                  tab9,tab10=st.tabs(["Districts","postal Codes"])
                                                  with tab9:
                                                         #dynamic
                                                         st.header("Top 10 Districts")
                                                  with tab10:
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

