import csv
class MovieManager():
    def load_movies(self, filepath) -> list:
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                reader= csv.DictReader(f)
                movie_dict=[]
                for row in reader:
                    movie_dict.append(dict(title=row['title'], genre=row['genre'], year=int(row['year']), rating=float(row['rating']), watched=row['watched']))
            return movie_dict
        except FileNotFoundError:
            raise FileNotFoundError(f"{filepath} File not found!!!")
    
    def save_movies(self,movies:list,filepath: str):
        pass
    
    def add_movie(self,movies: list, title: str, genre: str, year: int,rating: float,watched: str)-> list:
        pass
    
    def get_watched(self, movies: list)-> list:
        pass
m=MovieManager()
print(m.load_movies("movies.csv"))