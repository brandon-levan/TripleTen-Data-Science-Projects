# [Sprint 2 - Exploratory Data Analysis](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2002%20-%20Exploratory%20Data%20Analysis%20(EDA)/Sprint_2_Project.ipynb)

## Skills Learned in Sprint 
- More advanced ways to read and process data of different sources and formats
- How to identify and process missing and duplicate data
- How to visualize data for your own understanding and for presentations to an audience
- More advanced techniques to filter data
- How to create new columns by processing columns in the raw data
- How to group data and combine data from different tables in various ways (merge and concatenation)

## Libraries Used
 - `pandas` `numpy` `matplotlib`
 
## Problem Statement & Task
Instacart is a grocery delivery platform where customers can place a grocery order and have it delivered to them, similar to how Uber Eats and Door Dash work. In this project, I will be working with a dataset that was publicly released by Instacart in a 2017 for a Kaggle competition.

The goal of this project is to clean up the data and prepare a report that gives insight into the shopping habits of Instacart customers.

## Data Description

There are five tables in the enitre Instantcart dataset. These tables provide information on what a user orders, when they order, and what products are in the users orders.

## Steps to Complete Project
- Explore data
- Clean data (find duplicates, fill missing values, convert datatypes, find outliers)
- Perform data analysis
- Makes conclusions
  
## Results & Findings

After checking for missing values and duplicates in the five tables in the Instantcart data set, I was able to uncover several insights in my exploratory data analysis. Here are a few findings -

- **Insight 1:** The most popular time of the day to shop is 10 am
- **Insight 2:** The most popular time of the week to shop is Monday
- **Insight 3:** For those users that place multiple orders, on average people tend to wait 11.1 days until placing another order
- **Insight 4:** On average users will purchase 10.1 items per order

## Examples of Visualizations Used in Project
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/8ce6db8f5f3f9a8b19ad837095671f4dcf5b04ec/Sprint%2002%20-%20Exploratory%20Data%20Analysis%20(EDA)/Charts/hourly_instacart_orders.png)
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/4313ed56dbf2bf24088b483ecd25f4773af4bb15/Sprint%2002%20-%20Exploratory%20Data%20Analysis%20(EDA)/Charts/days_elapsed.png)


