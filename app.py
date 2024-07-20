import streamlit as st
import pandas as pd
import numpy as np

# catch the data from csv and return 
def load_data():
    #should catch data from oneDrive cloud, for now just use local data for demo 
    path = './data/USA_Housing.csv'
    df=pd.read_csv(path)
    return df

#create a funciton to filter the data
def filter_data(data):
    price_to_filter = st.slider('Home Price', min_value=1000000, max_value=2000000, value=(1000000,1200000))
    filtered_df = data[data['Price'].between(*price_to_filter)]
    st.dataframe(filtered_df)
    
def column_selector(data): 
    areaIncome = currList['Avg. Area Income']
    houseAge= currList['Avg. Area House Age']
    areaPopulation= currList['Area Population']
    houseAge_choice = st.sidebar.selectbox('Select your home age', houseAge)
    areaIncome_choice = st.sidebar.selectbox('Select your area income:', areaIncome)
    areaPopulation_choice = st.sidebar.selectbox('Select your area population',areaPopulation)  


# show app title, header, button, and table
st.header("INFO 4330 - Group 3")
st.subheader('Python Streamlit App hooked with Azure web services')
st.write("USA Housing Data for demo streamlit filter ")

#load data
currList= load_data()

#click the button to show the list and filter
#if st.button('click here to see all'):
#   st.write(currList)
   
filter_data(currList)
column_selector(currList)


