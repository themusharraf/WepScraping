import requests
from bs4 import BeautifulSoup

URL = "https://uzxit.net/uzbek-mp3"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# job_elements = soup.find_all("div", class_="cols fx-row")
job = soup.find_all("div", class_="track-item fx-row fx-middle js-item js-share-item")
for x in job:
    data_track_value = x.get("data-track")

    print("data-track:", data_track_value)
