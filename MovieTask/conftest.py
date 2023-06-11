import movies_catalog
import pytest


@pytest.fixture()
def mock_movie():
    the_movie = movies_catalog.Movie("Guardians of the Galaxy III", "8.2/10",
                                     "2023")
    return the_movie


@pytest.fixture()
def mock_movie1():
    the_movie = movies_catalog.Movie("Interstellar", "9.9/10",
                                     "2015")
    return the_movie


@pytest.fixture()
def mock_movie2():
    the_movie = movies_catalog.Movie("Pokemons", "7/10",
                                     "2001")
    return the_movie
