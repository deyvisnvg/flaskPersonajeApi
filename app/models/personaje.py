import datetime
import requests


class Personaje:
    API = "https://rickandmortyapi.com/api/character"

    def __init__(self, name, status, especie, genero, imagen) -> None:
        self.name = name
        self.status = status
        self.especie = especie
        self.genero = genero
        self.imagen = imagen

    def obtener_personajes(self, cantidad_personajes):
        response = requests.get(self.API + '/' + cantidad_personajes)
        lista_personaje = response.json()

        return lista_personaje

    def to_json(self):
        return {
            'name': self.name,
            'status': self.status,
            'especie': self.especie,
            'genero': self.genero,
            'imagen': self.imagen
        }
