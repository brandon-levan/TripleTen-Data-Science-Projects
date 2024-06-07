# [Sprint 10 - Integrated Project 2](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2010%20-%20Integrated%20Project%202/Sprint_10_Project.ipynb)

## Skills Learned in Sprint 
- Supervised learning - develop models and evaluate their quality for both regression and classification tasks

## Libraries Used
 - `pandas` `numpy` `matplotlib` `sklearn`
 - *From scikit-learn* - `train_test_split` `LinearRegression` `DecisionTreeRegressor` `RandomForestRegressor` `mean_squared_error` `DummyRegressor`,`make_scorer`,`cross_val_score`
 
## Problem Statement & Task
**Project Objective** - I work for the OilyGiant mining company, and my task is to find the best place for a new well.

![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2010%20-%20Integrated%20Project%202/Assets/recovery.jpeg)

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

Compared to the baseline results of the DummyRegressor model (9.73), the DecisionTreeRegressor produces a slightly better model performance in regards to Final sMAPE (9.38). Given these results, I would implement a DecisionTreeRegressor model for Zyfra to predict the amount of gold recovered from gold ore with the smallest mean average error between the true values and predict values.

## Examples of Visualizations Used in Project
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2010%20-%20Integrated%20Project%202/Assets/particle_size.png)
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2010%20-%20Integrated%20Project%202/Assets/outputs.png)


