import streamlit as st
import pickle
import os
import pandas as pd
import numpy as np
import requests # its help us to hit any API 

# now next we want to show the 
# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=YOUR_API_KEY&language=en-US'.format(movie_id))
#     data = response.json()
#     return "https://image.tmdb.org/t/p/w500" + data['poster_path']

# creating the recommend funtion
def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    # we do not have similarity matrix so we have to get that again using pickle
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:6]
    
    recommended_movie = []
    recommended_movie_posters = []
    
    for i in movies_list:
        
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie.append(movies.iloc[i[0]].title)
        # fetch poster from API
        # recommended_movie_posters.append(fetch_poster(movie_id))
        
    # return recommended_movie, recommended_movie_posters
    return recommended_movie
# so this fuctionn will return us 5 movies based given input movie

# Download similarity.pkl if not present
# here we are accessing the file online
file_url = "https://drive.google.com/uc?export=download&id=1F8LRUgA_pDdI2Mw34gCofG-2-IuBzQmV"
filename = "similarity.pkl"

if not os.path.exists(filename):
    with open(filename, 'wb') as f:
        response = requests.get(file_url)
        f.write(response.content)

similarity = pickle.load(open(filename, 'rb'))

# for offline file accessing we can use this
# similarity = pickle.load(open('similarity.pkl', 'rb'))

movies = pickle.load(open('movies_data.pkl', 'rb'))
movies_name_list = movies['title'].values
# here it will print the title of every movies
# it will we pass in the option box than there we will have list of movies

movies_name_list = np.insert(movies_name_list, 0, 'Select movie')
# # by default value of option box is first movie name 
# # therefore here we are setting first value as Select movies

st.title('Movie Recommendation System')

# Now next we want a type box where user will type the name of movies
# also it will be look like  a dropdown where user can see all the movies name

selected_movie_name = st.selectbox(
    'Select the name of Movie: ',
    movies_name_list
)
# if we will click on the select box than it will give us list of all movies 
# so select outside somewhere so that list will be not shown any more


# we are putting a button which will give us option to ask recommend movies
if st.button('Recommend') and selected_movie_name != 'Select movie':
    
    # this code is for movie and poster both
    
    # names, posters = recommend(selected_movie_name)
    # # here we will pass selected_movie_name and fucntion will return us 5 movie name and there posters
    
    # col1, col2, col3, col4, col5 = st.columns(5)
    # with col1:
    #     st.text(names[0])
    #     st.image(posters[0])
    
    # with col2:
    #     st.text(names[1])
    #     st.image(posters[1])
    
    # with col3:
    #     st.text(names[2])
    #     st.image(posters[2])
    
    # with col4:
    #     st.text(names[3])
    #     st.image(posters[3])
    
    # with col5:
    #     st.text(names[4])
    #     st.image(posters[4])
    
    # this code is for movies
    
    recommendation = recommend(selected_movie_name)
    # here we will pass selected_movie_name and fucntion will return us 5 movie name
    
    for i in recommendation:
        st.write(i)
    
    