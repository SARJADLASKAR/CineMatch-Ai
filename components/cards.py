import streamlit as st
from components.poster import get_movie_poster


def movie_card(
    title,
    rating=None,
    year=None,
    genre=None,
    director=None,
    actor1=None,
    actor2=None,
    actor3=None,
    similarity=None
):
    """
    Display a professional movie card with poster and details.
    """

    # Get movie information from OMDb
    info = get_movie_poster(title)

    with st.container(border=True):

        col1, col2 = st.columns([1, 3])

        # ==================================================
        # LEFT SIDE : MOVIE POSTER
        # ==================================================

        with col1:

            if (
                info is not None
                and info.get("poster")
                and info["poster"] != "N/A"
            ):

                try:

                    st.image(
                        info["poster"],
                        width=180
                    )

                except Exception:

                    st.info("🎬 Poster not available")

            else:

                st.info("🎬 Poster not available")

        # ==================================================
        # RIGHT SIDE : MOVIE DETAILS
        # ==================================================

        with col2:

            st.markdown(f"## 🎬 {title}")

            # Rating
            if rating is not None:

                st.write(f"⭐ **Rating:** {rating}")

            elif info and info.get("rating"):

                st.write(f"⭐ **IMDb Rating:** {info['rating']}")

            # Year
            if year is not None:

                st.write(f"📅 **Year:** {year}")

            elif info and info.get("year"):

                st.write(f"📅 **Year:** {info['year']}")

            # Genre
            if genre:

                st.write(f"🎭 **Genre:** {genre}")

            elif info and info.get("genre"):

                st.write(f"🎭 **Genre:** {info['genre']}")

            # Runtime
            if info and info.get("runtime"):

                st.write(f"⏱ **Runtime:** {info['runtime']}")

            # Language
            if info and info.get("language"):

                st.write(f"🌐 **Language:** {info['language']}")

            # Director
            if director:

                st.write(f"🎬 **Director:** {director}")

            # Cast
            cast = []

            if actor1:
                cast.append(actor1)

            if actor2:
                cast.append(actor2)

            if actor3:
                cast.append(actor3)

            if cast:

                st.write("👥 **Cast:**")

                st.write(", ".join(cast))

            # Plot
            if (
                info is not None
                and info.get("plot")
                and info["plot"] != "N/A"
            ):

                st.write("📝 **Plot**")

                st.caption(info["plot"])

            # Recommendation Score
            if similarity is not None:

                similarity = float(similarity)

                percent = round(similarity * 100, 1)

                st.progress(min(similarity, 1.0))

                st.success(
                    f"🎯 Recommendation Score: {percent}%"
                )

    st.markdown("---")