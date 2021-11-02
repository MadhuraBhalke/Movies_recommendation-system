import streamlit as st
import pandas as pd


import pickle 

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])[1:6]
    for i in distances[1:6]:
        print(movies.iloc[i[0]].title)

    recommended_movies = []
    for i in distances:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

similarity = pickle.load(open('similarity.pkl' , 'rb'))


movie_dict = pickle.load(open('movie_dict.pkl' , 'rb'))
movies = pd.DataFrame(movie_dict)

st.title('Movies Recommender System')

options = st.selectbox('What would you like to see today ?', movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(options)
    for i in recommendations:
        st.write(i)