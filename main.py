import requests

apikey="your api key"
url = f"https://newsapi.org/v2/everything?q=apple&from=2023-10-15&to=2023-10-15&sortBy=popularity&apiKey={str(apikey)}"

req = requests.get(url)
res = req.json()
articles = res.get("articles")

#longueur = len(articles) -- 10

with open("data", "w") as TitleUrl:
  for i in articles:
    print("--------------------------------------")
    print(f"Titre : {i.get('title')}")
    print(f"{i.get('url')} ")
    TitleUrl.write("--------------------------------\n")
    TitleUrl.write("Title : "+ str(i.get('title'))+"\n")
    TitleUrl.write("url   : " + str(i.get('url'))+"\n")

#myDico = dict(articles[0])

#print(articles[0]["source"]["id"])
""" for i in articles["url"] :
  print(articles[i]["url"])"""

##print(articles[0])
"""for i , j in enumerate(articles["title"],articles["url"]) :
  print(f"{i} \n  {j}")
  """
"""res = req.json()
print(res)"""

##print(req)
