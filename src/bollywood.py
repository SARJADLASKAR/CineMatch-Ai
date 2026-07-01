from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.preprocess import preprocess_bollywood


def build_bollywood_model():
    """
    Build Content-Based Recommendation Model
    """

    print("\nBuilding Bollywood Recommendation Model...\n")

    movies = preprocess_bollywood()

    # Convert text into numerical vectors
    vectorizer = TfidfVectorizer(stop_words="english")

    tfidf_matrix = vectorizer.fit_transform(
        movies["combined_features"]
    )

    similarity = cosine_similarity(tfidf_matrix)

    print("Similarity Matrix Created Successfully")

    return movies, similarity


def recommend_movies(movie_name, movies, similarity, top_n=5):
    """
    Recommend Bollywood movies
    """

    # Search movie (case insensitive)
    matches = movies[
        movies["Name"].str.lower() == movie_name.lower()
    ]

    if matches.empty:
        print("\nMovie not found!")
        return

    movie_index = matches.index[0]

    similarity_scores = list(
        enumerate(similarity[movie_index])
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print("\nRecommended Movies\n")

    count = 0

    for index, score in similarity_scores[1:]:

        print(
            f"{count+1}. {movies.iloc[index]['Name']} "
            f"({movies.iloc[index]['Year']})"
        )

        count += 1

        if count == top_n:
            break


if __name__ == "__main__":

    movies, similarity = build_bollywood_model()

    while True:

        print("\n---------------------------")

        movie = input("Enter Movie Name (or exit): ")

        if movie.lower() == "exit":
            break

        recommend_movies(
            movie,
            movies,
            similarity
        )