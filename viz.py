import plotly.express as px 
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




def get_map(selected1,selected2,selected3):
    if selected1 is None and selected2 is None and selected3 is None:
        #display 2023, Q2
        query='select * from map_trans_years'
        selected2=2023
        selected3='Q2'
        df=pd.read_sql(query,connection_object)
        df.name=df.name.apply(lambda x: x.title())
        filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]

        fig = px.choropleth(filtered_df,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                    featureidkey='properties.ST_NM',
                    locations='name',
                    color='count',hover_data=['year','Quater','amount'],
                    color_continuous_scale='sunset')

        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_layout(title_text=f'{selected2} {selected3} Transactions- State wise data (Hover for breakdown)')
        return fig
    
    elif selected1=='transaction':
         if selected2 is None and selected3 is None:
            #display 2023, Q2
                query='select * from map_trans_years'
                df=pd.read_sql(query,connection_object)
                selected2=2023
                selected3="Q2"
                df.name=df.name.apply(lambda x: x.title())
                filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]

                fig = px.choropleth(filtered_df,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='name',
                            color='count',hover_data=['year','Quater','amount'],
                            color_continuous_scale='sunset')

                fig.update_geos(fitbounds="locations", visible=False)
                fig.update_layout(title_text=f'{selected2} {selected3} Transactions - State wise data (Hover for breakdown)')
                return fig

         elif selected2==None and selected3 !=None:
             
            query='select * from map_trans_years'
            df=pd.read_sql(query,connection_object)
            selected2=2023
            df.name=df.name.apply(lambda x: x.title())
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]

            fig = px.choropleth(filtered_df,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='name',
                        color='count',hover_data=['year','Quater','amount'],
                        color_continuous_scale='sunset')

            fig.update_geos(fitbounds="locations", visible=False)
            fig.update_layout(title_text=f'{selected2} {selected3} Transactions- State wise data (Hover for breakdown)')
            return fig

        
         elif selected2!=None and selected3 !=None:
             
            query='select * from map_trans_years'
            df=pd.read_sql(query,connection_object)
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
            df.name=df.name.apply(lambda x: x.title())
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]

            fig = px.choropleth(filtered_df,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='name',
                        color='count',hover_data=['year','Quater','amount'],
                        color_continuous_scale='sunset')

            fig.update_geos(fitbounds="locations", visible=False)
            fig.update_layout(title_text=f'{selected2} {selected3}Transactions- State wise data (Hover for breakdown)')
            return fig
       
         elif  selected2!=None and selected3==None :
             
            query='select * from map_trans_years'
            df=pd.read_sql(query,connection_object)
            df.name=df.name.apply(lambda x: x.title())
            selected3='Q4'
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]

            fig = px.choropleth(filtered_df,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='name',
                        color='count',hover_data=['year','Quater','amount'],
                        color_continuous_scale='sunset')

            fig.update_geos(fitbounds="locations", visible=False)
            fig.update_layout(title_text=f'{selected2} {selected3}Transactions- State wise data (Hover for breakdown)')
            return fig

            
        
         elif selected2!=None:
                    query='select * from map_trans_years'
                    df=pd.read_sql(query,connection_object)
                    selected3='Q4'
                    df.name=df.name.apply(lambda x: x.title())
                    filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
                    fig = px.choropleth(filtered_df,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='name',
                        color='count',hover_data=['year','Quater','amount'],
                        color_continuous_scale='sunset')

                    fig.update_geos(fitbounds="locations", visible=False)
                    fig.update_layout(title_text=f'{selected2} {selected3}Transactions- State wise data (Hover for breakdown)')
                    return fig
                    
         elif selected3!=None:
                    query='select * from map_trans_years'
                    df=pd.read_sql(query,connection_object)
                    selected2=2023
                    df.name=df.name.apply(lambda x: x.title())
                    filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
                    fig = px.choropleth(filtered_df,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='name',
                        color='count',hover_data=['year','Quater','amount'],
                        color_continuous_scale='sunset')

                    fig.update_geos(fitbounds="locations", visible=False)
                    fig.update_layout(title_text=f'{selected2} {selected3} Transactions-State wise data (Hover for breakdown)')
                    return fig


    else:
         if selected2==None and selected3==None:
            query='select * from map_user_years'
            df=pd.read_sql(query,connection_object)
            selected2=2023
            selected3="Q2"
            df.state=df.state.apply(lambda x: x.title())
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
            fig = px.choropleth(filtered_df,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='state',
                        color='count',hover_data=['year','Quater','amount'],
                        color_continuous_scale='sunset')

            fig.update_geos(fitbounds="locations", visible=False)
            fig.update_layout(title_text=f'{selected2} {selected3} users - State wise data (Hover for breakdown)')
            return fig
         elif selected2==None and selected3!=None:
            query='select * from map_user_years'
            df=pd.read_sql(query,connection_object)
            selected2=2023
            df.state=df.state.apply(lambda x: x.title())
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]

            fig = px.choropleth(filtered_df,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='state',
                        color='count',hover_data=['year','Quater','amount'],
                        color_continuous_scale='sunset')

            fig.update_geos(fitbounds="locations", visible=False)
            fig.update_layout(title_text=f'{selected2} {selected3} users - State wise data (Hover for breakdown)')
            return fig
            
         elif selected2 != None and selected3 != None:
            query='select * from map_user_years'
            df=pd.read_sql(query,connection_object)
            df.state=df.state.apply(lambda x: x.title())
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected2)]
            df.state=df.state.apply(lambda x: x.title())
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]

            fig = px.choropleth(filtered_df,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='state',
                        color='count',hover_data=['year','Quater','amount'],
                        color_continuous_scale='sunset')

            fig.update_geos(fitbounds="locations", visible=False)
            fig.update_layout(title_text=f'{selected2} {selected3}users - State wise data (Hover for breakdown)')
            return fig
         elif selected2 !=None and selected3==None:
            query='select * from map_user_years'
            df=pd.read_sql(query,connection_object)
            selected3="Q4"
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]    
            df.state=df.state.apply(lambda x: x.title())
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]

            fig = px.choropleth(filtered_df,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='state',
                        color='count',hover_data=['year','Quater','amount'],
                        color_continuous_scale='sunset')

            fig.update_geos(fitbounds="locations", visible=False)
            fig.update_layout(title_text=f'{selected2} {selected3} users - State wise data (Hover for breakdown)')
            return fig
         elif selected1=='user' and selected2!= None and selected3 !=None:
            query='select * from map_user_years'
            df=pd.read_sql(query,connection_object)
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]
            df.state=df.state.apply(lambda x: x.title())
            filtered_df=df[(df['year']==selected2)&(df['Quater']==selected3)]

            fig = px.choropleth(filtered_df,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='state',
                        color='count',hover_data=['year','Quater','amount'],
                        color_continuous_scale='sunset')

            fig.update_geos(fitbounds="locations", visible=False)
            fig.update_layout(title_text=f'{selected2} {selected3}users -  State wise data (Hover for breakdown)')  
            return fig            
