# [Sprint 3 - Statistical Data Analysis](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2003%20-%20Statistical%20Data%20Analysis/Sprint_3_Project.ipynb)

### Skills Learned in Sprint 
- Learn to choose the optimal metrics for data description
- Assess continuous and discrete variables using histograms of various types
- Draw conclusions about the data based on statistical metrics
- Get familiar with the probability theory
- Define distribution types and learn to calculate both normal and binomial distributions
- Learn to formulate and test hypotheses
 
## Problem Statement & Task
Instacart is a grocery delivery platform where customers can place a grocery order and have it delivered to them, similar to how Uber Eats and Door Dash work. In this project, I will be working with a dataset that was publicly released by Instacart in a 2017 for a Kaggle competition.

The goal of this project is to clean up the data and prepare a report that gives insight into the shopping habits of Instacart customers.

## Libraries Used
 - `pandas`, `numpy`, `matplotlib`, `scipy`

## Data Description

There are five tables in the enitre Instantcart dataset. These tables provide information on what a user orders, when they order, and what products are in the users orders.

## Steps to Complete Project
- Step 1: Read in the data files and study the general information in those files
- Step 2: Preprocess the data by doing the following:
  - Verify and fix data types
  - Identify and fill in missing values
  - Identify and remove duplicate values
  - Find and eliminate errors in the data
- Step 3: Aggregate User Level Metrics
  - Generate metrics such as monthly calls made, minutes used per month, texts sent per month, and more.
- Step 4: Describe the customers' behavior by analyzing the data
  - After finding the minutes, texts, and volume of data the users of each plan require per month. Calculate the mean, variance, and standard deviation. Plot histograms. Describe the distributions.
- Step 5: Test the hypotheses
  A- The average revenue from users of Ultimate and Surf calling plans differs. The average revenue from users in NY-NJ area is different from that of the users from other regions. Decide what alpha value and explain the hypotheses and the results of the statistical tests run on the data set.
- Step 6: Summarize Findings and Make a Conclusion
  
## Results & Findings

After checking for missing values and duplicates in the five tables in the Instantcart data set, I was able to uncover several insights in my exploratory data analysis. Here are a few findings -

- **Insight 1:** The most popular time of the day to shop is 10 am
- **Insight 2:** The most popular time of the week to shop is Monday
- **Insight 3:** For those users that place multiple orders, on average people tend to wait 11.1 days until placing another order
- **Insight 4:** On average users will purchase 10.1 items per order

## Examples of Visualizations Used in Project
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2003%20-%20Statistical%20Data%20Analysis/Assets/gigs.png)
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/4313ed56dbf2bf24088b483ecd25f4773af4bb15/Sprint%2002%20-%20Exploratory%20Data%20Analysis%20(EDA)/Charts/days_elapsed.png)
