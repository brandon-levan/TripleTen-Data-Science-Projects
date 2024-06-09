# [Sprint 15 - Computer Vision](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2015%20-%20Computer%20Vision/Sprint_15_Project.ipynb)

## Skills Learned in Sprint 
- Learn about the tools of the Keras library
- Understand fully connected networks and convolutional networks
- Learn to train a ResNet model

## Libraries Used
 - `pandas` `numpy` `matplotlib` `tensorflow` `keras`

## Problem Statement & Task

The supermarket chain Good Seed would like to explore whether Data Science can help them adhere to alcohol laws by making sure they do not sell alcohol to people underage. The shops are equipped with cameras in the checkout area which are triggered when a person is buying alcohol. Computer vision methods can be used to determine age of a person from a photo.

*The task* is to build and evaluate a model for verifying people's age. To start working on the task, I will be working with a set of photographs of people with their ages indicated.

## Steps to Complete Project
1. Perform exploratory data analysis to get an overall impression of the dataset.
2. Train and evaluate the model (it needs to be done on the GPU platform).
3. Combine your code, output and findings (from the previous points) in the final Jupyter notebook.
4. Make conclusions of the model evaluation, add them to the notebook.
   
## Data Description

The dataset is stored in the `/datasets/faces/` folder, there you can find
- The `final_files` folder with 7.6k photos
- The `labels.csv` file with labels, with two columns: `file_name` and `real_age`

Given the fact that the number of image files is rather high, it was advisable to avoid reading them all at once, which would greatly consume computational resources. It was recommended to build a generator with the ImageDataGenerator generator. This method was explained earlier in the course.
  
## Results & Findings
Recall that the supermarket chain Good Seed would like to explore whether Data Science can help them adhere to alcohol laws by making sure they do not sell alcohol to people underage. I was asked to conduct that evaluation. The shops are equipped with cameras in the checkout area which are triggered when a person is buying alcohol. Using a sample of photos of people, I built a computer vision model that can predict a person's age.

To complete this project, I used a ResNet50 neural network to predict a person's age by using facial images and evaluated model performance through the use of a mean average error (MAE) loss function. The requirement for this project was that the MAE score not be higher than 8, and I found my model to have a MAE of 7.65. While the model meets the acceptance criteria, the best indicator of where a person is of age to purchase alcohol would be there drivers license. Checking a drivers license would produce much better results than implementing a model that may or may not accurately predict a user's age each time which may have unitended consequences for Good Seed.

## Examples of Visualizations Used in Project
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2015%20-%20Computer%20Vision/Assets/age_distro.png)
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2015%20-%20Computer%20Vision/Assets/images_of_peoples.png)