"""
End of map_display
"""

"""
Viz - Insights
"""
def get_overall():
      query='Select * from agg_trans_years'
      df=pd.read_sql(query,connection_object)
      df2=df.groupby(['year','Quater'])[['amount','count']].agg(sum)
      x_values = df2.index.get_level_values(0)
      quater=df2.index.get_level_values(1)
      fig=px.bar(x=x_values,y=df2['amount'],color=quater,title="overall Tranascation amount")
      fig.update_layout(
         xaxis_title="Year",
         yaxis_title="Amount"
      )
      fig1=px.bar(x=x_values,y=df2['count'],color=quater,title='Overall Transaction count')
      fig1.update_layout(
         xaxis_title="Year",
         yaxis_title="Count"
      )
      
      query2='Select * from agg_user_years'
      df3=pd.read_sql(query2,connection_object)
      df4=df3.groupby(['year','Quater'])[['count','percentage']].agg(sum)
      x_values = df4.index.get_level_values(0)
      quater=df4.index.get_level_values(1)
      fig2=px.bar(x=x_values,y=df4['count'],color=quater,title='Overall user count')
      fig2.update_layout(
         xaxis_title="Year",
         yaxis_title="Count"
      )
      df5=df3.groupby('brand')[['count','percentage']].agg(sum)
      x_values = df5.index.get_level_values(0)
      fig3=px.bar(x=x_values,y=df5['count'],title='Overall device users  count')
      fig3.update_layout(
         xaxis_title="brand",
         yaxis_title="Count"
      )


      return fig,fig1,fig2,fig3