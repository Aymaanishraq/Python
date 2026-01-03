import pandas as pd, sys
from textblob import TextBlob
from colorama import Fore,init
init(autoreset=True)

try:
    df = pd.read_csv('imdb_top_1000.CSV')
except FileNotFoundError:
    print(Fore.RED +"File not found");sys.exit()
genres = sorted({g.strip() for x in df['Genre'].dropna() for g in x.split(',')})

def recommend(genre=None , mood=None, rating=0,top=5):
    data= df.copy()
    if genre:data = data[data['Genre'].str.contains(genre,case=False,na=False)]
    if rating : data=data[data['IMDB_Rating']>= rating]
    recs = [(r['Series_Title'], TextBlob(r['Overview']).sentiment.polarity)

       for _, r in data.sample(frac=1).iterrows()

       if not mood or TextBlob(mood).sentiment.polarity * TextBlob(r['Overview']).sentiment.polarity >= 0]
    return recs[:top] or [("No match found",0)]
print(Fore.BLUE + "AI Movie Recommender")
name = input(Fore.YELLOW + "Your name")
print(Fore.GREEN + f"Hi {name}! Available Genres:\n"+ ','.join(genres))
while True:
    g =input(Fore.YELLOW + "Pick genre (Enter to skip):")or None
    mood= input("Your mood:")
    r = input("Min rating (0-10)")
    r= float(r) if r.replace('.','',1).isdigit() else 0
    print(Fore.CYAN+ f"\n Recommendations for {name}:")
    for t,p in recommend(g,mood,r):
        print(f"- {t} ({'😊' if p>0 else '😐' if p==0 else '😢'})")
    if input(Fore.YELLOW+"\nAnother? (y/n):").lower() !='y':
        print(Fore.GREEN+f"Enjoy your movies,{name}!")
        break
