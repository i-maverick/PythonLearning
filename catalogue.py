import random
import time


class Movie:
    def __init__(self, name, year=None, genre=None):
        self.__name = name
        self.__year = year
        self.__genre = genre

    def name(self):
        return self.__name

    def __str__(self):
        return self.__name


class Catalogue:
    def __init__(self):
        self.catalogue = {}

    def insert(self, movie):
        if movie.name() not in self.catalogue:
            self.catalogue[movie.name()] = movie
            return True
        return False

    def remove(self, movie):
        if movie.name() in self.catalogue:
            self.catalogue.remove(movie.name())
            return True
        return False

    def random(self):
        length = len(self.catalogue)
        if length == 0:
            return
        random.seed(time.time())
        num = random.randint(0, length - 1)
        keys = list(self.catalogue)
        return self.catalogue[keys[num]]


movies = Catalogue()
movies.insert(Movie("Justice League"))
movies.insert(Movie("Wish Upon"))
movies.insert(Movie("Fargo"))
movies.remove(Movie("Trainspotting"))
movies.insert(Movie("Trainspotting"))
movies.insert(Movie("Fargo"))

movie = movies.random()
print(movie.name() if movie is not None else "Catalogue is empty")
