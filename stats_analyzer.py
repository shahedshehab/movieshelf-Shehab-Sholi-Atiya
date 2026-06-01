
#prepared by :Reem Sholi

class StatsAnalyzer:
 # 1.define average_rating method to calculates the average rating of all movies
    def average_rating(self, movies):
      if not movies:
        return 0.0

      ratings = [m["rating"] for m in movies]
      return round(sum(ratings) / len(ratings), 2)
        
# 2.define top_rated method for return The highest-rated movies.
    
    def top_rated(self, movies, n=5):
      sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True  )
      return sorted_movies[:n]

# 3.define genre_counts method to count the number of movies in each genre.
    
    def genre_counts(self, movies):
      counts = {}

      for movie in movies:
        genre = movie["genre"]
        if genre in counts:
            counts[genre] += 1
        else:
            counts[genre] = 1

      return counts
        
# 4. define watched_summery method to clarifies numbers of movies ,watched and unwatched movies
    
    def watched_summary(self, movies):
        if not movies:
          return {
            "total": 0,
            "watched": 0,
            "unwatched": 0,
            "watched_%": 0.0
        }
        watched = sum(1 for m in movies if m["watched"] == "yes")
        unwatched = len(movies) - watched

        return {
         "total": len(movies),
         "watched": watched,
         "unwatched": unwatched,
         "watched_%": round(watched / len(movies) * 100, 1 )
        }
    

