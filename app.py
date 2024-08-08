import streamlit as st
import pickle
import pandas as pd
import requests



# Dark theme settings
st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎬",
   
    
)

# Custom CSS for dark theme and styling
st.markdown("""
    <style>
    body {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    .css-18e3th9 {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    .stButton > button {
        background-color: #00BFFF;
        color: #FFFFFF;
        border-radius: 10px;
        border: none;
        padding: 10px;
    }
    .stButton > button:hover {
        background-color: #000066;
    }
    .stSelectbox > div > div > div {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    .stImage {
        border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True) 


def fetch_poster(movie_id):
    api_key = '8265bd1679663a7ea12ac168da84d2e8'
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'poster_path' in data:
            poster_path = data['poster_path']
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        else:
            return "https://via.placeholder.com/500x750.png?text=No+Poster+Available"
    else:
        return "https://via.placeholder.com/500x750.png?text=Error+Fetching+Poster"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
    
    return recommended_movies, recommended_movie_posters

# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit app
st.title('🎥 Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])



st.markdown('---')
st.text('Made by - Chayan Mondal')