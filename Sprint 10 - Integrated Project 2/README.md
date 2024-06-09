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
In order to start working on this process, I needed to familiarize myself with the gold extraction process. Mined ore undergoes primary processing to get the ore mixture or rougher feed, which is the raw material for flotation (also known as the rougher process). After flotation, the material is sent to two-stage purification. After the floatation and the two-stage purification steps, you are left with the final gold concentrate. The process of taking a gold ore mixture and extracting gold concentrate will be refferred to as recovery or the recovery process. 

![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2010%20-%20Integrated%20Project%202/Assets/gold_process.jpeg)

For this project, we need to simulate the process of recovering gold from gold ore. The following formula can be used to simulate the recovery process:

![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2010%20-%20Integrated%20Project%202/Assets/recovery.jpeg)

*__Where:__*

- **C —** share of gold in the concentrate right after flotation (for finding the rougher concentrate recovery)/after purification (for finding the final concentrate recovery)
 - This is represented in the dataset as `rougher.output.concentrate_au`
- **F —** share of gold in the feed before flotation (for finding the rougher concentrate recovery)/in the concentrate right after flotation (for finding the final concentrate recovery)
 - This is represented in the dataset as `rougher.input.feed_au` 
- **T —** share of gold in the rougher tails right after flotation (for finding the rougher concentrate recovery)/after purification (for finding the final concentrate recovery)
 - This is represented in the dataset as `rougher.output.tail_au`

In this problem, we need a way to assess how well the model works - in other words - how good are the predictions the model outputs based on the training data. To do this, will need a new metric. It is called sMAPE, symmetric Mean Absolute Percentage Error. sMAPE will be the evaluation metric used in this project and it is calculated using the equation below

![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2010%20-%20Integrated%20Project%202/Assets/smape.jpeg)

As I noted earlier, we want to create a model to maximize the amount of gold concentration output throughout the gold extraction process-**
- **rougher concentrate recovery** (*rougher.output.recovery*)
- **final concentrate recovery** (*final.output.recovery*) 
Therefore, we need to predict the rougher concentrate recovery `rougher.output.recovery` and final concentrate recovery `final.output.recovery`. Using sMAPE and these predictions, we will use the **Final sMAPE** to assess how well each model performs in maximizing gold output by looking at which model produces the lowests final sMAPE

![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2010%20-%20Integrated%20Project%202/Assets/final_smape.jpeg)

## Steps to Complete Project

- Step 1 - Prepare the data
   - Open the files and look into the data
   - Check that recovery is calculated correctly. Using the training set, calculate recovery for the rougher.output.recovery feature. Find the MAE between your calculations and the feature values. Provide findings
   - Analyze the features not available in the test set. What are these parameters? What is their type
   - Perform data preprocessing
- Step 2 - Analyze the data
   - Take note of how the concentrations of metals (Au, Ag, Pb) change depending on the purification stage
   - Compare the feed particle size distributions in the training set and in the test set. If the distributions vary significantly, the model evaluation will be incorrect
   - Consider the total concentrations of all substances at different stages: raw feed, rougher concentrate, and final concentrate. Do you notice any abnormal values in the total distribution? If you do, is it worth removing such values from both samples? Describe the findings and eliminate anomalies
- Step 3 - Build the model
   - Write a function to calculate the final sMAPE value
   - Train different models. Evaluate them using cross-validation. Pick the best model and test it using the test sample. Provide findings

## Data Description

#### Technological process

- Rougher feed — raw material
- Rougher additions (or reagent additions) — flotation reagents: Xanthate, Sulphate, Depressant
- Xanthate — promoter or flotation activator;
- Sulphate — sodium sulphide for this particular process;
- Depressant — sodium silicate.
- Rougher process — flotation
- Rougher tails — product residues
- Float banks — flotation unit
- Cleaner process — purification
- Rougher Au — rougher gold concentrate
- Final Au — final gold concentrate

#### Parameters of stages
- air amount — volume of air
- fluid levels
- feed size — feed particle size
- feed rate
- Feature naming
  
#### Here's how you name the features:

[stage].[parameter_type].[parameter_name]
Example: rougher.input.feed_ag

Possible values for [stage]:
- rougher — flotation
- primary_cleaner — primary purification
- secondary_cleaner — secondary purification
- final — final characteristics

Possible values for [parameter_type]:
- input — raw material parameters
- output — product parameters
- state — parameters characterizing the current state of the stage
- calculation — calculation characteristics
  
## Results & Findings

Compared to the baseline results of the DummyRegressor model (9.73), the DecisionTreeRegressor produces a slightly better model performance in regards to Final sMAPE (9.38). Given these results, I would implement a DecisionTreeRegressor model for Zyfra to predict the amount of gold recovered from gold ore with the smallest mean average error between the true values and predict values.

## Examples of Visualizations Used in Project
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2010%20-%20Integrated%20Project%202/Assets/particle_size.png)
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2010%20-%20Integrated%20Project%202/Assets/outputs.png)


