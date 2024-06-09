
# [Sprint 13 - Time Series](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2013%20-%20Time%20Series/Sprint_13_Project.ipynb)

## Skills Learned in Sprint 
- Understand the trends and seasonality of time series
- Learn to create features from time series
- Use obtained features to train a regression model

## Libraries Used
- `pandas` `numpy` `matplotlib` `sklearn`, `statsmodels.tsa` `LGBMRegressor` `CatBoostRegressor` `XGBRegressor`
- *From sklearn*
   - `train_test_split` `StandardScaler` `mean_squared_error` `LinearRegression` `RandomForestRegressor` `GridSearchCV`
- *From statsmodels.tsa*
   - `seasonal_decompose` `adfuller` `AutoReg` `ar_select_order` `ARIMA` `arma_order_select_ic`

## Problem Statement & Task

The Sweet Lift Taxi company has collected historical data on taxi orders at airports. To attract more drivers during peak hours, we need to predict the amount of taxi orders for the next hour. Build a model for such a prediction.

The RMSE metric on the test set should not be more than 48.
 
## Steps to Complete Project
1. Download the data and resample it by one hour
2. Analyze the data
3. Train different models with different hyperparameters. The test sample should be 10% of the initial dataset
4. Test the data using the test sample and provide a conclusion
   
## Data Description

The data is stored in file `taxi.csv`. The number of orders is in the `num_orders` column.
  
## Results & Findings
Given the results generated in section 7, **I would recommend the Sweet Lift Taxi Company implement a XGBoost model if it wants to produce results with the least amount of error (lowest RMSE). However, if the Sweet Lift Taxi Company is concerned with the speed of predictions, the CatBoost model produced a similiar RMSE (within 2% difference) but makes the prediction in half the time.**

| Model    | RMSE When Predicting Targets on Test Set | Prediction Speed |
|----------|------------------------------------------|------------------|
| CatBoost | 37.96                                    | 111 ms           |
| XGBoost  | 37.43                                    | 224 ms           |


## Examples of Visualizations Used in Project
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2013%20-%20Time%20Series/Assets/seasonal_decompose.png)
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2013%20-%20Time%20Series/Assets/randomforrest_predictions.png)
