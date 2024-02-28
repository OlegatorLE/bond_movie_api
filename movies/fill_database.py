import os
import django
import time
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_database.settings')
django.setup()

from decouple import config as decouple_config
from movies.models import Movie, Actor

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def get_top_250_movie_ids() -> list:
    url = "https://www.imdb.com/chart/top/"

    driver = Chrome(service=Service(
        ChromeDriverManager().install()
    ))

    driver.get(url)
    time.sleep(5)
    elements = driver.find_elements(By.CLASS_NAME, 'ipc-title-link-wrapper')
    movie_ids = []
    for element in elements:
        try:
            href = element.get_attribute('href')
            movie_id = href.split('/')[4]  # Get ID from URL
            movie_ids.append(movie_id)
        except IndexError:
            continue
    return movie_ids


def fill_database() -> None:
    api_key = decouple_config("OMDb_API_KEY")  # Use your API KEY from https://www.omdbapi.com/
    movie_ids = get_top_250_movie_ids()
    for movie_id in movie_ids:
        if movie_id.startswith("tt"):
            url = f"http://www.omdbapi.com/?apikey={api_key}&i={movie_id}"
            response = requests.get(url)
            data = response.json()

            actors_list = data["Actors"].split(", ")
            actors = []
            for actor_name in actors_list:
                actor, created = Actor.objects.get_or_create(name=actor_name)
                actors.append(actor)

            if not Movie.objects.filter(title=data['Title']).exists():
                movie = Movie(
                    title=data["Title"],
                    release_year=data["Year"],
                    director=data["Director"],
                    runtime=data["Runtime"],
                    plot=data["Plot"],
                    poster=data["Poster"],
                )
                movie.save()
                movie.actors.set(actors)
                print(f"Movie '{movie.title}' has been saved with actors: {', '.join(actor.name for actor in actors)}")
            else:
                print(f"Movie '{data['Title']}' already exists in the database.")

    print("Database has been filled with top 250 movies.")


if __name__ == "__main__":
    fill_database()
