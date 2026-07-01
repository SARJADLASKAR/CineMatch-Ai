from sklearn.metrics.pairwise import cosine_similarity
from src.preprocess import preprocess_hollywood


def build_hollywood_model():
    """
    Builds the Hollywood recommendation model using
    Collaborative Filtering and Cosine Similarity.
    """

    print("\nBuilding Hollywood Recommendation Model...\n")

    # Load processed data
    merged_df, user_movie_matrix = preprocess_hollywood()

    # Transpose matrix
    movie_matrix = user_movie_matrix.T

    # Calculate similarity
    similarity = cosine_similarity(movie_matrix)

    print("Similarity Matrix Created Successfully")

    return movie_matrix, similarity


def recommend_movies(movie_name, movie_matrix, similarity, top_n=5):
    """
    Recommend similar movies.
    """

    # Check movie exists
    if movie_name not in movie_matrix.index:
        print("\nMovie not found!")
        return

    movie_index = movie_matrix.index.get_loc(movie_name)

    similarity_scores = list(enumerate(similarity[movie_index]))

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print("\nRecommended Movies:\n")

    count = 0

    for index, score in similarity_scores[1:]:

        print(f"{count+1}. {movie_matrix.index[index]}")

        count += 1

        if count == top_n:
            break


if __name__ == "__main__":

    movie_matrix, similarity = build_hollywood_model()

    while True:

        print("\n--------------------------------")

        movie = input("Enter Movie Name (or exit): ")

        if movie.lower() == "exit":
            break

        recommend_movies(movie, movie_matrix, similarity)