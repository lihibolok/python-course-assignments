import tkinter as tk
print("Loading IMDb data...")
from tkinter import ttk
from imdb_logic import load_imdb_data, filter_movies

df = load_imdb_data()
print("Loading finished!")


GENRES = [
    "Any", "Action", "Adventure", "Animation", "Biography", "Comedy", "Crime", "Drama",
    "Family", "Fantasy", "History", "Horror", "Music", "Romance", "Sci-Fi", "Thriller"
]

def generate_recommendations():
    genre = genre_var.get()
    min_year = int(min_year_var.get())
    max_year = int(max_year_var.get())
    min_rating = float(min_rating_var.get())
    max_duration = int(max_duration_var.get())

    results = filter_movies(df, genre, min_year, max_year, min_rating, max_duration)

    output.delete(1.0, tk.END)

    if results.empty:
        output.insert(tk.END, "No movies found.\n")
    else:
        for _, row in results.iterrows():
            output.insert(
                tk.END,
                f"{row['primaryTitle']} ({row['startYear']})\n"
                f"  Genre: {row['genres']}\n"
                f"  Rating: {row['averageRating']}\n"
                f"  Duration: {row['runtimeMinutes']} min\n\n"
            )

root = tk.Tk()
root.title("IMDb Movie Picker")

# Variables
genre_var = tk.StringVar(value="Any")
min_year_var = tk.StringVar(value="1980")
max_year_var = tk.StringVar(value="2024")
min_rating_var = tk.StringVar(value="7.0")
max_duration_var = tk.StringVar(value="150")

# UI layout
ttk.Label(root, text="Genre:").grid(row=0, column=0, sticky="w")
ttk.OptionMenu(root, genre_var, *GENRES).grid(row=0, column=1)

ttk.Label(root, text="Min year:").grid(row=1, column=0, sticky="w")
ttk.Entry(root, textvariable=min_year_var).grid(row=1, column=1)

ttk.Label(root, text="Max year:").grid(row=2, column=0, sticky="w")
ttk.Entry(root, textvariable=max_year_var).grid(row=2, column=1)

ttk.Label(root, text="Min rating:").grid(row=3, column=0, sticky="w")
ttk.Entry(root, textvariable=min_rating_var).grid(row=3, column=1)

ttk.Label(root, text="Max duration (min):").grid(row=4, column=0, sticky="w")
ttk.Entry(root, textvariable=max_duration_var).grid(row=4, column=1)

ttk.Button(root, text="Generate", command=generate_recommendations).grid(row=5, columnspan=2)

output = tk.Text(root, width=60, height=15)
output.grid(row=6, columnspan=2)

root.mainloop()
