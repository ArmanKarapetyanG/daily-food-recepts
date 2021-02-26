import requests
import smtplib
import datetime

now = datetime.datetime.now().strftime('%H')

querystring = {"number": "1"}

headers = {
    'x-rapidapi-key': "af97540220msh7ff7ff47eb8b851p1ca53djsnd66b8a103f8e",
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"

if now == 8:
    response = requests.get(url, headers=headers, params=querystring)
    name = response.json()['recipes'][0]['sourceName']
    url = response.json()['recipes'][0]['spoonacularSourceUrl']
    msg = f"Subject: Breakfast time! \n\n" \
          f"{name} - {url}"
elif now == 18:
    response = requests.get(url, headers=headers, params=querystring)
    name = response.json()['recipes'][0]['sourceName']
    url = response.json()['recipes'][0]['spoonacularSourceUrl']
    msg = f"Subject: Lunch time! \n\n" \
          f"{name} - {url}"
elif now == 22:
    response = requests.get(url, headers=headers, params=querystring)
    name = response.json()['recipes'][0]['sourceName']
    url = response.json()['recipes'][0]['spoonacularSourceUrl']
    msg = f"Subject: Dinner time! \n\n" \
          f"{name} - {url}"


def send(msg):
    with smtplib.SMTP('smtp.gmail.com') as l:
        l.starttls()
        l.login(user='sberrusmoscow@gmail.com', password='00ls0002002123')
        l.sendmail(from_addr='sberrusmoscow@gmail.com', to_addrs='arman009.cooll@gmail.com', msg=msg)
try:
    send(msg=msg)
except NameError:
    pass

