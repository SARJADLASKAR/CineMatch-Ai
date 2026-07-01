import streamlit as st

from components.cards import movie_card
from components.search import search_box


def show_hollywood(movie_matrix, similarity):
    """
    Hollywood Movie Recommendation UI
    """

    st.header("🎥 Hollywood Movie Recommendation")

    st.write(
        "Search for a Hollywood movie and get the Top 5 similar movie recommendations."
    )

    # ----------------------------------------
    # Search Box
    # ----------------------------------------

    submitted, movie_name = search_box(
        title="Enter Hollywood Movie Name",
        placeholder="Example: Toy Story"
    )

    if not submitted:
        return

    # ----------------------------------------
    # Empty Search
    # ----------------------------------------

    movie_name = movie_name.strip()

    if movie_name == "":
        st.warning("Please enter a movie name.")
        return

    # ----------------------------------------
    # Partial Search
    # ----------------------------------------

    matches = []

    for movie in movie_matrix.index:

        if movie_name.lower() in movie.lower():

            matches.append(movie)

    if len(matches) == 0:

        st.error("Movie not found!")

        st.info(
            "Try searching like:\n\n"
            "- Toy Story\n"
            "- Titanic\n"
            "- Heat\n"
            "- Matrix"
        )

        return

    # ----------------------------------------
    # Selected Movie
    # ----------------------------------------

    selected_movie = matches[0]

    st.success("Selected Movie")

    movie_card(
        title=selected_movie
    )

    st.divider()

    st.subheader("🎯 Top 5 Recommendations")

    movie_index = movie_matrix.index.get_loc(
        selected_movie
    )

    similarity_scores = list(
        enumerate(
            similarity[movie_index]
        )
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    count = 0

    for index, score in similarity_scores:

        movie = movie_matrix.index[index]

        if movie == selected_movie:
            continue

        movie_card(
            title=movie,
            similarity=score
        )

        count += 1

        if count == 5:
            break