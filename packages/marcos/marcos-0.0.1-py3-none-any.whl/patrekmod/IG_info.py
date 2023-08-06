import requests 

class IG_info:
 
 hd = {
  'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
  'viewport-width':'412',
  'x-asbd-id':'198387',
  'x-ig-app-id':'1217981644879628',
  'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5IG_info.hdMSoxwjz'}
 
 def name(self, user:str) -> str:
  try:
   rer = requests.get(
    url="https://i.instagram.com/api/v1/users/web_profile_info/?username="+user,
    headers=IG_info.hd
   ).json()["data"]["user"]
   return str(rer['full_name'])
  except:
   return str("Error")
 
 def followers(self, user:str)-> str:
  try:
   rer = requests.get(
    url="https://i.instagram.com/api/v1/users/web_profile_info/?username="+user,
    headers=IG_info.hd
   ).json()["data"]["user"]
   return str(rer['edge_followed_by']['count'])
  except:
   return str("Error")
 
 def following(self, user:str) -> str:
  try:
   rer = requests.get(
    url="https://i.instagram.com/api/v1/users/web_profile_info/?username="+user,
    headers=IG_info.hd
   ).json()["data"]["user"]
   return str(rer['edge_follow']['count'])
  except:
   return str("Error")
 
 def private(self, user:str)->str:
  try:
   rer = requests.get(
    url="https://i.instagram.com/api/v1/users/web_profile_info/?username="+user,
    headers=IG_info.hd
   ).json()["data"]["user"]
   return str(rer['is_private'])
  except:
   return str("Error")
 
 def business(self, user:str)->str:
  try:
   rer = requests.get(
    url="https://i.instagram.com/api/v1/users/web_profile_info/?username="+user,
    headers=IG_info.hd
   ).json()["data"]["user"]
   return str(rer['is_business_account'])
  except:
   return str("Error")
 
 def posts(self, user:str)->str:
  try:
   rer = requests.get(
    url="https://i.instagram.com/api/v1/users/web_profile_info/?username="+user,
    headers=IG_info.hd
   ).json()["data"]["user"]
   return str(rer['edge_owner_to_timeline_media']['count'])
  except:
   return str("Error")
 
 def id(self, user:str)->str:
  try:
   rer = requests.get(
    url="https://i.instagram.com/api/v1/users/web_profile_info/?username="+user,
    headers=IG_info.hd
   ).json()["data"]["user"]
   return str(rer['id'])
  except:
   return str("Error")
 
 def date(self, user:str)->str:
  try:
   rer = requests.get(
    url="https://i.instagram.com/api/v1/users/web_profile_info/?username="+user,
    headers=IG_info.hd
   ).json()["data"]["user"]
   date = requests.get(f"https://o7aa.pythonanywhere.com/?id={rer['id']}").json()["date"]
   return str(date)
  except:
   return str("Error")
 
 def bio(self, user:str)->str:
  try:
   rer = requests.get(
    url="https://i.instagram.com/api/v1/users/web_profile_info/?username="+user,
    headers=IG_info.hd
   ).json()["data"]["user"]
   return str(rer['biography'].replace('\n'," "))
  except:
   return str("Error")
 
 def pic(self, user:str)->str:
  try:
   rer = requests.get(
    url="https://i.instagram.com/api/v1/users/web_profile_info/?username="+user,
    headers=IG_info.hd
   ).json()["data"]["user"]
   return str(rer["profile_pic_url_hd"])
  except:
   return str("Error")
 
 def all(self, user:str)->str:
  try:
   rer = requests.get(
    url="https://i.instagram.com/api/v1/users/web_profile_info/?username="+user,
    headers=IG_info.hd
   ).json()["data"]["user"]
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
   return str("Error")