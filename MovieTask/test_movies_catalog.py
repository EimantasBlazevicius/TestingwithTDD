import movies_catalog


def test_create_movie_object(mock_movie):
    assert mock_movie.title == "Guardians of the Galaxy III"
    assert mock_movie.imdb_rating == "8.2/10"
    assert mock_movie.release_year == "2023"
    assert eval(repr(mock_movie)) == "Guardians of the Galaxy III"


def test_add_movie_to_seen_list(mock_movie):
    my_testing_list = movies_catalog.MoviesIHaveSeen()
    assert len(my_testing_list.seen_list) == 0
    my_testing_list.add_movie(mock_movie, "10/10")
    assert len(my_testing_list.seen_list) == 1
    assert my_testing_list.seen_list[0]["rating"] == "10/10"


def test_remove_movie_from_seen_list(mock_movie):
    my_testing_list = movies_catalog.MoviesIHaveSeen()
    assert len(my_testing_list.seen_list) == 0
    my_testing_list.add_movie(mock_movie, "10/10")
    assert len(my_testing_list.seen_list) == 1
    my_testing_list.delete_movie()
    assert len(my_testing_list.seen_list) == 0


def test_remove_specific_movie_from_seen_list(mock_movie, mock_movie1, mock_movie2):
    my_testing_list = movies_catalog.MoviesIHaveSeen()
    assert len(my_testing_list.seen_list) == 0
    my_testing_list.add_movie(mock_movie, "10/10")
    my_testing_list.add_movie(mock_movie1, "10/10")
    my_testing_list.add_movie(mock_movie2, "10/10")
    assert len(my_testing_list.seen_list) == 3
    my_testing_list.delete_movie(1)
    assert my_testing_list.seen_list[1]["movie"].title == "Pokemons"


def test_prepare_data_for_display(mock_movie):
    my_seen_list = movies_catalog.MoviesIHaveSeen()
    my_created_list = movies_catalog.CreatedMovies()
    my_seen_list.add_movie(mock_movie, "10/10")
    my_created_list.add_movie(mock_movie)
    result = movies_catalog.data_about_movies_in_the_lists(my_created_list, my_seen_list)
    assert {"created": my_created_list.created, "seen": my_seen_list.seen_list} == result