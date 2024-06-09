# [Sprint 7 - Introduction to ML](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2007%20-%20Introduction%20to%20ML/Sprint_7_Project.ipynb)

## Skills Learned in Sprint 
- To understand basic machine learning terminology. For example, the difference between classification and regression, or the difference between a model and a learning algorithm.
- To master the scikit-learn library, learn to measure evaluation metrics and train models.
- To learn how to examine models and pick the best one.

## Libraries Used
 - `pandas` `numpy` `matplotlib` `sklearn`
 -  *From scikit-learn*
    - `train_test_split` `DecisionTreeClassifier` `RandomForestClassifier` `LogisticRegression` `accuracy_score` 
 
## Problem Statement & Task
**Problem Summary** - Mobile carrier Megaline has found out that many of their subscribers use legacy plans. They want to develop a model that would analyze subscribers' behavior and recommend one of Megaline's newer plans: Smart or Ultra. Because I have access to behavioral data about subscribers who have already switched to the new plans, I will develop a classification model that will pick the right plan for subscribers on legacy plans.

**Objective** - Develop a model with the highest possible accuracy. In this project, the threshold for accuracy is 0.75.

## Data Description

Every observation in the dataset contains monthly behavior information about one user. The information given is as follows:

- `сalls` — number of calls
- `minutes` — total call duration in minutes
- `messages` — number of text messages
- `mb_used` — Internet traffic used in MB
- `is_ultra` — plan for the current month (Ultra - 1, Smart - 0)

## Steps to Complete Project
1. Open and look through the data file
2. Split the data into a training set, a validation set, and a test set
3. Investigate the quality of different models by changing hyperparameters and describe the findings
4. Check the quality of the model using the test set
  
## Results & Findings

Mobile carrier Megaline has found out that many of their subscribers use legacy plans. They want to develop a model that would analyze subscribers' behavior and recommend one of Megaline's newer plans: Smart or Ultra. After testing and tuning a few classification models on behavioral data about subscribers who have already switched to the new plans, I would suggest to Megaline to implement a Decision Tree Classification Model with depth of 3 in order to pick the right plan for subscribers on legacy plans. This model had the highest accuracy of all three classification models and is above the acceptable accuracy threshold of 75%.

## Examples of Visualizations Used in Project
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2007%20-%20Introduction%20to%20ML/Assets/histogram.png)


