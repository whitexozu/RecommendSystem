'''
example
    https://stackabuse.com/creating-a-simple-recommender-system-in-python-using-pandas/
corrwith
    https://rfriend.tistory.com/tag/corrwith%28%29
pansas drop na
    http://twinstarinfo.blogspot.com/2018/10/python-pandasdataframedropna.html
'''

import numpy as np 
import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sns.set_style('dark')

def parse_genres(genres_str):
    genres = json.loads(genres_str.replace('\'', '"'))
    
    genres_list = []
    for g in genres:
        genres_list.append(g['name'])

    return '|'.join(genres_list)

def pyplot_graph(data):
    # print( data.groupby('title')['rating'].mean().head() )

    # print( data.groupby('title')['rating'].mean().sort_values(ascending=False).head() )

    # print( data.groupby('title')['rating'].count().sort_values(ascending=False).head() )

    ratings_mean_count = pd.DataFrame(data.groupby('title')['rating'].mean())
    ratings_mean_count['rating_counts'] = pd.DataFrame(data.groupby('title')['rating'].count())
    # print( ratings_mean_count.head() )

    plt.figure(figsize=(8,6))
    plt.rcParams['patch.force_edgecolor'] = True
    ratings_mean_count['rating_counts'].hist(bins=50)
    # plt.show()

    plt.figure(figsize=(8,6))
    plt.rcParams['patch.force_edgecolor'] = True
    ratings_mean_count['rating'].hist(bins=50)
    # plt.show()

    plt.figure(figsize=(8,6))
    plt.rcParams['patch.force_edgecolor'] = True
    sns.jointplot(x='rating', y='rating_counts', data=ratings_mean_count, alpha=0.4)
    # plt.show()
    
if __name__ == "__main__":

    ratings = pd.read_csv('/Users/whitexozu/dev/project/recommend/data/the-movies-dataset/ratings_small.csv')
    ratings.head()

    meta = pd.read_csv('/Users/whitexozu/dev/project/recommend/data/the-movies-dataset/movies_metadata.csv', dtype={'popularity': str})
    # meta.head()

    meta = meta[['id', 'original_title', 'original_language', 'genres']]
    meta = meta.rename(columns={'id':'movieId'})
    meta = meta.rename(columns={'original_title':'title'})
    meta = meta[meta['original_language'] == 'en']

    meta.movieId = pd.to_numeric(meta.movieId, errors='coerce')
    ratings.movieId = pd.to_numeric(ratings.movieId, errors='coerce')

    meta['genres'] = meta['genres'].apply(parse_genres)

    data = pd.merge(ratings, meta, on='movieId', how='inner')

    # print( data.head() )

    ratings_mean_count = pd.DataFrame(data.groupby('title')['rating'].mean())
    ratings_mean_count['rating_counts'] = pd.DataFrame(data.groupby('title')['rating'].count())
    # pyplot_graph(data)

    user_movie_rating = data.pivot_table(index='userId', columns='title', values='rating')
    # print( user_movie_rating.head(20) )

    forrest_gump_ratings = user_movie_rating['Young and Innocent']

    # print( forrest_gump_ratings.head() )

    movies_like_forest_gump = user_movie_rating.corrwith(forrest_gump_ratings)
    # print( movies_like_forest_gump )

    corr_forrest_gump = pd.DataFrame(movies_like_forest_gump, columns=['Correlation'])
    corr_forrest_gump.dropna(inplace=True)
    # corr_forrest_gump.head()

    # corr_forrest_gump.sort_values('Correlation', ascending=False).head(10)

    corr_forrest_gump = corr_forrest_gump.join(ratings_mean_count['rating_counts'])
    # corr_forrest_gump.head()

    print( corr_forrest_gump[corr_forrest_gump ['rating_counts']>50].sort_values('Correlation', ascending=False).head() )