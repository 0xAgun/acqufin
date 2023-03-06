import requests
import sys
from rich.console import Console
from rich.table import Table
from rich.progress import track

banner = '''

                \033[32;1m_______ _______  _____  _     _ _______ _____ __   _\033[0m
                \033[31;1m|_____| |       |   __| |     | |______   |   | \  |\033[0m
                \033[32;1m|     | |_____  |____\| |_____| |       __|__ |  \_|\033[0m
                                                                    
                    \033[33;1mAqacquisition Domain Finder\033[0m   \033[34;1m-Author: [0xAgun]\033[0m
                

'''

print(banner)

table = Table(title="Enumerating domain for "+sys.argv[1])

table.add_column("Type", justify="right", style="cyan", no_wrap=False)
table.add_column("Urls", style="magenta", justify="center")
# table.add_column("Box Office", justify="right", style="green")






mainurl = "https://crt.sh/?q="
domain = sys.argv[1]
req = requests.get(mainurl+domain+'&output=json')
js = req.json()

for url in js:
    j = url['common_name']
    save = open("urls.txt","a")
    save.write(str(j)+"\n")
    save.close()
    table.add_row("domain", j)



console = Console()
console.print(table)


print("\033[31mDone grabbing check urls.txt\033[0m")