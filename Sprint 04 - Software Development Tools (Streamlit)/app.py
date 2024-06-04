# Import Libraries 
import pandas as pd 
import streamlit as st
import plotly.express as px
import os 

# Provide info about project
st.title('TripleTen: Project Four')
st.subheader('Car Advertisement Analysis By Brandon Levan')
st.write("Using a car advertisement data set, I've created two plots below that visual how certain attributes impact used car sales. [Here is the link to my GitHub Repository That Generates This Web App](https://github.com/brandon-levan/TripleTen_Sprint_Four_Project)")

# Add divider
st.divider()

# Create variable path to csv 
path = os.path.dirname(__file__)
my_file = path+'/vehicles_us.csv'

# Read in csv
vehicles = pd.read_csv(my_file)

# Replace Missing Values 
# Model Year - I will replace null values with a 0. Since we know that there weren't cars made in year 0, this will be a catch-all for cars without a model year
vehicles['model_year'].fillna(0, inplace=True)

# Cylinders - I will replace Cylinders with the median value of the same vehicle type that was sold. Making the assumption that the median cylinder by type most closely resemble how many cylinders the vehcile may have, if it had a missing value.
vehicles['cylinders'] = vehicles['cylinders'].fillna(vehicles.groupby('type')['cylinders'].transform('median'))

# Odomoter -  I will replace Odometer with the median value of the same vehicle type that was sold. Because Odometer must be an integer and because 0 represents a new car, I will set the missing value with an average value for all sold vehicles in the dataset of the same vehicle type. 
vehicles['odometer'] = vehicles['odometer'].fillna(vehicles.groupby('type')['odometer'].transform('median'))

# Paint Color - I will replace null values with the string 'Unknown' and convert paint_color to be a string.
vehicles['paint_color'].fillna('Unknown', inplace=True)

# Is 4WD - I will replace null values with 0. Currently, when is_4wd is 1, this means that the vehicle has four-wheel drive. If zero, we can assume that the vehicle either doesn't have four wheel drive or that the value is unknown. 
vehicles['is_4wd'].fillna(0, inplace=True)

# Convert data types 
vehicles['price'] = vehicles['price'].astype(float)
vehicles['model_year'] = vehicles['model_year'].astype('Int64')
vehicles['model'] = vehicles['model'].astype(str)
vehicles['condition'] = vehicles['condition'].astype(str)
vehicles['cylinders'] = vehicles['cylinders'].astype('Int64')
vehicles['fuel'] = vehicles['fuel'].astype(str)
vehicles['odometer'] = vehicles['odometer'].astype(float)
vehicles['transmission'] = vehicles['transmission'].astype(str)
vehicles['type'] = vehicles['type'].astype(str)
vehicles['paint_color'] = vehicles['paint_color'].astype(str)
vehicles['is_4wd'] = vehicles['is_4wd'].astype('Int64')
vehicles['date_posted'] = vehicles['date_posted'].astype('datetime64[ns]')
vehicles['days_listed'] = vehicles['days_listed'].astype('Int64')

# Change column names
vehicles = vehicles.rename(columns={"price": "Price", "model_year": "Model Year", "model": "Model", "condition": "Condition", "cylinders": "Cylinders", "fuel": "Fuel", "odometer": "Odometer", "transmission": "Transmission", "type": "Type", "paint_color": "Paint Color", "is_4wd": "Is 4WD", "date_posted": "Date Posted", "days_listed": "Days Listed"})

# Create header
st.header("How Each Attribute Affects a Car's Selling Price")

# Create toggle that allows user to hide or show the scatter plot. Default toggle to true
plot_one = st.toggle('Toggle off to Hide Scatter Plot', value=True)

# If the toggle is set to true than show the scatter plot
if plot_one:

    # Use radio button to allow users to choose which attribute they want to use as the x-axis to compare against price
    genre = st.radio("Choose Which Attribute You Want to use as the X-Axis"
                    , ["Cylinders", "Model Year", "Condition"]
                    , index=0
                    , horizontal=True
                    )
    
    # Add Slider to Adjust Date to Filter Out Year 0
    values = st.slider(
        'Select Model Years of Interest - Note: Model Year 0 Means Vehicle was Listed Without a Model Year',
        0, 2020, (0, 2020))

    # Create a vehicles data frame that filters with model year slider
    vehicles_filtered = vehicles[vehicles["Model Year"].between(values[0], values[1])]

    # Configure parameters of Scatter Plot
    fig_one = px.scatter(vehicles_filtered, x=genre, y="Price", color = "Condition", symbol="Condition", hover_data=['Model'], title= "Scatter plot of " + genre + " vs. Price")
    
    # Plot Scatter Plot
    # If I wanted to take this one step further, I could use a streamlit slider to filter out model year 0 
    st.plotly_chart(fig_one, theme="streamlit", use_container_width=True)

# Create toggle that allows user to hide or show the histogram. Default toggle to true
plot_two = st.toggle('Toggle off to Hide Histogram', value=True)

# If the toggle is set to true than show the histogram
if plot_two:

    # Use select box to allow users to choose which attribute they want to use as the color option.
    # Histogram will box count by model year and color option 
    # Took a few attributes just to demonstrate usage of select box feature 
    option = st.selectbox("You'd Like to see Count of Car Sales By Model Year and..."
                         , ('Type', 'Paint Color', 'Transmission', 'Condition')
                         )
    
    # Add Slider to Adjust Date to Filter Out Year 0
    values_two = st.slider(
        'Select Model Years of Interest - Note: Model Year 0 Means Vehicle was Listed Without a Model Year ',
        0, 2020, (0, 2020))

    # Create a vehicles data frame that filters with model year slider
    vehicles_filtered = vehicles[vehicles["Model Year"].between(values_two[0], values_two[1])]

    # Configure parameters of Histogram
    fig_two = px.histogram(vehicles_filtered, x="Model Year", color= option, title= "Histogram of Model Year vs. " + option)
    
    # Plot Histogram 
    st.plotly_chart(fig_two, theme="streamlit", use_container_width=True)



