import requests, json, os, dotenv

dotenv.load_dotenv()
api_key = os.getenv("NEWSAPI_KEY")

url = ('https://newsapi.org/v2/top-headlines?' 
       'country=us&'
       'category=technology&'
       f'apiKey={api_key}')
response = requests.get(url)

data = response.json()

with open("news.json", "w") as f:
    json.dump(data, f, indent=4)