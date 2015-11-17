'''
Pandas Homework with IMDb data
'''

'''
BASIC LEVEL
'''
import pandas as pd
import matplotlib.pyplot as plt
import csv
# read in 'imdb_1000.csv' and store it in a DataFrame named movies


path = 'imdb_1000.csv'
movies = pd.read_csv(path)
# check the number of rows and columns
movies.shape
#979 x 6 columns

# check the data type of each column
movies.columns
movies.dtypes

# calculate the average movie duration
movies.duration.mean()

# sort the DataFrame by duration to find the shortest and longest movies

movies.duration.order()

# create a histogram of duration, choosing an "appropriate" number of bins
plt.rcParams['figure.figsize'] = (8, 6)
plt.rcParams['font.size'] = 14

movies.duration.plot(kind='hist', bins=10)
# use a box plot to display that same data
movies.boxplot(column = 'duration')

'''
INTERMEDIATE LEVEL
'''

# count how many movies have each of the content ratings
movies.content_rating.value_counts()

# use a visualization to display that same data, including a title and x and y labels
movies.content_rating.value_counts().plot(kind='bar', title = 'Density of Movie Ratings')
plt.xlabel('Rating')
plt.ylabel('Number of movies')


# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP
movies.content_rating.replace('NOT RATED', 'UNRATED', inplace=True)
movies.content_rating.replace('APPROVED', 'UNRATED', inplace=True)
movies.content_rating.replace('PASSED', 'UNRATED', inplace=True)
movies.content_rating.replace('GP', 'UNRATED', inplace=True)

# convert the following content ratings to "NC-17": X, TV-MA
movies.content_rating.replace('X', 'NC-17', inplace=True)
movies.content_rating.replace('TV-MA', 'NC-17', inplace=True)

# count the number of missing values in each column
movies.isnull().sum()

# if there are missing values: examine them, then fill them in with "reasonable" values
movies[movies.content_rating.isnull()] 
movies.content_rating.fillna(value='Not listed', inplace=True)

# calculate the average star rating for movies 2 hours or longer,
movies[movies.duration > 120].star_rating.mean()  

# and compare that with the average star rating for movies shorter than 2 hours
movies[movies.duration < 120].star_rating.mean()  


# use a visualization to detect whether there is a relationship between duration and star rating
movies.plot(kind='scatter', x='duration', y='star_rating')

# calculate the average duration for each genre
movies.groupby('genre').duration.mean()

'''
ADVANCED LEVEL
'''

# visualize the relationship between content rating and duration
movies.hist(column='duration', by='content_rating', bins=20)
movies.boxplot(column='duration', by='content_rating')

# determine the top rated movie (by star rating) for each genre



# check if there are multiple movies with the same title, and if so, determine if they are actually duplicates


# calculate the average star rating for each genre, but only include genres with at least 10 movies



'''
BONUS
'''

# Figure out something "interesting" using the actors data!
