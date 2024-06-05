# [Sprint 1 - Working With Data in Python](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2001%20-%20Working%20With%20Data%20in%20Python/Sprint_1_Project.ipynb)

### Skills Used in Project
- EDA | Pandas | Data Preprocessing (Finding Duplicates, Filling Missing Values, Outlier Detection) | Data Analysis
  
## Problem Statement
In this project, you will work with data from the entertainment industry. You will study a dataset with records on movies and shows. The research will focus on the "Golden Age" of television, which began in 1999 with the release of The Sopranos and is still ongoing.

The aim of this project is to investigate how the number of votes a title receives impacts its ratings. The assumption is that highly-rated shows (we will focus on TV shows, ignoring movies) released during the "Golden Age" of television also have the most votes.
  
## Data Description

The table contains nine columns. The majority store the same data type: object. The only exceptions are 'release Year' (int64 type), 'imdb sc0re' (float64 type) and 'imdb v0tes' (float64 type). Scores and votes will be used in our analysis, so it's important to verify that they are present in the dataframe in the appropriate numeric format. Three columns ('TITLE', 'imdb sc0re' and 'imdb v0tes') have missing values.

According to the documentation:

 - `name` — actor/director's name and last name
 - `Character` — character played (for actors)
 - `r0le` — the person's contribution to the title (it can be in the capacity of either actor or director)
 - `TITLE` — title of the movie (show)
 - `Type` — show or movie
 - `release Year` — year when movie (show) was released
 - `genres` — list of genres under which the movie (show) falls
 - `imdb sc0re` — score on IMDb
 - `imdb v0tes` — votes on IMDb

## Steps to Complete Project
- Explore data, clean data (find duplicates, fill missing values, convert datatypes, find outliers), perform analysis, conclusions
  
## Results/Findings

The research done confirms that highly-rated shows released during the "Golden Age" of television also have the most votes. While shows with score 4 have more votes than ones with scores 5 and 6, the top three (scores 7-9) have the largest number. The data studied represents around 94% of the original set, so we can be confident in our findings.
