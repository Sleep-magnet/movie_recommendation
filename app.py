'''
Author: Bappy Ahmed (Modified by ChatGPT)
Email: entbappy73@gmail.com
Date: 2021-Nov-15
'''

import pickle
import streamlit as st
import requests
import time

API_KEY = "8265bd1679663a7ea12ac168da84d2e8"

def fetch_poster(movie_id, retries=3, backoff=1):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            poster_path = data.get('poster_path')
            if poster_path:
                return "https://image.tmdb.org/t/p/w500/" + poster_path
            else:
                return None
        except requests.exceptions.RequestException as e:
            print(f"[Attempt {attempt+1}] Failed to fetch poster: {e}")
            time.sleep(backoff * (attempt + 1))
    return None


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]]['movie_id']
        poster = fetch_poster(movie_id)
        recommended_movie_posters.append(poster)
        recommended_movie_names.append(movies.iloc[i[0]].title)
        time.sleep(0.5)  # Wait 500ms between API calls to avoid rate limits

    return recommended_movie_names, recommended_movie_posters


# Streamlit UI
st.header('Movie Recommender System Using Machine Learning')

movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(recommended_movie_names[idx])
            if recommended_movie_posters[idx]:
                st.image(recommended_movie_posters[idx])
            else:
                st.warning("Poster not available.")
