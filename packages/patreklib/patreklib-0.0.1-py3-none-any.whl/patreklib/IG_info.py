import requests  , json
from user_agent import *

class IG_info:
    def name(user:str) -> str:
        try:
            hd = {
 'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
 'viewport-width':'412',
 'x-asbd-id':'198387',
 'x-ig-app-id':'1217981644879628',
 'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'
    }
            rer = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username="+user,headers=hd).json()["data"]["user"]
            name=rer["full_name"]
            return str(name)
        except:
            return False
    def followers(user:str)-> str:
        try:
            hd = {
 'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
 'viewport-width':'412',
 'x-asbd-id':'198387',
 'x-ig-app-id':'1217981644879628',
 'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'
    }
            rer = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username="+user,headers=hd).json()["data"]["user"]
            followers=rer['edge_followed_by']['count']
            return str(followers)
        except:
            return False
    def following(user:str) -> str:
        try:
            hd = {
 'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
 'viewport-width':'412',
 'x-asbd-id':'198387',
 'x-ig-app-id':'1217981644879628',
 'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'
    }
            rer = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username="+user,headers=hd).json()["data"]["user"]
            following=rer['edge_follow']['count']
            return str(following)
        except:
            return False
    def private(user:str)->str:
        try:
            hd = {
 'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
 'viewport-width':'412',
 'x-asbd-id':'198387',
 'x-ig-app-id':'1217981644879628',
 'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'
    }
            rer = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username="+user,headers=hd).json()["data"]["user"]
            private=self.rer['is_private']
            return str(private)
        except:
            return False
    def business(user:str)->str:
        try:
            hd = {
 'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
 'viewport-width':'412',
 'x-asbd-id':'198387',
 'x-ig-app-id':'1217981644879628',
 'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'
    }
            rer = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username="+user,headers=hd).json()["data"]["user"]
            business=self.rer['is_business_account']
            return str(business)
        except:
            return False
    def posts(user:str)->str:
        try:
            hd = {
 'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
 'viewport-width':'412',
 'x-asbd-id':'198387',
 'x-ig-app-id':'1217981644879628',
 'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'
    }
            rer = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username="+user,headers=hd).json()["data"]["user"]
            posts=self.rer['edge_owner_to_timeline_media']['count']
            return str(posts)
        except:
            return False
    def id(user:str)->str:
        try:
            hd = {
 'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
 'viewport-width':'412',
 'x-asbd-id':'198387',
 'x-ig-app-id':'1217981644879628',
 'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'
    }
            rer = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username="+user,headers=hd).json()["data"]["user"]
            id=self.rer['id']
            return str(id)
        except:
            return False
    def date(user:str)->str:
        try:
            hd = {
 'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
 'viewport-width':'412',
 'x-asbd-id':'198387',
 'x-ig-app-id':'1217981644879628',
 'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'
    }
            rer = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username="+user,headers=hd).json()["data"]["user"]
            id=self.rer['id']
            date = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}").json()["date"]
            return str(date)
        except:
            False
    def bio(user:str)->str:
        try:
            hd = {
 'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
 'viewport-width':'412',
 'x-asbd-id':'198387',
 'x-ig-app-id':'1217981644879628',
 'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'
    }
            rer = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username="+user,headers=hd).json()["data"]["user"]
            bioi=self.rer['biography']
            bio=bioi.replace('\n'," ")
            return str(bio)
        except:
            return False
    def pic(user:str)->str:
        try:
            hd = {
 'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
 'viewport-width':'412',
 'x-asbd-id':'198387',
 'x-ig-app-id':'1217981644879628',
 'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'
    }
            rer = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username="+user,headers=hd).json()["data"]["user"]
            pic=self.rer["profile_pic_url_hd"]
            return str(pic)
        except:
            return False
    def all(user:str)->str:
        try:
            hd = {
 'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
 'viewport-width':'412',
 'x-asbd-id':'198387',
 'x-ig-app-id':'1217981644879628',
 'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'
    }
            rer = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username="+user,headers=hd).json()["data"]["user"]
            name=f"name:"+rer['full_name']
            fols=f"followers:{rer['edge_followed_by']['count']}"
            folg=f"following:{rer['edge_follow']['count']}"
            private=f"private:{rer['is_private']}"
            bis=f"business:{rer['is_business_account']}"
            posts=f"posts:{rer['edge_owner_to_timeline_media']['count']}"
            id=f"id:{rer['id']}"
            date = f'date:{requests.get(f"https://o7aa.pythonanywhere.com/?id={id}").json()["date"]}'
            bioi=rer['biography']
            bio=f"bio:"+bioi.replace('\n'," ")
            pic=f"pic:"+rer["profile_pic_url_hd"]
            return name,fols,folg,private,bis,posts,id,date,bio,pic
        except:
            return False