import streamlit as st


def search_box(
    title="Search Movie",
    placeholder="Enter movie name..."
):
    """
    Reusable search box with Enter key support.

    Returns:
        submitted (bool)
        movie_name (str)
    """

    with st.form(
        key=f"{title}_form",
        clear_on_submit=False
    ):

        movie_name = st.text_input(
            label=title,
            placeholder=placeholder
        )

        submitted = st.form_submit_button(
            "🎬 Recommend"
        )

    return submitted, movie_name