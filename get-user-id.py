
import requests,re,os
from pyfiglet import print_figlet
from pyfiglet import parse_color


class user_id_finder:
    def __init__(self):
        
        self.menu()
    def logo(self):
        print('\x1b[38;5;129m')
        print_figlet('GET-UID','cyberlarge')
        print('\t\x1b[0mMade by : \x1b[1;92mgithub.com/hasan1818666891')
        print('      \x1b[0m%s'%('-'*40))
    def menu(self):
        self.logo()
        print('''
    1. Facebook
    2. Instagram
    0. Exit
        ''')
        c = input('Choose : ')
        if c in ['1','01']:
            print('''
    1. Get user id
    0. Back
            ''')
            cc = input('Choose : ')
            if cc in ['01','1']:self.fb_user_id()
            elif cc in ['02','2']:self.fb_post_id()
            elif cc in ['0']:self.clear();self.menu()
            else:self.clear();self.menu()
        elif c in ['2','02']:
            print('''
    1. Get userid
    2. Get post id
    0. Back
            ''')
            cc = input('Choose : ')
            if cc in ['01','1']:self.ig_user_id()
            elif cc in ['02','2']:self.ig_post_id()
            elif cc in ['0']:self.clear();self.menu()
            else:self.clear();self.menu()
    def clear(self):
        return os.system('clear')
        
    def ig_user_id(self):
        link=input('\n    Instagram id Link : ')
        req = requests.get(link).text
        userid = re.search('"user_id":"(.*?)",',str(req)).group(1)
        username=re.search('{"username":"(.*?)"}',str(req)).group(1)
        print('''
    id        :  {}
    username  :  {}
    '''.format(userid,username))
    def ig_post_id(self):
        link=input('\n    Instagram post Link : ')
        req = requests.get(link).text
        media_id = re.search('"media_id":"(.*?)","',str(req)).group(1)
        print('\n    instagram post id : {media_id}'.format(media_id=media_id))
    def fb_user_id(self):
        link=input('\n    Facebook id Link : ')
        req = requests.get(link).text
        id = re.search('"userID":"(.*?)",',str(req)).group(1)
        username = re.search('"userVanity":"(.*?)",',str(req)).group(1)
        name = re.search('"title":"(.*?)"',str(req)).group(1)
        print('''
    id        :  {100095451701470&mibextid=ZbWKwL}
    name      :  {ພອນ}
    username  :  {ໄທຜູ້ນ້ອຍ}
    '''.format(id,name,username))
    def fb_post_id(self):
        pass
 
user_id_finder(100095451701470&mibextid=ZbWKwL)
