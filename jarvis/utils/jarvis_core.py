
import webbrowser
import requests
from openai import OpenAI
from utils.musicLibrary import music

def ai_response(command, api_key):
    client = OpenAI(api_key=api_key)
    resp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Jarvis, a helpful assistant. Keep responses short."},
            {"role": "user", "content": command}
        ]
    )
    return resp.choices[0].message.content

def process_command(command, openai_key, news_api_key=None):
    cmd = command.lower()
    if "open google" in cmd:
        return "Opening Google", "https://www.google.com"
    if "open youtube" in cmd:
        return "Opening YouTube", "https://www.youtube.com"
    if "open facebook" in cmd:
        return "Opening Facebook", "https://www.facebook.com"
    if cmd.startswith("play "):
        song = cmd.split(" ",1)[1]
        link = music.get(song)
        return (f"Playing {song}", link) if link else ("Song not found", None)
    if "news" in cmd:
        if not news_api_key:
            return "Please provide News API key!", None
        url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api_key}"
        r = requests.get(url)
        if r.status_code != 200:
            return "Failed to fetch news", None
        articles = r.json().get("articles", [])[:5]
        titles = [a["title"] for a in articles]
        return "Here are top headlines:", titles
    # default → AI
    return ai_response(command, openai_key), None
