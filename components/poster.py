import re
import requests

API_KEY = "62ff5e92"


def get_movie_poster(movie_name):
    """
    Fetch movie details from OMDb API.
    """

    # -----------------------------------------
    # Extract year from title
    # Example:
    # Toy Story (1995)
    # ->
    # title = Toy Story
    # year = 1995
    # -----------------------------------------

    year = None

    match = re.search(r"\((\d{4})\)", movie_name)

    if match:
        year = match.group(1)

    title = re.sub(r"\(\d{4}\)", "", movie_name).strip()

    # -----------------------------------------

    url = f"https://www.omdbapi.com/?t={title}&apikey={API_KEY}"

    if year:
        url += f"&y={year}"

    try:

        response = requests.get(url, timeout=10)

        data = response.json()

        print(data)          # <-- Keep this temporarily

        if data.get("Response") == "True":

            return {

                "poster": data.get("Poster"),

                "rating": data.get("imdbRating"),

                "year": data.get("Year"),

                "genre": data.get("Genre"),

                "plot": data.get("Plot"),

                "runtime": data.get("Runtime"),

                "language": data.get("Language")

            }

    except Exception as e:

        print(e)

    return None