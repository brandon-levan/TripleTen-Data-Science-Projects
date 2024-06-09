# [Sprint 17 - Final Project](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2017%20-%20Final%20Project/Sprint_17_Project.ipynb)

## Problem Statement & Task
**The telecom operator Interconnect would like to be able to forecast their churn of clients.** If it's discovered that a user is planning to leave, they will be offered promotional codes and special plan options. Interconnect's marketing team has collected some of their clientele's personal data, including information about their plans and contracts.

Interconnect mainly provides two types of services:

1. Landline communication. The telephone can be connected to several lines simultaneously.
2. Internet. The network can be set up via a telephone line (DSL, *digital subscriber line*) or through a fiber optic cable.

Some other services the company provides include:

- Internet security: antivirus software (*DeviceProtection*) and a malicious website blocker (*OnlineSecurity*)
- A dedicated technical support line (*TechSupport*)
- Cloud file storage and data backup (*OnlineBackup*)
- TV streaming (*StreamingTV*) and a movie directory (*StreamingMovies*)

The clients can choose either a monthly payment or sign a 1- or 2-year contract. They can use various payment methods and receive an electronic invoice after a transaction.

## Libraries Used
 - `pandas` `numpy` `matplotlib` `sklearn` `lightgbm` `catboost` `xgboost`
 - *From scikit-learn*
    - `train_test_split` `StandardScaler` `GridSearchCV` `LogisticRegression` `mean_squared_error` `DummyClassifier` `RandomForestClassifier`
    -  `accuracy_score` `accuracy_score` `recall_score` `precision_score` `f1_score` `roc_curve` `roc_auc_score` `classification_report`

## Steps to Complete Project

- Step 1 - **Exploratory Data Analysis**
   - In this notebook, I cleaned, combined, and analyzed the datasets Interconnect provided in order to get a better understand and familiarity with users that churn. 
- Step 2 - **Prepare Data For Model Training**
   - Fields need to be scaled and encoded before training the model. Additional, the data needs to be split into train, validation, and test data sets for model training and evaluation. 
- Step 3 -  **Tune & Evaluate Classification Models on Training Data**
   - Perform hyperparameter tuning for a variety of classifcation models. Evaluate accuracy and AUC-ROC scores.Provide findings.
- Step 4 - **Choose Model & Evaluate Performance on Test Data**
   - Based on the accuracy and AUC-ROC scores of model training. Choose the best model and evaluate accuracy and AUC-ROC scores on test data. Provide findings and conclusions. 
    
## Data Description

Four files were provided to me by the telecom operator interconnect to help me forecast their churn of clients - 

`contract.csv` contains customers' contractual information with Interconnect
- `customer_id` - unique ID assigned to each customer <br>
- `begin_date` - sign-up date for each customer
- `end_date` - our target feature, No == customer remains with the service
- `contract_type` - plan type
- `paperless_billing` - way of receiving billing statements
- `payment_method` - method of payment <br>
- `monthly_charges` -  monthly charges for the services provided <br>
- `total_charges` - total charges for the services provided <br>

`personal.csv` contains data about a customer's personal information
- `customer_id` - unique ID assigned to each customer
- `gender` - gender of the customer
- `senior_citizen` - age identifier for each customer
- `partner` - customer husband/wife or partner
- `dependents` - customer dependents

`internet.csv` contains information about Interconnect's internet offerings
- `customer_id` - unique ID assigned to each customer
- `internet_service` - type of internet service
- `online_security` - additional internet service
- `online_backup` - additional internet service
- `device_protection` - additional internet service
- `tech_support` - additional internet service

`phone.csv` contains information about Interconnect's phone offerings
- `customer_id` - unique ID assigned to each customer
- `multiple_lines` - quantity of cell phone lines

Each file contains the primary key customer_id which is leveraged in order to do the data merging. Our primary metric is AUC-ROC. 'end_date` in the contract.csv was used as the target for predicting churn. 

## Results & Findings

**The XGBClassifier predicts test values with an AUC_ROC score of 0.901 and an accuracy score of 0.861.** The XGBClassifier would be a great choice for Interconnect to implement to predict which users are most likely to churn because the predictions are accurate and fast. While XGBClassifier produces the highest AUC_ROC, there are other models that we didn't use to predict test values like tbhe LGBMClassifier and RandomForrestClassifier. These models also have high accuracy scores and AUC_ROC, but the hyperparameter tuning time was around 10 seconds whereas XGBClassifier was over a minute. If Interconnect needs faster tuning and prediction times, consider evaluating these models. However, for our use case, the XGBClassifier meets the mark with both a high accuracy and AUC_ROC scores.

## Examples of Visualizations Used in Project
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2017%20-%20Final%20Project/Assets/categorical_features.png)
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2017%20-%20Final%20Project/Assets/numerical_features.png)
