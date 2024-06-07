# [Sprint 7 - Introduction to ML](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2007%20-%20Introduction%20to%20ML/Sprint_7_Project.ipynb)

## Skills Learned in Sprint 
- To understand basic machine learning terminology. For example, the difference between classification and regression, or the difference between a model and a learning algorithm.
- To master the scikit-learn library, learn to measure evaluation metrics and train models.
- To learn how to examine models and pick the best one.
 
## Problem Statement & Task
**Problem Summary** - Mobile carrier Megaline has found out that many of their subscribers use legacy plans. They want to develop a model that would analyze subscribers' behavior and recommend one of Megaline's newer plans: Smart or Ultra. Because I have access to behavioral data about subscribers who have already switched to the new plans, I will develop a classification model that will pick the right plan for subscribers on legacy plans.

**Objective** - Develop a model with the highest possible accuracy. In this project, the threshold for accuracy is 0.75.

## Libraries Used
 - `pandas`, `numpy`, `matplotlib`, `sklearn` 
 - train_test_split, DecisionTreeClassifier, RandomForestClassifier, LogisticRegression, accuracy_score, 

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
1. Open and look through the data file
2. Split the data into a training set, a validation set, and a test set
3. Investigate the quality of different models by changing hyperparameters and describe the findings
4. Check the quality of the model using the test set
  
## Results & Findings

As an analyst for Zuber, a new ride-sharing company that's launching in Chicago, my task was to find patterns in the available information. I wanted to understand passenger preferences and the impact of external factors on rides. Below are some insights from our competitors data that I derived -

- **Insight 1** - Flash Cab had almost double the rides given on Nov 15 and 16, 2017. Flash Cab had 19,558 rides where as Taxi Affiliation Services had 11,422 trips.
- **Insight 2** - The greatest number of rides ended in the Loop. The Loop, River North, Streeterville, and West Loop might be more populous neighborhoods compared to the other neighborhoods in Chicago that made it into the Top 10 dropoff locations.
- **Insight 3** - There is a statistically signficant difference in the average ride duration from the Loop to O'Hare International Airport between rainy and non-rainy Saturdays.

## Examples of Visualizations Used in Project
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2006%20-%20Data%20Collection%20and%20Storage%20(SQL)/Assets/dropoffs.png)
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2006%20-%20Data%20Collection%20and%20Storage%20(SQL)/Assets/trips.png)

