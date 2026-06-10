import matplotlib.pyplot as plt
 
class Visualizer:
    def rating_histogram(self,movies:list):
        ratings=[m["rating"]for m in movies]
        fig,ax=plt.subplots(figsize=(8,5))
        ax.hist(ratings,bins=10,range=(0,10),color="steelblue",edgecolor="black")
        avg=sum(ratings)/len(ratings)
        ax.axvline(avg,color="red",linestyle="--",label=f"Average:{avg:.1f}")
        ax.legend()
        ax.set_xlim(0,10)
        ax.set_title("Movie Rating Distribution")
        ax.set_xlabel("Rating")
        ax.set_ylabel("Number of Movies")
        plt.tight_layout()
        plt.show()
    
    def genre_pie_chart(self,genre_counts:dict):
        labels=list(genre_counts.keys())
        sizes=list(genre_counts.values())
        fig,ax=plt.subplots(figsize=(7,7))
        ax.pie(sizes,labels=labels,autopct="%1.1f%%",startangle=140)
        ax.set_title("Movies by Genre")
        plt.show()

    
    
    
        
     
    
        
        
    