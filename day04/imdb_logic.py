import pandas as pd
import gzip
import requests
import os

IMDB_BASE_URL = "https://datasets.imdbws.com/"
BASICS_FILE = "title.basics.tsv.gz"
RATINGS_FILE = "title.ratings.tsv.gz"


def download_file(filename):
    """Downloads a file from IMDb datasets if missing."""
    if os.path.exists(filename):
        return

    url = IMDB_BASE_URL + filename
    print(f"Downloading {filename}...")
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to download {filename}")

    with open(filename, "wb") as f:
        f.write(response.content)


def load_imdb_data():
    """Downloads and loads IMDb data into merged dataframe."""
    download_file(BASICS_FILE)
    download_file(RATINGS_FILE)

    basics = pd.read_csv(BASICS_FILE, sep="\t", compression="gzip", dtype=str)
    ratings = pd.read_csv(RATINGS_FILE, sep="\t", compression="gzip", dtype=str)

    # Keep only movies
    basics = basics[basics["titleType"] == "movie"]

    # Convert numeric fields
    basics["startYear"] = pd.to_numeric(basics["startYear"], errors="coerce")
    basics["runtimeMinutes"] = pd.to_numeric(basics["runtimeMinutes"], errors="coerce")
    ratings["averageRating"] = pd.to_numeric(ratings["averageRating"], errors="coerce")

    # Merge
    df = basics.merge(ratings, on="tconst", how="inner")

    return df


def filter_movies(df, genre, min_year, max_year, min_rating, max_duration):
    """Returns filtered movie list according to user preferences."""
    result = df.copy()

    if genre != "Any":
        result = result[result["genres"].str.contains(genre, na=False)]

    result = result[
        (result["startYear"] >= min_year) &
        (result["startYear"] <= max_year) &
        (result["averageRating"] >= min_rating) &
        (result["runtimeMinutes"] <= max_duration)
    ]

    # Clean output
    result = result[["primaryTitle", "startYear", "genres", "averageRating", "runtimeMinutes"]]

    # Sort by rating desc
    return result.sort_values(by="averageRating", ascending=False).head(3)
