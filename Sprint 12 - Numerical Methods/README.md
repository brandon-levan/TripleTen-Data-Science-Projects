
# [Sprint 12 - Numerical Methods](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2012%20-%20Numerical%20Methods/Sprint_12_Project.ipynb)

## Skills Learned in Sprint 
- Write a gradient descent algorithm
- Understand how linear regression models and neural networks are trained using gradient descent
- Master the gradient boosting technique

## Libraries Used
 - `pandas` `numpy` `sklearn` `LGBMRegressor` `CatBoostRegressor` `XGBRegressor`
 - *From sklearn*
    - `train_test_split` `StandardScaler` `mean_squared_error` `LinearRegression` `RandomForestRegressor` `GridSearchCV`

## Problem Statement & Task

Rusty Bargain is a used car sales service is developing an app to attract new customers. In that app, you can quickly find out the market value of your car. You have access to historical data: technical specifications, trim versions, and prices. The task is to build the model to determine the value.

Rusty Bargain is interested in - 
- the quality of the prediction
- the speed of the prediction
- the time required for training
 
**The goal of this project** is to train different models with various hyperparameters. The goal is to compare gradient boosting methods with random forest, decision tree, and linear regression.

## Steps to Complete Project
1. Download and look at the data.
2. Train different models with various hyperparameters (You should make at least two different models, but more is better. Remember, various implementations of gradient boosting don't count as different models.) The main point of this step is to compare gradient boosting methods with random forest, decision tree, and linear regression.
3. Analyze the speed and quality of the models.
   
## Data Description

- **Features**
  - `DateCrawled` — date profile was downloaded from the database
  - `VehicleType — vehicle body type
  - `RegistrationYear` — vehicle registration year
  - `Gearbox` — gearbox type
  - `Power` — power (hp)
  - `Model` — vehicle model
  - `Mileage` — mileage (measured in km due to dataset's regional specifics)
  - `RegistrationMonth` — vehicle registration month
  - `FuelType` — fuel type
  - `Brand` — vehicle brand
  - `NotRepaired` — vehicle repaired or not
  - `DateCreated` — date of profile creation
  - `NumberOfPictures` — number of vehicle pictures
  - `PostalCode` — postal code of profile owner (user)
  - `LastSeen` — date of the last activity of the user

- **Target**
   - `Price` — price (Euro)
  
## Results & Findings
Given the results generated in section 8, **the Rusty Bargain should implement a Catboost model to make its predictions.** It is extremely fast in making predictions and it produced the lowest RMSE (compared to the RandomForrestRegressor).

| Model            | RMSE When Predicting Targets on Test Set | Prediction Speed  |
|------------------|------------------------------------------|-------------------|
| LinearRegression |                  3168.3                  | 19.3 seconds      |
| RandomForrest    |                  2007.0                  | 1 mins 26 seconds |
| **CatBoost**         |                  1970.08                 | 4.24 s            |
