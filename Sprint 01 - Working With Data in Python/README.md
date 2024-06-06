# [Sprint 1 - Working With Data in Python](https://github.com/brandon-levan/TripleTen-Data-Science-Projects/blob/main/Sprint%2001%20-%20Working%20With%20Data%20in%20Python/Sprint_1_Project.ipynb)

### Skills Learned in Sprint
- How to work with large amounts of data in lists and dictionaries
- How to write functions
- How to perform four essential data-focused activities: retrieval, preprocessing, analysis, and presenting results
- How to perform advanced data processing and analysis techniques using the pandas library
- How to work with data and present results using Jupyter Notebook
  
## Problem Statement & Task
In this project, I worked with data from the entertainment industry. I studied a dataset with records on movies and shows. The research will focus on the "Golden Age" of television, which began in 1999 with the release of The Sopranos and is still ongoing.

The aim of this project was to investigate how the number of votes a title receives impacts its ratings. The assumption is that highly-rated shows (we will focus on TV shows, ignoring movies) released during the "Golden Age" of television also have the most votes.

## Libraries Used in Project
- `pandas`
  
## Data Description

The table contains nine columns. The majority store the same data type: object. The only exceptions are 'release Year' (int64 type), 'imdb sc0re' (float64 type) and 'imdb v0tes' (float64 type). Scores and votes will be used in our analysis, so it's important to verify that they are present in the dataframe in the appropriate numeric format. Three columns ('TITLE', 'imdb sc0re' and 'imdb v0tes') have missing values.

*According to the documentation:*

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
- Explore data
- Clean data (find duplicates, fill missing values, convert datatypes, find outliers)
- Perform analysis
- Makes conclusions
  
## Results & Findings

The research done confirms that highly-rated shows released during the "Golden Age" of television also have the most votes. While shows with score 4 have more votes than ones with scores 5 and 6, the top three (scores 7-9) have the largest number. The data studied represents around 94% of the original set, so we can be confident in our findings.
