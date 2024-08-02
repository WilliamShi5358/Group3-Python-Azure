import streamlit as st #pip install streamlit
import pandas as pd    #pip install pandas
import numpy as np     #pip install numpy

# show app header,title
st.subheader('INFO 4330 Group 3 Python Streamlit App Deploying by Azure web service')
st.write("Dataset of Global YouTube Statistic CSV for demo streamlit filter ")

#define global variable df 
global df
#Creating a method to upload the csv file, return df as pd dataframe
#reference by https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader
def uploader_csv():
    #set sidebar sub header for file uploader
    st.sidebar.subheader('Single CSV File Upload')
    #deploy streamlit file_uploader method 
      #coding
    # deploy pandas library to read csv file, try and except
      #coding
    return df

#create a method to filter the data, return filtered dataframe, the argument is the pd datafram 
#reference: https://blog.streamlit.io/auto-generate-a-dataframe-filtering-ui-in-streamlit-with-filter_dataframe/
def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    #placed at sidebar, and define the subheader, and created a sentinel as onFilter to turn on the filter function 
    st.sidebar.subheader('Filter Settings')
    onFilter = st.sidebar.checkbox("Add filters")

    if not onFilter:
        return df

    df = df.copy()
    #  coding
    #  coding
    #  coding

    return df


def vitualization():
    path = './data/Global_YouTube_Statistics.csv'
    dataset =pd.read_csv(path)
    #coding for visualization 
    st.bar_chart(dataset.groupby('Country')['Population'].mean(), x_label='Country', y_label='Population')
    st.dataframe(pd.DataFrame(dataset))
    
    #coding for visualization 
 
  
try:
    df = uploader_csv()
except Exception:
    vitualization()
    print('please choose the csv file to upload for web app')

#call datafram filter method 
try: 
   st.dataframe(filter_dataframe(df))
except Exception as e:
   print('please choose the csv file to upload for web app')


