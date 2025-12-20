from colorama import Fore,Style,init
from textblob import TextBlob
print(Fore.BLUE + "Welcome to Sentiment Spy!")
name = input(Fore.MAGENTA +"Enter your name").strip() or "Friendly Agent"
print(Fore.CYAN + f"Hello Agent {name}! (exit| reset| history)")

history = []
while True:
    text = input(Fore.GREEN + "You:") .strip()
    if not text:
        print(Fore.RED + f"Goodbye Agent {name}!");continue
    cmd = text.lower()
    if cmd =="exit":
        print(Fore.GREEN + f"Goodbye Agent {name}!");break
    if cmd =="reset":
        history.clear();print(Fore.CYAN + "History Cleared!");continue
    if cmd =="history":
        if not history: print(Fore.YELLOW + "No history yet")
        else:
          print(Fore.CYAN + "Conversation history")
          for i,(t,p,s) in enumerate(history,1):
            col = {"Positive":Fore.GREEN,"Negative":Fore.YELLOW}[s]
            print(f"[{i}]{col}{t}({p:.2f},{s})")
        continue
    polarity = TextBlob(text).sentiment.polarity
    sentiment,color = (
    ("Positive",Fore.GREEN) if polarity > 0.05 else
    ("Negative",Fore.RED) if polarity <0.05 else
    ("Neutral",Fore.YELLOW)
    )
    history.append((text,polarity,sentiment))
    print(f"{color}Sentiment : {sentiment}({polarity:.2f})")