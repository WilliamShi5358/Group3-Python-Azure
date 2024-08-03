import streamlit as st #pip install streamlit
import pandas as pd    #pip install pandas
import numpy as np     #pip install numpy


# show app header,title
st.subheader('INFO 4330 Group 3 Python Streamlit Filter App')
st.write("Dataset of Global YouTube Statistic CSV ")

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
def dynamic_filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
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
    dataset = pd.DataFrame(dataset)
    #clean dataset
    dataset['Country'] = dataset['Country'].str.replace('india', 'India', case=False)
    #coding for visualization 
    chart1, chart2= st.columns(2)
    with chart1:
        st.bar_chart(dataset.groupby('Country')['subscribers'].sum().sort_values(ascending=False).head(10), x_label='Country', y_label='YouTube  Subscribers')
    with chart2:
       st.bar_chart(dataset.groupby('category')['subscribers'].sum().sort_values(ascending=False).head(10),x_label='Category', y_label='YouTube  Subscribers')
    
    st.dataframe(dataset)    
 

try:
    #user uploads csv file
    df = uploader_csv()
except Exception:
    #if user doesn't uploads csv file, app can show the YouTube statistic dataset by default
    vitualization()
    print('please choose the csv file to upload for web app')

#call datafram filter method 
try: 
   st.dataframe(dynamic_filter_dataframe(df))
except Exception as e:
   print('please choose the csv file to upload for web app')


