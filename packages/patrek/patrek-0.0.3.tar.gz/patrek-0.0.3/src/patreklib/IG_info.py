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
            name=rer['full_name']
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
            private=rer['is_private']
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
            business=rer['is_business_account']
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
            posts=rer['edge_owner_to_timeline_media']['count']
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
            id=rer['id']
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
            id=rer['id']
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
            bioi=rer['biography']
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
            pic=rer["profile_pic_url_hd"]
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
            name=rer['full_name']
            fols=rer['edge_followed_by']['count']
            folg=rer['edge_follow']['count']
            private=rer['is_private']
            bis=rer['is_business_account']
            posts=rer['edge_owner_to_timeline_media']['count']
            id=rer['id']
            date =requests.get(f"https://o7aa.pythonanywhere.com/?id={id}").json()["date"]
            bioi=rer['biography']
            bio=bioi.replace('\n'," ")
            pic=rer["profile_pic_url_hd"]
            return {"full_name":name,"edge_followed_by":{"count":fols},"edge_follow":{"count":folg},"is_private":private,"'is_business_account":bis,"edge_owner_to_timeline_media":{"count":posts},"id":id,"date":date,"biography":bio,"profile_pic_url_hd":pic}
        except:
            return False
name = IG_info.all(user="lcn4")
print(name)