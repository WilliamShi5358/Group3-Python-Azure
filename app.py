import streamlit as st #pip install streamlit
import pandas as pd    #pip install pandas
import numpy as np     #pip install numpy

import streamlit_app as default_filter
import dynamic_filter as dynamic_filter

# show app header,title
st.subheader('INFO 4330 Group 3 Python Streamlit App Deploying by Azure web service')
st.write("Multi Columns Streamlit filter ")

#define global variable df 
global loaded_df
#Creating a method to upload the csv file, return df as pd dataframe
def uploader_csv():
    #set sidebar sub header for file uploader
    st.sidebar.subheader('Single CSV File Upload')
    #deploy streamlit file_uploader method 
    upload_file= st.sidebar.file_uploader(label='Choose csv file to upload',type=['csv'])
    # deploy pandas library to read csv file
    if upload_file is not None:
        try:
            loaded_df= pd.read_csv(upload_file)
            st.sidebar.success("Loaded CSV dataset!")
        except Exception:
            print("please choose the csv file to upload...")
    return loaded_df
    
try:
    #user uploads csv file
    loaded_df = uploader_csv()
except Exception:
    #if user doesn't uploads csv file, app can show the YouTube statistic dataset by default
    default_filter.filter()
    print('please choose the csv file to upload for web app')

#call datafram filter method 
try: 
   st.dataframe(dynamic_filter.dynamicFilter(loaded_df))
except Exception as e:
   print('please choose the csv file to upload for web app')


