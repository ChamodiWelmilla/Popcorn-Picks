import streamlit as st
import pickle
import requests


api_key = "Your API key here"

movies = pickle.load(open("movies_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))
movies_list = movies["title"].values

st.header("Popcorn Pick🍿")

def fetch_trending():
    url = f"https://api.themoviedb.org/3/trending/movie/week?api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    movies = data["results"][:10] 
    titles = [movie["title"] for movie in movies]
    posters = [
        "https://image.tmdb.org/t/p/w500/" + movie["poster_path"] for movie in movies
    ]
    return titles, posters

titles, posters = fetch_trending()
st.text("🔥 Trending Movies")
st.markdown(
    """
    <style>
    .scrolling-wrapper {
        display: flex;
        overflow-x: auto;
        padding: 10px;
    }
    .card {
        flex: 0 0 auto;
        margin-right: 10px;
        text-align: center;
    }
    .card img {
        width: 150px;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

cards_html = '<div class="scrolling-wrapper">'
for title, poster in zip(titles, posters):
    cards_html += f'<div class="card"><img src="{poster}"><p>{title}</p></div>'
cards_html += "</div>"

st.markdown(cards_html, unsafe_allow_html=True)

selected = st.selectbox("Select a movie you like:", movies_list)

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    response = requests.get(url)
    data = response.json() 
    poster_path = data.get("poster_path") 
    return "https://image.tmdb.org/t/p/w500/" + poster_path

def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distance = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1]
    )
    recommendations = []
    poster_paths = []   
    for i in distance[1:6]:
        movie_id =movies.iloc[i[0]].id
        recommendations.append(movies.iloc[i[0]].title)
        poster_paths.append(fetch_poster(movie_id))
    return recommendations, poster_paths

if st.button("Recommend Me Movies"):
    recommendations, poster_paths = recommend(selected)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.image(poster_paths[0], width=220)
        st.text(recommendations[0])
    with col2:
        st.image(poster_paths[1], width=220)        
        st.text(recommendations[1])
    with col3:
        st.image(poster_paths[2], width=220)
        st.text(recommendations[2])
    with col4:
        st.image(poster_paths[3], width=220)        
        st.text(recommendations[3])
    with col5:
        st.image(poster_paths[4], width=220)
        st.text(recommendations[4])
