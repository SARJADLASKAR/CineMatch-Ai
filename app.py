import streamlit as st
import joblib

from components.sidebar import sidebar
from components.hollywood_ui import show_hollywood
from components.bollywood_ui import show_bollywood


st.set_page_config(

    page_title="CineMatch-Ai",

    page_icon="🎬",

    layout="wide"

)

# Load CSS
with open("assets/style.css") as f:

    st.markdown(

        f"<style>{f.read()}</style>",

        unsafe_allow_html=True

    )

# Load Models
movie_matrix = joblib.load(
    "models/movie_matrix.pkl"
)

hollywood_similarity = joblib.load(
    "models/hollywood_similarity.pkl"
)

bollywood_movies = joblib.load(
    "models/bollywood_movies.pkl"
)

bollywood_similarity = joblib.load(
    "models/bollywood_similarity.pkl"
)

st.title("🎬 CineMatch-Ai")

choice = sidebar()

if choice == "Hollywood":

    show_hollywood(

        movie_matrix,

        hollywood_similarity

    )

else:

    show_bollywood(

        bollywood_movies,

        bollywood_similarity

    )