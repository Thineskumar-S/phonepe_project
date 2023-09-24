import streamlit as st

def run():
    
    with st.container():
        st.title(":violet[Phonepe pulse]")  
    tab1,tab2,tab3,tab4=st.tabs(["Home",'Aggregation',"map","user"])
    with tab1:
        with st.container():
                st.header("Home")
    with tab2:
        with st.container():        
                st.header("Aggregation")
    with tab3:    
        with st.container():
            st.header("Map")
    with tab4:
         with st.container():
              st.header("User")

        






if __name__=='__main__':
    run()

