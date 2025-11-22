# IMDb Movie Picker – Day 04 Assignment

This project uses real data from the [IMDb public datasets](https://datasets.imdbws.com/) to create a simple movie recommendation app.

The program:
- Downloads real IMDb data files (`title.basics.tsv.gz` and `title.ratings.tsv.gz`)
- Extracts useful information about movies:
  - Title
  - Genre
  - Year
  - IMDb rating
  - Duration
- Loads and filters this data according to user preferences:
  - Genre  
  - Year range  
  - Minimum rating  
  - Maximum duration
- Displays **three recommended movies** in a simple **Tkinter GUI**.

---

## 🧩 Program Structure
day04/
├── imdb_logic.py # Business logic: downloading, loading, filtering data
├── imdb_gui.py # GUI: user interface with Tkinter
├── README.md # Project documentation
└── .gitignore # Excludes pycache and temporary files

---

## ▶️ How to Run
1. Open a terminal in the `day04` folder.  
2. Run:
   ```bash
   python3 imdb_gui.py
3. Wait a few moments — the program first downloads IMDb data, which can take tens of seconds depending on your internet connection and computer speed.
During this stage, the console will print:
Loading IMDb data...
Loading finished!
4. Once loading is complete, the GUI window will appear.

---

## 🪄 Notes
The first run may take longer because data files are being downloaded.
The next runs will be faster because the files are saved locally.
You can edit the code to add more filters or change the sorting criteria.

---

## AI usage
I used ChatGPT (GPT-4/5) to help generate:
- The structure of the project
- The separation between business logic and UI
- The logic for downloading and filtering IMDb data
- The Tkinter GUI code

---

## ✨ Example Output
Console output:
Loading IMDb data...
Loading finished!

GUI window:
Genre: Action
Min year: 2000
Max year: 2024
Min rating: 7.5
Max duration (min): 150
[Generate]
→ Recommended movies displayed below.