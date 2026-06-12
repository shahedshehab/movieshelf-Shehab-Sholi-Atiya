import json
from movie_manager import MovieManager
from stats_analyzer import StatsAnalyzer
from visualizer import Visualizer

def main():
    DATA_FILE ="movies.csv"
    REPORT_FILE ="movie_report.json"
    
    mm= MovieManager()
    sa= StatsAnalyzer()
    viz= Visualizer()
    
    # Step 1: Load movies
    print("[1/4]loading movies....")
    movies=mm.load_movies(DATA_FILE)
    print(f" Loaded{len(movies)} movies\n")
    # Step 2: Calculate statistics
    print("[2/4] Calculating statistics.....")
    avg_rating = sa.average_rating(movies)
    top_movies =sa.top_rated(movies,n=5)
    genre_counts =sa.genre_counts(movies)
    watch_summary =sa.watched_summary(movies)
    
    print(f"  Average Rating:{avg_rating}")
    print(f"  Total Movies  :{watch_summary['total']}")
    print(f"  Watched       :{watch_summary['watched']} ({watch_summary['watched_%']}%)")
    print(f"  Unwatched     :{watch_summary['unwatched']}")
    print(f"\n Top 5 Movies:")
    for i, m in enumerate(top_movies,1):
        print(f"    {i}. {m['title']:30s} {m['rating']}")
    #Step 3: Save report 
    print("\n[3/4] Saving report....")
    report ={
        "total_movies": len(movies),
        "average_rating":  avg_rating,
        "watched_summary": watch_summary,
        "genre_counts": genre_counts,
        "top_5_movies": top_movies
    }
    
    with open(REPORT_FILE,"w",encoding="utf-8") as f:
        json.dump(report,f,indent=2)
    print(f"   Report saved: {REPORT_FILE}")
    
    # Step 4: Visualize
    print("[4/4] Displaying charts....")
    viz.rating_histogram(movies)
    viz.genre_pie_chart(genre_counts)
    viz.top_movies_bar(top_movies)
    print("\nDone!")
    
if __name__ =="__main__":
    main()
    
    
    
    
    
    
    