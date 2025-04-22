import requests
import random
from bs4 import BeautifulSoup
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Sample proxies list
proxies_list = [
    "http://proxy1:port",
    "http://proxy2:port",
    "http://proxy3:port",
]

def get_random_proxy():
    return {"http": random.choice(proxies_list)}

@api_view(["GET"])
def instagram_profile(request):
    username = request.query_params.get("username")
    if not username:
        return Response({"error": "Username is required"}, status=400)

    url = f"https://www.instagram.com/{username}/"
    try:
        response = requests.get(url, headers={
            "User-Agent": "Mozilla/5.0"
        }, proxies=get_random_proxy(), timeout=10)

        if response.status_code != 200:
            return Response({"error": f"Instagram returned status code {response.status_code}"})

        soup = BeautifulSoup(response.text, "html.parser")
        description = soup.find("meta", property="og:description")

        return Response({"bio": description["content"] if description else "Not found"})

    except Exception as e:
        return Response({"error": str(e)})
