import pandas as pd
from src.data_loader import load_hollywood, load_bollywood


# ------------------------------------
# Hollywood Preprocessing
# ------------------------------------
def preprocess_hollywood():
    """
    Loads and preprocesses the Hollywood MovieLens dataset.
    Returns:
        merged_df
        user_movie_matrix
    """

    movies, ratings = load_hollywood()

    # Merge ratings with movie names
    merged_df = pd.merge(ratings, movies, on="movieId")

    print("\nHollywood Dataset Merged Successfully")
    print(f"Rows : {merged_df.shape[0]}")

    # Create User-Movie Matrix
    user_movie_matrix = merged_df.pivot_table(
        index="userId",
        columns="title",
        values="rating"
    )

    # Fill missing values with 0
    user_movie_matrix = user_movie_matrix.fillna(0)

    print("\nUser-Movie Matrix Created")
    print(f"Shape : {user_movie_matrix.shape}")

    return merged_df, user_movie_matrix


# ------------------------------------
# Bollywood Preprocessing
# ------------------------------------
def preprocess_bollywood():
    """
    Cleans the Bollywood dataset and creates a combined feature
    used later for recommendations.
    """

    bollywood = load_bollywood()

    # Fill missing values
    bollywood = bollywood.fillna("")

    # Combine important columns
    bollywood["combined_features"] = (
        bollywood["Genre"].astype(str) + " " +
        bollywood["Director"].astype(str) + " " +
        bollywood["Actor 1"].astype(str) + " " +
        bollywood["Actor 2"].astype(str) + " " +
        bollywood["Actor 3"].astype(str)
    )

    print("\nBollywood Dataset Cleaned Successfully")
    print(f"Movies : {bollywood.shape[0]}")

    return bollywood


# ------------------------------------
# Test
# ------------------------------------
if __name__ == "__main__":

    hollywood_df, matrix = preprocess_hollywood()

    bollywood_df = preprocess_bollywood()

    print("\nHollywood Data")
    print(hollywood_df.head())

    print("\nUser-Movie Matrix")
    print(matrix.head())

    print("\nBollywood Data")
    print(bollywood_df[["Name", "combined_features"]].head())
    