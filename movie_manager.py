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
    
    def save_movies(self,movies:list,filepath: str) -> None:
            with open(filepath, 'w', newline="", encoding='utf-8')as f:
                writer=csv.DictWriter(f,fieldnames=['title','genre','year','rating','watched'])
                writer.writeheader()
                writer.writerows(movies)
            print(f"movies is saved to {filepath}") 
    
    def add_movie(self,movies: list, title: str, genre: str, year: int,rating: float,watched: str)-> list:
        if rating<0.0 or rating>10.0:
            raise ValueError("rating must be between 0.0-10.0")
        if watched != "yes" and watched != "no":
            raise ValueError("watched must be yes or no")
        movie={'title':title,'genre':genre,"year":year,'rating':rating,'watched':watched}
        movies.append(movie)
        return movies
    
    def get_watched(self, movies: list)-> list:
        return [m for m in movies if m["watched"]=="yes"]

#just for pre testing
# m=MovieManager()
# print(m.load_movies("movies.csv"))
# m.save_movies([{'title':"The Running Man",'genre':'action','year':2025,'rating':6.4,'watched':"no"}],"movies.csv")