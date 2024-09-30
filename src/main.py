from fastapi import FastAPI
from pydantic import BaseModel
import requests
import random
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Response(BaseModel):
    titulo: str
    imagenfondo: str
    resumen: str
    precio: str
    personas: str

likes = {
    "texto": "Homero Simpson, Marge Simpson y Bart Simpson",
}

@app.get("/")
def get_random_movie():
    pelicula = generate_random_movie()
    
    response = Response(
        titulo = pelicula["title"],
        imagenfondo = f"https://image.tmdb.org/t/p/w500{pelicula['backdrop_path']}",
        resumen = pelicula["overview"],
        precio = get_precio(),
        personas = get_likes()["texto"]
    )
    
    return response
    

def generate_random_movie():
    url_tmdb = "https://api.themoviedb.org/3/trending/movie/day?language=en-US&api_key=62e9afa9b26ec1658e4f7c572663a19b"

    headers = {
        "accept": "application/json"
    }

    response = requests.get(url_tmdb, headers=headers)
    peliculas = response.json()["results"]

    numero_azar = random.randint(1, 10)

    pelicula = peliculas[numero_azar]

    return pelicula

def get_likes():
    return likes

def get_precio():
    url = "https://preciotawd.onrender.com/"
    response = requests.get(url)
    return str(response.json().get("precio")) + " " +  response.json().get("moneda")    

