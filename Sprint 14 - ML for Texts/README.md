# [Sprint 14 - ML for Texts](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2014%20-%20ML%20for%20Texts/Sprint_14_Project.ipynb)

## Skills Learned in Sprint 
- Learn to calculate TF-IDF values for texts
- Figure out how to create embeddings with a BERT model
- Build a classification model for texts

## Libraries Used
 - `pandas` `numpy` `matplotlib` `seaborn`, `sklearn` `nltk` `spacy`

## Problem Statement & Task

The Film Junky Union, a new edgy community for classic movie enthusiasts, is developing a system for filtering and categorizing movie reviews. The goal is to train a model to automatically detect negative reviews. You'll be using a dataset of IMBD movie reviews with polarity labelling to build a model for classifying positive and negative reviews. The model will need to have an F1 score of at least 0.85.
 
## Steps to Complete Project
1. Load the data
2. Preprocess the data, if required
3. Conduct an EDA and make your conclusion on the class imbalance
4. Preprocess the data for modeling
5. Train at least three different models for the given train dataset
6. Test the models for the given test dataset
7. Compose a few of your own reviews and classify them with all the models
8. Check for differences between the testing results of models in the above two points. Try to explain them
9. Present your findings
   
## Data Description

The data is stored in the `imdb_reviews.tsv` file. 

The data was provided by Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng, and Christopher Potts. (2011). Learning Word Vectors for Sentiment Analysis. The 49th Annual Meeting of the Association for Computational Linguistics (ACL 2011).

Here's the description of the selected fields:

 - `review`: the review text
 - `pos`: the target, '0' for negative and '1' for positive
 - `ds_part`: 'train'/'test' for the train/test part of dataset, correspondingly
 
*There are other fields in the dataset. Feel free to explore them if you'd like.*
  
## Results & Findings
The Film Junky Union, a new edgy community for classic movie enthusiasts, is developing a system for filtering and categorizing movie reviews. **The goal is to train a model to automatically detect negative reviews with an F1 score of at least 0.85.** We see that when using different models and methdologies, Models 1,2, and 3 all produce F1 scores higher than 0.85; however, **models using LinearRegression produce the best F1 score.** I would avoid using spaCy going forward because text preprocessing took 16 mins and produced the same results as using NLTK which took significantly less time to run (11 seconds).

| Model/Methodology                          | Test Accuracy | Test F1 | Test APS | Test ROC AUC |
|--------------------------------------------|---------------|---------|----------|--------------|
| Model 0 - DummyClassifier                  | 0.50          | 0.50    | 0.50     | 0.50         |
| Model 1 - NLTK, TF-IDF and LR              | 0.88          | 0.88    | 0.95     | 0.95         |
| Model 2 - spaCy, TF-IDF and LR             | 0.88          | 0.88    | 0.95     | 0.95         |
| Model 3 - spaCy, TF-IDF and LGBMClassifier | 0.86          | 0.86    | 0.93     | 0.94         |


## Examples of Visualizations Used in Project
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2014%20-%20ML%20for%20Texts/Assets/movies_over_years.png)
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2014%20-%20ML%20for%20Texts/Assets/distribution_of_ratings.png)
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2014%20-%20ML%20for%20Texts/Assets/scores.png)
