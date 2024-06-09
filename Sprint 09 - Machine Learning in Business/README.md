# [Sprint 9 - Machine Learning in Business](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2009%20-%20Machine%20Learning%20in%20Business/Sprint_9_Project.ipynb)

## Skills Learned in Sprint 
- Learn business metrics and how they relate to ML metrics.
- Master the bootstrapping technique and learn to analyze the A/B test results.
- Understand what data labeling is and who the assessors are.

## Libraries Used
 - `pandas` `numpy` `matplotlib` `sklearn`
 - *From scikit-learn*
    - `train_test_split` `LinearRegression` `mean_squared_error`
 
## Problem Statement & Task
**Project Objective** - I work for the OilyGiant mining company, and my task is to find the best place for a new well.

## Steps to Complete Project
**_To choose a new location I will -_**

- Collect the oil well parameters for each of the selected region: oil quality and volume of reserves
- Build a model for predicting the volume of reserves in the new wells
- Pick the oil wells with the highest estimated values
- Pick the region with the highest total profit for the selected oil wells
- Build a model that will help to pick the region with the highest profit margin
- Analyze potential profit and risks using the Bootstrapping technique
   
## Data Description

*Every observation in the dataset contains monthly behavior information about one user. The information given is as follows:*

**Features**
- `id` — unique oil well identifier
- `f0, f1, f2` — three features of points (their specific meaning is unimportant, but the features themselves are significant)

**Target**
- `product` — volume of reserves in the oil well (thousand barrels)

## Results & Findings

To help make it easier to visualize which region OilyGiant mining company should develop in, I created the table below with the findings from each Region - 

| Region       | Lower Bound     | Upper Bound   | Average Profit  | Risk of Losses  |
| -----------  | ------          | ----          | ----            | ----     |
| Region A     |  -4,750,652.92  | 9,493,674.16  | 2,741,939.54   | 21.1%    |
| Region B     |  -473,533.83    | 9,359,388.99  | 4,454,815.22   | 3.2%     |
| Region C     |  -3,624,449.01  | 10,963,629.04 | 3,338,564.25   | 19.2%    |

After all of my analysis, my suggestion would be for OilyGiant mining company to develop in **Region B**. I suggest development in Region B because of the strong results Region B generated as a result of bootstrapping. When we select a sample of the top 200 wells from a larger random sample of 500 wells from each region 1000 times, we start to gain a more realistic understanding of what our profit might be and what the risk of losing money on our investment could be. By running the this experiment 1000 times, we see that Region B not only has the highest average profit for a selection of 200 wells given a random sample of 500, it also has the highest chance of being profitable (3.2% risk of losses). If there were to be losses for Region B, the lower bound for loss is much less extreme compared to the other regions. For example, if your investment is not profitable in Region B, you can expect to lose -473,533.83, whereas in the other two regions, you'd lose over $3 Million. After running our analysis, Region B seems like both a safe and profitable selection for OilyGiant mining company to develop wells in.

## Examples of Visualizations Used in Project
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2009%20-%20Machine%20Learning%20in%20Business/Assets/profit_distribution.png)

