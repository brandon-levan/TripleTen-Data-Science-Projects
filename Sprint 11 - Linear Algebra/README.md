# [Sprint 11 - Linear Algebra Learning in Business](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2011%20-%20Linear%20Algebra/Sprint_11_Project.ipynb)

## Skills Learned in Sprint 
- Perform common matrix and vector operations using the NumPy library
- Create Python classes for machine learning models
- Develop a deeper understanding of linear regression models

## Libraries Used
 - `pandas` `numpy` `seaborn` `sklearn` `math`
 - *From sklearn*
    - `train_test_split` `NearestNeighbors` `KNeighborsClassifier` `linear_model` `metrics preprocessing`

## Problem Statement & Task
The Sure Tomorrow insurance company wants to solve several tasks with the help of Machine Learning and you are asked to evaluate that possibility.

- **Task 1:** Find customers who are similar to a given customer. This will help the company's agents with marketing.
- **Task 2:** Predict whether a new customer is likely to receive an insurance benefit. Can a prediction model do better than a dummy model?
- **Task 3:** Predict the number of insurance benefits a new customer is likely to receive using a linear regression model.
- **Task 4:** Protect clients' personal data without breaking the model from the previous task. It's necessary to develop a data transformation algorithm that would make it hard to recover personal information if the data fell into the wrong hands. This is called data masking, or data obfuscation. But the data should be protected in such a way that the quality of machine learning models doesn't suffer. You don't need to pick the best model, just prove that the algorithm works correctly.

## Steps to Complete Project
- Load the data
- Check that the data is free of issues — there is no missing data, extreme values, and so on
- Work on each task and answer the questions posed in the project template
- Draw conclusions based on your experience working on the project
   
## Data Description

- `Features`: insured person's gender, age, salary, and number of family members
- `Target`: number of insurance benefits received by an insured person over the last five years
  
## Results & Findings

Conclusions
I've summarized the conclusions from each task below -

- **Task 1 - Similar Customers**
   - Scaling the data does have an affect on the KNN algorithm in terms of the distance the algorithm outputs.
   - There is a difference in the results for the Manhattan distance metric when using scaled and unscaled data.<br>
- **Task 2 - Is Customer Likely to Receive Insurance Benefit?**
   - Increasing the k value doesn't always have a positive affect on improving the F1 score.
   - Using scaled data in a kNN model produces better results than with unscaled data.
- **Task 3 - Regression (with Linear Regression)**
   - RMSE & R^2 values are the same when the linear regression model is run on scaled and unscaled data
- **Task 4 - Obfuscating Data**
   - Between the original and recovered data, the values aren't exactly the same because of rounding (floats vs integers). The transformed data is different than the original and reversed data because it is intended to be obfuscated.
- **Task 5 - Proof That Data Obfuscation Can Work with LR**
   - Obfuscation won't affect linear regression in terms of predicted values or RSME
- **Task 6 - Test Linear Regression With Data Obfuscation**
   - Obfuscating the data has no affect on the results of the linear regression model. When fitting the Linear Regression model to the original and obfuscated training data and predicting the test values, we see the same results in terms of F1 and R2 scores.

## Examples of Visualizations Used in Project
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2011%20-%20Linear%20Algebra/Assets/pairplot.png)

