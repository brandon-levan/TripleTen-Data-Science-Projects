# [Sprint 8 - Supervised Learning](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2008%20-%20Surpervised%20Learning/Sprint_8_Project.ipynb)

## Skills Learned in Sprint 
- Learn up new evaluation metrics for classification: precision, recall, F1 score, and AUC-ROC. Calculate their values using the scikit-learn tools.
- Solve imbalanced classification tasks. That includes adjusting class weights and tuning their thresholds.
- Understand the new evaluation metrics for regression: MAE and R². Calculate their values using the scikit-learn tools.
  
## Libraries Used
 - `pandas` `numpy` `matplotlib` `sklearn`
 - *From scikit-learn*
   - `train_test_split` `StandardScaler` `shuffle` `DecisionTreeClassifier` `RandomForestClassifier` `LogisticRegression`
 - *For Model Evaluation*
   - `accuracy_score` `confusion_matrix` `recall_score` `precision_score` `f1_score` `roc_curve` `roc_auc_score`
 
## Problem Statement & Task
**Problem Statement** - Beta Bank customers are leaving: little by little, chipping away every month. The bankers figured out it’s cheaper to save the existing customers rather than to attract new ones. My responsibility will be to predict whether a customer will leave the bank soon. I have the data on clients’ past behavior and termination of contracts with the bank to do this task.

**Project Objective** - I will build a model with the maximum possible F1 score, with the requirement that the F1 score for my model must be at least 0.59.

## Steps to Complete Project
1. Download and prepare the data and explain the procedure
2. Examine the balance of classes
   - Train the model without taking into account the imbalance
3. Improve the quality of the model using at least two approaches to fixing class imbalance
   - Use the training set to pick the best parameters
   - Train different models on training and validation sets to find the best model
4. Perform the final testing

## Data Description

*Every observation in the dataset contains monthly behavior information about one user. The information given is as follows:*

**Features**
- `RowNumber` — data string index 
- `CustomerId` — unique customer identifier 
- `Surname` — surname
- `CreditScore` — credit score 
- `Geography` — country of residence 
- `Gender` — gender
- `Age` — age 
- `Tenure` — period of maturation for a customer’s fixed deposit (years)
- `Balance` — account balance 
- `NumOfProducts` — number of banking products used by the customer
- `HasCrCard` — customer has a credit card
- `IsActiveMember` — customer’s activeness 
- `EstimatedSalary` — estimated salary 

**Target**
- `Exited` — сustomer has left
  
## Results & Findings

Mobile carrier Megaline has found out that many of their subscribers use legacy plans. They want to develop a model that would analyze subscribers' behavior and recommend one of Megaline's newer plans: Smart or Ultra. After testing and tuning a few classification models on behavioral data about subscribers who have already switched to the new plans, I would suggest to Megaline to implement a Decision Tree Classification Model with depth of 3 in order to pick the right plan for subscribers on legacy plans. This model had the highest accuracy of all three classification models and is above the acceptable accuracy threshold of 75%.

## Examples of Code Used in Project
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2008%20-%20Surpervised%20Learning/Assets/balance.png)
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2008%20-%20Surpervised%20Learning/Assets/compare.png)
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2008%20-%20Surpervised%20Learning/Assets/train.png)

