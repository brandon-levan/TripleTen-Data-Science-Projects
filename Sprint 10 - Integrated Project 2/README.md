# [Sprint 10 - Integrated Project 2](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2010%20-%20Integrated%20Project%202/Sprint_10_Project.ipynb)

## Skills Learned in Sprint 
- Develop models and evaluate their quality when solving supervised learning problems

## Libraries Used
 - `pandas` `numpy` `matplotlib` `sklearn`
 - *From scikit-learn*
    - `train_test_split` `LinearRegression` `DecisionTreeRegressor` `RandomForestRegressor` `mean_absolute_error` `DummyRegressor` `make_scorer` `cross_val_score`
 
## Problem Statement & Task
**Project Objective -** In this project, I will prepare a prototype of a machine learning model for Zyfra. The company develops efficiency solutions for the heavy metals industry. The model I create should predict the amount of gold recovered from gold ore. I have the data on extraction and purification. The model will optimize for the production of gold concentrate and will aim to eliminate unprofitable parameters.

**For this project, we want to create a model to maximize the amount of gold concentration output throughout the gold extraction process-**
- **rougher concentrate recovery** (*rougher.output.recovery*)
- **final concentrate recovery** (*final.output.recovery*) 

I will explore, prepare, and train a model on data provided by Zafra to optimize these parameters.  

## Project Context 

![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2010%20-%20Integrated%20Project%202/Assets/recovery.jpeg)

*__Where:__*

- **C —** share of gold in the concentrate right after flotation (for finding the rougher concentrate recovery)/after purification (for finding the final concentrate recovery)
 - This is represented in the dataset as `rougher.output.concentrate_au`
- **F —** share of gold in the feed before flotation (for finding the rougher concentrate recovery)/in the concentrate right after flotation (for finding the final concentrate recovery)
 - This is represented in the dataset as `rougher.input.feed_au` 
- **T —** share of gold in the rougher tails right after flotation (for finding the rougher concentrate recovery)/after purification (for finding the final concentrate recovery)
 - This is represented in the dataset as `rougher.output.tail_au`

To predict the coefficient, we need to find the share of gold in the concentrate and the tails. 

## Steps to Complete Project

1. Prepare the data
1.1. Open the files and look into the data
1.2. Check that recovery is calculated correctly. Using the training set, calculate recovery for the rougher.output.recovery feature. Find the MAE between your calculations and the feature values. Provide findings
1.3. Analyze the features not available in the test set. What are these parameters? What is their type
1.4. Perform data preprocessing
2. Analyze the data
2.1. Take note of how the concentrations of metals (Au, Ag, Pb) change depending on the purification stage
2.2. Compare the feed particle size distributions in the training set and in the test set. If the distributions vary significantly, the model evaluation will be incorrect
2.3. Consider the total concentrations of all substances at different stages: raw feed, rougher concentrate, and final concentrate. Do you notice any abnormal values in the total distribution? If you do, is it worth removing such values from both samples? Describe the findings and eliminate anomalies
3. Build the model
3.1. Write a function to calculate the final sMAPE value
3.2. Train different models. Evaluate them using cross-validation. Pick the best model and test it using the test sample. Provide findings

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


