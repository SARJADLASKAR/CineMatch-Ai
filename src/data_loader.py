import pandas as pd
import os


# -----------------------------
# Dataset Paths
# -----------------------------
HOLLYWOOD_MOVIES = "dataset/hollywood/movies.csv"
HOLLYWOOD_RATINGS = "dataset/hollywood/ratings.csv"
BOLLYWOOD_MOVIES = "dataset/bollywood/movies_data.csv"


# -----------------------------
# Load Hollywood Dataset
# -----------------------------
def load_hollywood():
    """
    Loads MovieLens movies and ratings datasets.
    Returns:
        movies_df
        ratings_df
    """

    movies = pd.read_csv(HOLLYWOOD_MOVIES)
    ratings = pd.read_csv(HOLLYWOOD_RATINGS)

    print("Hollywood Movies Loaded Successfully")
    print(f"Movies : {movies.shape[0]}")
    print(f"Ratings: {ratings.shape[0]}")

    return movies, ratings


# -----------------------------
# Load Bollywood Dataset
# -----------------------------
def load_bollywood():
    """
    Loads Bollywood movie dataset.
    Returns:
        bollywood_df
    """

    bollywood = pd.read_csv(BOLLYWOOD_MOVIES)

    print("Bollywood Dataset Loaded Successfully")
    print(f"Movies : {bollywood.shape[0]}")

    return bollywood


# -----------------------------
# Test
# -----------------------------
if __name__ == "__main__":

    hollywood_movies, hollywood_ratings = load_hollywood()

    bollywood_movies = load_bollywood()

    print("\nHollywood Movies")
    print(hollywood_movies.head())

    print("\nHollywood Ratings")
    print(hollywood_ratings.head())

    print("\nBollywood Movies")
    print(bollywood_movies.head())