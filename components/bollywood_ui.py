import streamlit as st

from components.cards import movie_card
from components.search import search_box


def show_bollywood(movies, similarity):
    """
    Bollywood Movie Recommendation UI
    """

    st.header("🎞️ Bollywood Movie Recommendation")

    st.write(
        "Search for a Bollywood movie and get the Top 5 similar movie recommendations."
    )

    # -------------------------------------
    # Search Box
    # -------------------------------------

    submitted, movie_name = search_box(
        title="Enter Bollywood Movie Name",
        placeholder="Example: 3 Idiots"
    )

    if not submitted:
        return

    movie_name = movie_name.strip()

    if movie_name == "":
        st.warning("Please enter a movie name.")
        return

    # -------------------------------------
    # Partial Search
    # -------------------------------------

    matches = movies[
        movies["Name"].str.lower().str.contains(
            movie_name.lower(),
            na=False
        )
    ]

    if matches.empty:

        st.error("Movie not found!")

        st.info(
            "Try searching:\n\n"
            "- 3 Idiots\n"
            "- PK\n"
            "- Dangal\n"
            "- Sholay"
        )

        return

    selected = matches.iloc[0]

    movie_index = selected.name

    # -------------------------------------
    # Selected Movie
    # -------------------------------------

    st.success("Selected Movie")

    movie_card(

        title=selected["Name"],

        rating=selected["Rating"],

        year=selected["Year"],

        genre=selected["Genre"],

        director=selected["Director"],

        actor1=selected["Actor 1"],

        actor2=selected["Actor 2"],

        actor3=selected["Actor 3"]

    )

    st.divider()

    st.subheader("🎯 Top 5 Recommendations")

    similarity_scores = list(
        enumerate(similarity[movie_index])
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    count = 0

    for index, score in similarity_scores:

        if index == movie_index:
            continue

        movie = movies.iloc[index]

        movie_card(

            title=movie["Name"],

            rating=movie["Rating"],

            year=movie["Year"],

            genre=movie["Genre"],

            director=movie["Director"],

            actor1=movie["Actor 1"],

            actor2=movie["Actor 2"],

            actor3=movie["Actor 3"],

            similarity=score

        )

        count += 1

        if count == 5:
            break