import streamlit as st


def sidebar():

    with st.sidebar:

        st.markdown(
            """
            # 🎬 Movie
            ## Recommendation
            """
        )

        st.markdown("---")

        choice = st.radio(
            "Choose Category",
            [
                "Hollywood",
                "Bollywood"
            ]
        )

        st.markdown("---")

        

       

        return choice