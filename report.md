# 1:project Title & member
# MovieShelf — Personal Movie Watchlist Tracker
**Course:** Python Programming
**Members:**
- Shahed Shehab — 202211666 — Responsible for: movie_manager.py, create_sample_data.py
- Reem Sholi    — 202211538 — Responsible for: stats_analyzer.py, requirements.txt
- Aseel Atiya   — 202212011 — Responsible for: visualizer.py, main.py

**GitHub Repository:** https://github.com/shahedshehab/movieshelf-Shehab-Sholi-Atiya

# 2:project description:
MovieShelf is a Python application designed to manage a personal movie watchlist. The application loads movie data from a CSV file, analyzes the data using Python statistics, and visualizes the results through charts created with Matplotlib. It also generates a JSON report containing useful information about the movie collection. The project demonstrates the use of file handling, object-oriented programming, data analysis, and data visualization in Python.

# 3: Library used
# Library      |     	Version	      |     How it was used
- matplotlib	 |       3.10.9       |       Creating histogram, pie chart, and bar chart
- csv          |     	Built-in	    |      Reading and writing movie data
- json	       |      Built-in	    |      Saving analysis results into JSON report


# 4: Module Descriptions
1- movie_manager.py:
is a class have methods like loading, saving, adding and filtering movies based on watched from csv file.
most important method-->load_movies():read csv file and convert each row into dictionary with updating on data types (like year as int)

2-stats_analyzer.py:
This module contains the StatsAnalyzer class, which performs statistical analysis on movie data. It calculates average ratings, finds top-rated movies,
counts genres, and summarizes watched versus unwatched movies. The most important method is average_rating(), which computes the overall average movie rating.



# 5: Test Cases
2. Test: average_rating()

Input: Ratings = 9.5, 8.0, 7.0
Expected Output: 8.17
Actual Output: 8.17 (exact)
sa = StatsAnalyzer()

movies = [
    {"rating": 9.5},
    {"rating": 8.0},
    {"rating": 7.0}
]
print(sa.average_rating(movies))


3. Test: genre_counts()

Input: Action, Action, Drama, Comedy
Expected Output:
{
    "Action": 2,
    "Drama": 1,
    "Comedy": 1
}
Actual Output: Correct counts returned 
print(sa.genre_counts(movies))


# 5: Screenshots


# 7: Individual Contributions
| Student | ID | Files | Commit Count | GitHub Username |
|---|---|---|---|---|
| Shahed Shehab | 202211666 | movie_manager.py, create_sample_data.py | 5 | @shahedshehab |
| Reem Sholi    | 202211538 | stats_analyzer.py, requirements.txt     | 8 | @reemsholi|
| Aseel Atiya   | 202212011 | visualizer.py, main.py                  | ? | @username |


# 8:  Challenges & What You Learned
Shahed Shehab (202211666): the main challenge was working with dictionaries in general -_- 
solve by restudying dict  but I still feel I need more practice.

Reem Sholi (202211538):
The problem was to calculate statistics for special cases, such as movies that have an empty list. 
The solution is to first test the length of the list and then perform the calculation.

# 9: How to Run
