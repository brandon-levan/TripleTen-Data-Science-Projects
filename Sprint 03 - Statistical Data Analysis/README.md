# [Sprint 3 - Statistical Data Analysis](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2003%20-%20Statistical%20Data%20Analysis/Sprint_3_Project.ipynb)

## Skills Learned in Sprint 
- Learn to choose the optimal metrics for data description
- Assess continuous and discrete variables using histograms of various types
- Draw conclusions about the data based on statistical metrics
- Get familiar with the probability theory
- Define distribution types and learn to calculate both normal and binomial distributions
- Learn to formulate and test hypotheses

## Libraries Used
 - `pandas` `numpy` `matplotlib` `scipy`
 
## Problem Statement & Task
As an analyst for the telecom operator Megaline, I will be doing an analysis for the commerical department on which pre-paid plan (Surf or Ultimate) brings in more revenue for Megaline so that they can adjust the advertising budget accordingly.

The average revenue from users of Ultimate and Surf calling plans differs. The average revenue from users in NY-NJ area is different from that of the users from other regions. Decide what alpha value and explain the hypotheses and the results of the statistical tests run on the data set.

## Data Description

I will be conducting this analysis using a sample of 500 Megaline clients from 2018. The data set I will be working with contains information such as who the clients are, where they're from, which plan they use, and the number of calls they made and text messages they sent.

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

1. Per month in 2018, we see that Ulitmate plan users spend more on average for their plans than surf plan users, however, surf plan users pay more in overages that ultimate plan users.
 - From the data, we can see these overages for surf plan users is largely attributed to GBs used for internet. Overages on internet for the surf plan cost 10 GB for every GB a user goes over the included amount of 15 GB. We don't see this for ultimate plan users. Looking at the box plot there are at least 25% of surf users that go over 15 GBs per month. This adds up fast.
2. With a confidence interval of 95%,
- We see that there is a difference in the average revenue for users in each plan.
- However, we do not see a difference in the average revenue for users when comparing users in the NY/NJ and other regions of the United States

## Examples of Visualizations Used in Project
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2003%20-%20Statistical%20Data%20Analysis/Assets/gigs.png)
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/4313ed56dbf2bf24088b483ecd25f4773af4bb15/Sprint%2002%20-%20Exploratory%20Data%20Analysis%20(EDA)/Charts/days_elapsed.png)
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2003%20-%20Statistical%20Data%20Analysis/Assets/hypothesis.png)
