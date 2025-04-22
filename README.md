# 📸 Instagram Profile Scraper API

This is a simple API built with Django that scrapes public Instagram profile data using a username or user ID, with support for rotating proxies to avoid blocking.

---
## 🚀 How to Install

1. Clone the Repository
git clone https://github.com/yourusername/instagram-scraper-api.git
cd instagram-scraper-api

2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Install Dependencies 
pip install -r requirements.txt

4.Run Migrations
python manage.py migrate

🛠️ How to Run It
Start the development server with:
python manage.py runserver

The API will be available at:
http://127.0.0.1:8000/api/{username_or_user_id}/

📡 API Endpoint

Method	    Endpoint	          Description
GET	     /api/<username>/	    Fetch Instagram profile data
📌 Example Usage
Request:
GET http://127.0.0.1:8000/api/prateek_bhardwajj/

Response:
json
{
  "username": "prateek_bhardwajj",
  "full_name": "Prateek Bhardwaj",
  "followers": 1200,
  "following": 300,
  "posts": 45,
  ...
}
