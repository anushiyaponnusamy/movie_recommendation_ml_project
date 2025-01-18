import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    movies_list = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])[1:6]
    recommended_movies=[]
    for i in movies_list:
        movie_id = i[0];
        
        recommended_movies.append(movies.iloc[i[0]].title)
    return  recommended_movies

movies_dict=pickle.load(open('movies_dict.pkkl','rb'))
similarity=pickle.load(open('similarity.pkkl','rb'))
movies=pd.DataFrame(movies_dict)


st.title('Movie Recommender System')
option = st.selectbox(
    "How would you like to be contacted?",
   movies['title'].values
)

if st.button('Recommend'):
    recommendations=recommend(option)
    for i in recommendations:
      st.write(i)