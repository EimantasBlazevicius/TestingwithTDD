# 1. I should be able to create a Movie record.
# - Each movie should have a title, imdb rating, release year.

class Movie:
    def __init__(self, title, imdb_rating, release_year):
        self.title = title
        self.imdb_rating = imdb_rating
        self.release_year = release_year

    def __repr__(self):
        return repr(self.title)

# 2. I should be able to add Movies to MoviesIHaveSeen list.


class MoviesIHaveSeen:
    def __init__(self):
        self.seen_list = []

    def __len__(self):
        return len(self.seen_list)

    #2.1 - When registering movie to the list I want to be able
    #     to provide my personal rating 0-10.
    def add_movie(self, the_movie_to_add, personal_rating):
        self.seen_list.append({"movie": the_movie_to_add,
                               "rating": personal_rating})

    # 3. There should be an option to delete last movie
    # from the MoviesIHaveSeen. OR
    # - 3.1 if the id of the movie is provided remove a that movie.

    def delete_movie(self, id=-1):
        if id == -1:
            self.seen_list.pop()
        elif id in range(0, 999):
            self.seen_list.pop(id)


class CreatedMovies:
    def __init__(self):
        self.created = []

    def add_movie(self, movie):
        self.created.append(movie)


def data_about_movies_in_the_lists(created_movies_list, seen_movies_list):
    return {"created": created_movies_list.created, "seen": seen_movies_list.seen_list}

