import requests


banner = '''

                            \033[32;1m_______ _______  _____  _     _ _______ _____ __   _\033[0m
                            \033[31;1m|_____| |       |   __| |     | |______   |   | \  |\033[0m
                            \033[32;1m|     | |_____  |____\| |_____| |       __|__ |  \_|\033[0m
                                                                                
                                \033[33;1mAqacquisition Domain Finder\033[0m   \033[34;1m-Author: [0xAgun]\033[0m
                            

'''

print(banner)
list_input = input("\033[36;1menter the company named list:\033[0m ")
print("\033[35mGeting Site from your list\033[0m")
mainurl = "https://crt.sh/?q="
with open(list_input, 'r') as listd:
    for word in listd.readlines():
        req = requests.get(mainurl+word.strip()+'&output=json')
        js = req.json()

        for url in js:
            j = url['common_name']
            save = open("urls.txt","a")
            save.write(str(j).replace("*", "")+"\n")
            save.close()
            print("\033[31mDone grabbing check urls.txt\033[0m")




