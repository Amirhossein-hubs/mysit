import requests
import pyttsx3
import json

Api= requests.get("https://api.diadata.org/v1/assetQuotation/Bitcoin/0x0000000000000000000000000000000000000000")
data= json.loads(Api.text)
print(Api.text)
print(Api.status_code)
print(data['Time'])
btc_Price= data['Price']

btc_Price= int(str(btc_Price).replace('.',''))
btc_Price= f"bitcoin price {btc_Price}"
print(btc_Price)

engine= pyttsx3.init()
engine.say(btc_Price)
engine.runAndWait()

#تمرین:یه کد که اگر قیمت از یه حدی بالابره به ما با صدا اطلاعات بده اگر از یه حدی پایین بره خبربده و داخل یه کلاس ایجادش کنم