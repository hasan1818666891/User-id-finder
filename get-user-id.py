import os
import re
import requests
from pyfiglet import print_figlet
from time import sleep

#colours
reset = "\x1b[0m"
green = "\x1b[1;92m"
yellow = "\x1b[1;93m"
black = "\x1b[1;90m"
red = "\x1b[1;91m"
cyan = "\x1b[1;96m"

class user_id_finder:
    def __init__(self):
        os.system("clear")
        self.__ver__ = 1.1
        
    def line(self):
        return f' {reset}{black}%s{reset}'%('~'*50)
        
    def clear(self):
        return os.system('clear')
        
    def logo(self):
        print_figlet('GET-UID','cyberlarge',colors='\x1b[38;5;129')
        print(self.line())
        print(f'\t\t{reset}Made by : \x1b[1;92mgithub.com/hasan1818666891'.expandtabs(2))
        print(f"\t\t{reset}Version : {green}{self.__ver__}".expandtabs(2))
        print(self.line())
        
    def info(self):
        print(f'\n\t{reset}[{green}!{reset}] {yellow}This tool made for getting UID of Facebook and Instagram account. Also you can get post UID using this, but facebook post option is now unavailable. {reset} '.expandtabs(4))
        
    def main(self):
        self.logo()
        print(f'\n\t{reset}{yellow}[{green}1{yellow}] Facebook\n\t{reset}{yellow}[{green}2{yellow}] Instagram\n\t{reset}{yellow}[{red}0{yellow}] Exit{reset}'.expandtabs(4))
        print(f'\n\t{reset}[{green}?{reset}] {cyan}Type "{green}info{cyan}" for information.{reset} '.expandtabs(4))
        select = input(f'\n\t{reset}[{green}>_{reset}] {cyan}Choose :{green} '.expandtabs(4))
        if select in ['1','01']:
            self.facebook()
        elif select in ['2','02']:
            self.instagram()
        elif select == "info":
            self.info()
        else:
            self.clear()
            self.main()
            
    def facebook(self):
        print(f'\n\t{reset}{yellow}[{green}1{yellow}] Get user id\n\t{reset}{yellow}[{green}2{yellow}] Get Post id\n\t{reset}{black}[{red}0{black}] Back{reset}'.expandtabs(4))
        select = input(f'\n\t{reset}[{green}>_{reset}]{cyan} Choose :{green} '.expandtabs(4))
        if select in ['01','1']:
            self.fb_user_id()
        elif select in ['02','2']:
            self.fb_post_id()
        elif select in ['0']:
            self.clear()
            self.main()
        else:
            self.clear()
            self.main()
            
    def instagram(self):
        print(f'\n\t{reset}{yellow}[{green}1{yellow}] Get user id\n\t{reset}{yellow}[{green}2{yellow}] Get Post id\n\t{reset}{black}[{red}0{black}] Back{reset}'.expandtabs(4))
        select = input(f'\n\t{reset}[{green}>_{reset}]{cyan} Choose :{green} '.expandtabs(4))
        if select in ['01','1']:
            self.ig_user_id()
        elif select in ['02','2']:
            self.ig_post_id()
        elif select in ['0']:
            self.clear()
            self.main()
        else:
            self.clear()
            self.main()
            
    def ig_user_id(self):
        print(f'\n\t{reset}{cyan}[{green}INFO{cyan}] Use Comma "," for many link'.expandtabs(4))
        links=input(f'\n\t{reset}[{green}>_{reset}] {cyan}Instagram id Link or username:{green} '.expandtabs(4))
        for link in links.split(','):
            link = link.replace(' ','')
            if "https://" not in link:
                link = f"https://www.instagram.com/{link}"
            try:
                req = requests.get(link).text
                userid = re.search('"user_id":"(.*?)",',str(req)).group(1)
                username=re.search('{"username":"(.*?)"}',str(req)).group(1)
                print(f'\n\t{reset}id        :  {green}{userid}{green}\n\t{reset}{green}{reset}username  :  {green}{username}{reset}')
                sleep(5)
            except requests.exceptions.ConnectionError:
                print(f"\n\t{reset}{red}[⚠️] {yellow} Network Connection Error. ".expandtabs(4))
            except AttributeError:
                print(f"\n\t{reset}[⚠️]  {green}{link}{yellow} User not found.".expandtabs(4))
            except Exception as e:
                print(e)
        print(self.line())
        input(f"\n\t{reset}[{black} ENTER for back {reset}]".expandtabs(4))
        self.clear()
        self.main()
        
    def ig_post_id(self):
        print(f'\n\t{reset}{cyan}[{green}INFO{cyan}] Use Comma "," for many link'.expandtabs(4))
        links=input(f'\n\t{reset}[{green}>_{reset}] {cyan}Instagram post/reels link: {green}'.expandtabs(4))
        for link in links.split(','):
            link = link.replace(' ','')
            try:
                req = requests.get(link).text
                media_id = re.search('"media_id":"(.*?)","',str(req)).group(1)
                print(f'\n\t{reset}post id  :  {green}{media_id}{reset}')
                sleep(5)
            except requests.exceptions.ConnectionError:
                print(f"\n\t{reset}{red}[⚠️] {yellow} Network Connection Error. ".expandtabs(4))
            except AttributeError:
                print(f"\n\t{reset}[⚠️]  {green}{link}{yellow} Post not found. Maybe account is private".expandtabs(4))
            except Exception as e:
                print(e)
        print(self.line())
        input(f"\n\t{reset}[{black} ENTER for back {reset}]".expandtabs(4))
        self.clear()
        self.main()
        
    def fb_user_id(self):
        print(f'\n\t{reset}{cyan}[{green}INFO{cyan}] Use Comma "," for many link'.expandtabs(4))
        links=input(f'\n\t{reset}[{green}>_{reset}] {cyan}Facebook id Link :{green} '.expandtabs(4))
        for link in links.split(','):
            link = link.replace(' ','')
            try:
                req = requests.get(link).text
                uid = re.search('"userID":"(.*?)",',str(req)).group(1)
                username = re.search('"userVanity":"(.*?)",',str(req)).group(1)
                name = re.search('"title":"(.*?)"',str(req)).group(1)
                print(f'\n\t{reset}id        :  {green}{uid}{green}\n\t{green}{reset}name      :  {green}{name}\n\t{reset}username  :  {green}{username}{reset}')
                sleep(5)
            except requests.exceptions.ConnectionError:
                print(f"\n\t{reset}{red}[⚠️] {yellow} Network Connection Error. ".expandtabs(4))
            except AttributeError:
                print(f"\n\t{reset}[⚠️]  {green}{link}{yellow} User not found, account redirected to login page.".expandtabs(4))
            except Exception as e:
                print(e)
        print(self.line())
        input(f"\n\t{reset}[{black} ENTER for back {reset}]".expandtabs(4))
        self.clear()
        self.main()
    def fb_post_id(self):
        print(f"\n\t{reset}[⚠️]  {yellow} Currently this option not available.".expandtabs(4))
        print(self.line())
        input(f"\n\t{reset}[{black} ENTER for back {reset}]".expandtabs(4))
        self.clear()
        self.main()
        
if __name__ == "__main__":
     run = user_id_finder()
     run.main()