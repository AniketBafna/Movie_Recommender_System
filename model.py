
import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path



def recommend(movie):
    index = movies[movies['title']==movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x:x[1])

    recommended_movies_names = []
    recommended_movies_posters = []
    recommended_movies_rating = []
    recommended_movies_year = []
    recommended_movies_runtime = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        # fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies_names.append(movies.iloc[i[0]].title)
        recommended_movies_rating.append(movies.iloc[i[0]].vote_average)
        recommended_movies_year.append(movies.iloc[i[0]].release_year)
        recommended_movies_runtime.append(movies.iloc[i[0]].runtime)

    return recommended_movies_names, recommended_movies_posters, recommended_movies_year, recommended_movies_runtime,recommended_movies_rating


def model():
    

    st.title('_Movie Recommender System_ :cinema:',)
    movie_list = movies['title'].values
    selected_movie = st.selectbox('Search Movie', movie_list)

    if st.button('Show Recommendation'):
        st.write("Top 5 on list")
        recommended_movie_names,recommended_movie_posters, recommended_movies_year, recommended_movies_runtime, recommended_movies_rating = recommend(selected_movie)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.image(recommended_movie_posters[0])
            st.subheader(recommended_movie_names[0])
            st.write("Release : ",recommended_movies_year[0])
            st.write("Runtime : ", recommended_movies_runtime[0])
            st.write(":star: ", recommended_movies_rating[0])
        with col2:
            st.image(recommended_movie_posters[1])
            st.subheader(recommended_movie_names[1])
            st.write("Release : ",recommended_movies_year[1])
            st.write("Runtime : ", recommended_movies_runtime[1])
            st.write(":star: ",recommended_movies_rating[1])
        with col3:
            st.image(recommended_movie_posters[2])
            st.subheader(recommended_movie_names[2])
            st.write("Release : ",recommended_movies_year[2])
            st.write("Runtime : ", recommended_movies_runtime[2])
            st.write(":star: ", recommended_movies_rating[2])
        with col4:
            st.image(recommended_movie_posters[3])
            st.subheader(recommended_movie_names[3])
            st.write("Release : ",recommended_movies_year[3])
            st.write("Runtime : ", recommended_movies_runtime[3])
            st.write(":star: ", recommended_movies_rating[3])
        with col5:
            st.image(recommended_movie_posters[4])
            st.subheader(recommended_movie_names[4])
            st.write("Release : ",recommended_movies_year[4])
            st.write("Runtime : ", recommended_movies_runtime[4])
            st.write(":star: ",recommended_movies_rating[4])
