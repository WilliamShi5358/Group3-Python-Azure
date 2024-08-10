import streamlit as st
import pandas as pd
import plotly.express as px
# Function to load the preloaded dataset




def filter(loaded_df):
    # Title of the Streamlit app
    st.title('Dashboard for Data Analysis')

    # Initialize an empty DataFrame
    df = pd.DataFrame(loaded_df)
   
    
    # If DataFrame is not empty, display the data and visualizations
    if not df.empty:

        
        # Display basic statistics
        st.header('Basic Statistics')
        st.write(df.describe())

        categoricalCol= df.select_dtypes(include=['object']).columns     
        numericalCol= df.select_dtypes(include=['float64']).columns

        st.header('Lets View the Best or Worst Performers')
        st.sidebar.header('Top/Bottom Performers')
        top_bottom = st.sidebar.selectbox('Select Top or Bottom', ['Top', 'Bottom'])
        top_n = st.sidebar.slider('Select number for range', min_value=1, max_value=50, value=10)
        x_axis_column = st.sidebar.selectbox('Select column for x-axis (string fields)', categoricalCol, index=None)
        y_axis_column = st.sidebar.selectbox('Select column for y-axis (numeric fields)', numericalCol ,index=None)

        if top_bottom == 'Top':
            dataset_bar = df.nlargest(top_n, y_axis_column)
        else:
            dataset_bar = df.nsmallest(top_n, y_axis_column)

        top_chart = px.bar(dataset_bar, x=x_axis_column, y=y_axis_column, title=f'{top_bottom} {top_n} by {y_axis_column}')
        st.plotly_chart(top_chart)

       
    
        
        create_Line_Bar = st.selectbox('Would you like to Create line chart to display analysis over time?', ['No','Yes'])
        if create_Line_Bar == 'Yes':
            time_column = st.selectbox('Select Time colunm', df.columns,index=None)            
            data_column = st.selectbox('Select colunm you want to display over time', df.columns,index=None)          

            # Ensure the time column is numeric
            df[time_column] = pd.to_numeric(df[time_column], errors='coerce')
            df = df.dropna(subset=[time_column])
            df = df.sort_values(by=time_column)
            st.sidebar.header('Line Chart')    
            # Sidebar selection for year range
            min_year = int(df[time_column].min())
            max_year = int(df[time_column].max())
            year_range = st.sidebar.slider('Select range', min_year, max_year, (min_year, max_year))
            # Filter the dataframe by the selected year range
            line_df = df[(df[time_column] >= year_range[0]) & (df[time_column] <= year_range[1])]
            # Check if the data column is numeric or not
            if pd.api.types.is_numeric_dtype(line_df[data_column]):
                # Sum the values if the data column is numeric
                time_series = line_df.groupby(time_column)[data_column].sum().reset_index()
            else:
                # Count the occurrences if the data column is not numeric
                time_series = line_df.groupby(time_column)[data_column].count().reset_index()
            # Create the line chart
            st.line_chart(time_series.set_index(time_column)[data_column])


        
        create_pie_chart = st.selectbox('Would you like to create a pie chart?', ['No', 'Yes'])
        if create_pie_chart == 'Yes':
            category_column = st.selectbox('Select category column for pie chart',categoricalCol,index=None)
            value_column = st.selectbox('Select value column for pie chart', numericalCol,index=None)
            # Sidebar selection for categories to include in the pie chart
            st.sidebar.header('Pie Chart')
            unique_categories = df[category_column].unique()
            selected_categories_for_pie = st.sidebar.multiselect('Select categories to include in pie chart', unique_categories, unique_categories)
            
            # Filter the dataframe by the selected categories
            pie_data = df[df[category_column].isin(selected_categories_for_pie)]
            
            # Aggregate the data for the pie chart
            pie_data = pie_data.groupby(category_column)[value_column].sum().reset_index()

            # Create the pie chart
            pie_chart = px.pie(pie_data, names=category_column, values=value_column, title=f'Pie chart of {value_column} by {category_column}')
            st.plotly_chart(pie_chart)

        create_bar_chart = st.selectbox('Would you like to create a bar chart?', ['No', 'Yes'])
        if create_bar_chart == 'Yes':
            category_column = st.selectbox('Select category column for bar chart', categoricalCol,index=None)
            value_column = st.selectbox('Select value column for bar chart', numericalCol,index=None)

            # Sidebar selection for categories to include in the bar chart
            unique_categories = df[category_column].unique()
            selected_categories_for_bar = st.sidebar.multiselect('Select categories to include in bar chart', unique_categories, unique_categories)            
            # Filter the dataframe by the selected categories
            bar_data = df[df[category_column].isin(selected_categories_for_bar)]            
            # Aggregate the data for the bar chart
            bar_data = bar_data.groupby(category_column)[value_column].sum().reset_index()

            # Create the bar chart
            bar_chart = px.bar(bar_data, x=category_column, y=value_column, title=f'Bar chart of {value_column} by {category_column}')
            st.plotly_chart(bar_chart)
        
