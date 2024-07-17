import streamlit as st
import pandas as pd
import numpy as np
# show app title, header, button, and table
st.header("INFO 4330 - Group 3")
st.subheader('Python Streamlit App hooked with Azure web services')
st.write("hello world ")


if st.button('click here'):
    st.write("show data")

# catch the data from csv and return 
def load_data():
    data=pd.read_csv()
    return data

def filter_data(condition,currData):
    data=currData
    return data