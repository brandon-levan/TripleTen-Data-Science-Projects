# [Sprint 6 - Data Collection and Storage (SQL)](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2006%20-%20Data%20Collection%20and%20Storage%20(SQL)/Sprint_6_Project.ipynb)

## Skills Learned in Sprint 
- How to write SQL queries of varying degrees of complexity
- What regular expressions are good for and how to write them
- How to slice data and write subqueries
- How to use SQL documentation
- How to use aggregate functions
- Various methods for merging tables

## Libraries Used
 - `pandas` `numpy` `matplotlib` `scipy`
 
## Problem Statement & Task
As an analyst for Zuber, a new ride-sharing company that's launching in Chicago, my task is to find patterns in the available information. I want to understand passenger preferences and the impact of external factors on rides. Working with a database, I will analyze data from competitors and test a hypothesis about the impact of weather on ride frequency.

## Data Description

`/datasets/project_sql_result_01.csv`
- `company_name` - taxi company name
- `trips_amount` - the number of rides for each taxi company on November 15-16, 2017.

`/datasets/project_sql_result_04.csv`
- `dropoff_location_name` - Chicago neighborhoods where rides ended
- `average_trips` - the average number of rides that ended in each neighborhood in November 2017.

`/datasets/project_sql_result_07.csv` contains data on rides from the Loop to O'Hare International Airport.
- `start_ts` - pickup date and time
- `weather_conditions` - weather conditions at the moment the ride started
- `duration_seconds` - ride duration in seconds

## Steps to Complete Project
1. Import the files
2. Study the data they contain
3. Make sure the data types are correct
4. Identify the top 10 neighborhoods in terms of drop-offs
5. Make graphs: taxi companies and number of rides, top 10 neighborhoods by number of dropoffs
6. Draw conclusions based on each graph and explain the results
7. Test the hypothesis
   - The average duration of rides from the Loop to O'Hare International Airport changes on rainy Saturdays
  
## Results & Findings

As an analyst for Zuber, a new ride-sharing company that's launching in Chicago, my task was to find patterns in the available information. I wanted to understand passenger preferences and the impact of external factors on rides. Below are some insights from our competitors data that I derived -

- **Insight 1** - Flash Cab had almost double the rides given on Nov 15 and 16, 2017. Flash Cab had 19,558 rides where as Taxi Affiliation Services had 11,422 trips.
- **Insight 2** - The greatest number of rides ended in the Loop. The Loop, River North, Streeterville, and West Loop might be more populous neighborhoods compared to the other neighborhoods in Chicago that made it into the Top 10 dropoff locations.
- **Insight 3** - There is a statistically signficant difference in the average ride duration from the Loop to O'Hare International Airport between rainy and non-rainy Saturdays.

## Examples of Visualizations Used in Project
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2006%20-%20Data%20Collection%20and%20Storage%20(SQL)/Assets/dropoffs.png)
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2006%20-%20Data%20Collection%20and%20Storage%20(SQL)/Assets/trips.png)

