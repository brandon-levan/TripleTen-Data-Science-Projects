# [Sprint 5 - Integrated Project 1](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2005%20-%20Integrated%20Project%201/Sprint_5_Project.ipynb)

## Skills Used in This Project (Learned in Previous Sprints)
- Perform four essential data-focused activities: retrieval, preprocessing, analysis, and presenting results
- Perform advanced data processing and analysis techniques using the pandas library
- Work with data and present results using Jupyter Notebook
- Identify and process missing and duplicate data
- Group data and combine data from different tables in various ways (merge and concatenation)
- Draw conclusions about the data based on statistical metrics
- Define distribution types and learn to calculate both normal and binomial distributions
- Formulate and test hypotheses

## Libraries Used
 - `pandas` `numpy` `matplotlib` `scipy` `seaborn`
 
## Problem Statement & Task
I work for an online store called Ice, which sells video games all over the world. User and expert reviews, genres, platforms (e.g. Xbox or PlayStation), and historical data on game sales are available from open sources. In this project I will identify patterns that determine whether a game succeeds or not. This will allow me to spot potential big winners and plan advertising campaigns. I have data going back to 2016, and I'm planning a campaign for 2017.

## Data Description

- `Name` - Name of game
- `Platform` - Platform game was released on
- `Year_of_Release` - Year of game release
- `Genre` - Genre of game
- `NA_sales` - North American sales in USD million
- `EU_sales` - sales in Europe in USD million
- `JP_sales` - sales in Japan in USD million
- `Other_sales` - sales in other countries in USD million
- `Critic_Score` - maximum of 100
- `User_Score` - maximum of 10
- `Rating (ESRB)` - The Entertainment Software Rating Board evaluates a game's content and assigns an age rating such as Teen or Mature.

## Steps to Complete Project
- Step 1. Open the data file and study the general information
- Step 2. Prepare the data
  - Replace column names, convert the data types, handle with missing values, calculate the total sales for each game
- Step 3. Analyze the data in a variety of ways. For example,
  - Look at how many games were released in different years.
  - Look at how sales varied from platform to platform.
  - Look at platforms that used to be popular but now have zero sales
  - Many more...
- Step 4. Create a user profile for each region by,
  - For each region (NA, EU, JP), determine:
  - The top five platforms. Describe variations in their market shares from region to region.
  - The top five genres. Explain the difference.
  - Do ESRB ratings affect sales in individual regions?
- Step 5. Test the following hypotheses:
  - Average user ratings of the Xbox One and PC platforms are the same.
  - Average user ratings for the Action and Sports genres are different.
  
## Results & Findings

Recall that it's December 2016 and I'm planning a video game advertising campaign for 2017. From my analysis of video game sales data from 2014 through 2016, I have a few important takeaways that I think will help my business sell more games in 2017 based on what we've historically seen in the past few years. Those findings are

1. The platforms with high sales and popularity going into 2017 are the 3DS, PS4, and Xbox One
2. In North America, the highest grossing genres are similiar to those in Europe: Shooters, Action, Sports, and Role-Playing. In Japan, the top genres by sales are Role-Playing and Action. For this reason, I will focus on advertising these genres.
3. Games with E or M ratings tend to have high sales compared to other ESRB ratings
4. There is a moderate positive correlation between critic score and sales for the PS4, so I will advertise any games for the PS4 with a high critic score. It would be beneficial to check if this holds true across other platforms so that I can keep my eyes open for high critic scores.
   
With these few insights, I can try to optimizing my advertising campaign for 2017 to increase sales.

## Examples of Visualizations Used in Project
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2005%20-%20Integrated%20Project%201/Assets/bars.png)
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2005%20-%20Integrated%20Project%201/Assets/critic_score_scatter.png)
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2005%20-%20Integrated%20Project%201/Assets/histograms.png)
![alt text](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2005%20-%20Integrated%20Project%201/Assets/sales_by_platform.png)
