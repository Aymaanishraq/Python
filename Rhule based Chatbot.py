import re,random
from colorama import Fore,init;init(autoreset=True)

dest={"beaches":["Bali","Maldives","Phuket"],
      "mountains":["Swiss Alps","Rocky Mountains","Himalayas"],
      "cities":["Tokyo","Paris","New York"]}


n=lambda t:re.sub(r"\s+"," ",t.strip().lower())
rec=lambda: (lambda p:n(input(f"{Fore.CYAN}Beaches/mountains/cities?\n{Fore.YELLOW}You: "))) (0) if False else None
def rec():
    p=n(input(f"{Fore.CYAN}Beaches/mountains/cities?\n{Fore.YELLOW}You: "))
    if p not in dest:return print(Fore.RED+"No such option")
    while True:
        s=random.choice(dest[p]);print(Fore.GREEN+"How about "+s+"?")
        a=input(f"{Fore.YELLOW}You (yes/no): ").lower()
        if a=="yes":return print(Fore.GREEN+"Enjoy "+s+"!")
        if a!="no":return
help=lambda:print(f"""{Fore.MAGENTA}\nI can:\n{Fore.GREEN}- recommend\n- help\n- exit\n""")

def chat():
    print(Fore.CYAN+"Hello! I’m TravelBot.")
    name=input(Fore.YELLOW+"Your name? ");print(Fore.GREEN+"Nice to meet you,",name);help()
    cmd={"recommend":rec,"suggest":rec,"help":help}
    while True:
        u=n(input(Fore.YELLOW+name+": "))
        if any(x in u for x in["exit","bye"]):return print(Fore.CYAN+"Safe travels, goodbye!")
        [f() for k,f in cmd.items() if k in u] or print(Fore.RED+"Could you rephrase?")

if __name__=="__main__":chat()